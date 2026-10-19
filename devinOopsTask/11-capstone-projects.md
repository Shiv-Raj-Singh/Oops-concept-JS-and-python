# 11 — Capstone Projects 🚀

Three real systems, each in **both** languages, using every concept from the guide. Read the Python one, then compare the JS version — notice how the same OOP design maps across languages.

Concepts used are tagged like `[Encapsulation]` `[Polymorphism]` `[Composition]` `[Mixin]` `[Dunder]` `[Factory]`.

---

# PROJECT 1 — Bank Account System 🏦

*Encapsulation (private balance), validation via setters, inheritance, polymorphic interest, class methods, custom errors.*

## 🐍 Python

```python
from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from datetime import datetime

class InsufficientFunds(Exception): pass           # custom error type

class Transaction:                                  # [Composition part]
    def __init__(self, kind, amount):
        self.kind = kind
        self.amount = amount
        self.time = datetime.now()
    def __repr__(self):                             # [Dunder]
        return f"{self.time:%H:%M} {self.kind} ₹{self.amount}"

class Account(ABC):
    _next_id = 1                                    # class-level counter

    def __init__(self, owner, balance=0):
        self.id = Account._next_id; Account._next_id += 1
        self.owner = owner
        self._balance = 0                           # protected
        self._history = []                          # [Composition] account HAS transactions
        if balance:
            self.deposit(balance)

    @property                                       # read-only public view
    def balance(self):
        return self._balance

    def deposit(self, amount):                      # controlled write
        if amount <= 0:
            raise ValueError("deposit must be positive")
        self._balance += amount
        self._history.append(Transaction("DEPOSIT", amount))
        return self._balance

    def withdraw(self, amount):
        if amount > self._balance:
            raise InsufficientFunds(f"need ₹{amount}, have ₹{self._balance}")
        self._balance -= amount
        self._history.append(Transaction("WITHDRAW", amount))
        return self._balance

    @abstractmethod                                 # [Abstraction] every account must define
    def interest_rate(self): ...

    def apply_interest(self):                       # [Polymorphism] each child computes own rate
        interest = self._balance * self.interest_rate()
        return self.deposit(interest)

    def statement(self):
        return [str(t) for t in self._history]      # comprehension from file 01

    @classmethod                                    # [Factory]
    def from_string(cls, s):                        # "Shiv,5000" → Account
        owner, bal = s.split(",")
        return cls(owner, float(bal))

class SavingsAccount(Account):
    def interest_rate(self): return 0.04

class CurrentAccount(Account):
    def interest_rate(self): return 0.0
    def withdraw(self, amount):                     # override — overdraft allowed to -10k
        if self._balance - amount < -10_000:
            raise InsufficientFunds("overdraft limit")
        self._balance -= amount
        self._history.append(Transaction("WITHDRAW", amount))
        return self._balance

# ── usage ──
acc = SavingsAccount.from_string("Shiv,5000")       # factory
acc.deposit(2000)
acc.apply_interest()                                 # 4% interest added
print(acc.balance)                                   # 7280.0
print(acc.statement())
# ['14:32 DEPOSIT ₹5000.0', '14:32 DEPOSIT ₹2000', '14:32 DEPOSIT ₹280.0']

try:
    acc.withdraw(999999)
except InsufficientFunds as e:
    print(e)                                         # graceful failure
```

## ⚡ JavaScript

```js
class InsufficientFunds extends Error {}

class Transaction {
  constructor(kind, amount) {
    Object.assign(this, { kind, amount, time: new Date() });
  }
  toString = () => `${this.time.toLocaleTimeString()} ${this.kind} ₹${this.amount}`;
}

class Account {
  static #nextId = 1;                                // private static!

  constructor(owner, balance = 0) {
    if (new.target === Account) throw new Error("Account is abstract");
    this.id = Account.#nextId++;
    this.owner = owner;
    this.#balance = 0;
    this.#history = [];
    if (balance) this.deposit(balance);
  }

  #balance;
  #history;

  get balance() { return this.#balance; }            // read-only
  get statement() { return this.#history.map(String); } // map from file 01

  deposit(amount) {
    if (amount <= 0) throw new Error("deposit must be positive");
    this.#balance += amount;
    this.#history.push(new Transaction("DEPOSIT", amount));
    return this.#balance;
  }

  withdraw(amount) {
    if (amount > this.#balance)
      throw new InsufficientFunds(`need ₹${amount}, have ₹${this.#balance}`);
    this.#balance -= amount;
    this.#history.push(new Transaction("WITHDRAW", amount));
    return this.#balance;
  }

  interestRate() { throw new Error("implement in subclass"); }  // abstract-ish

  applyInterest() {
    return this.deposit(this.#balance * this.interestRate());
  }

  static fromString(s, Cls = this) {                 // factory + subclass-aware
    const [owner, bal] = s.split(",");
    return new Cls(owner, +bal);
  }
}

class SavingsAccount extends Account {
  interestRate() { return 0.04; }
}

class CurrentAccount extends Account {
  interestRate() { return 0; }
  withdraw(amount) {                                 // override: overdraft
    if (this.balance - amount < -10000)
      throw new InsufficientFunds("overdraft limit");
    this.#recordWithdraw?.(amount);                  // note: need protected access pattern
    return this.balance;
  }
}

// ⚠️ JS gotcha: #private can't be touched by subclasses (truly private).
// For subclass access use a "protected-by-convention" _balance instead:

class Account2 {
  constructor(owner) { this._balance = 0; }          // _ = "protected"
}
// Design lesson 🆚: Python's _single_underscore was MADE for this;
// JS # fields are per-class-only — use _ for subclass-shared internals.

const acc = Account.fromString("Shiv,5000", SavingsAccount);
acc.deposit(2000);
acc.applyInterest();
console.log(acc.balance);      // 7280
console.log(acc.statement);
```

**Cross-language lesson:** Python `_x` = protected (subclass-visible), `__x` = mangled. JS `#x` = absolutely private, `_x` = the "protected" convention. Match the tool to the intent.

---

# PROJECT 2 — E-commerce Cart 🛒

*Value objects, dunders (`__eq__`, `__add__`), Strategy pattern for discounts, composition, generators.*

## 🐍 Python

```python
from dataclasses import dataclass
from functools import total_ordering
from abc import ABC, abstractmethod

@total_ordering                             # [Dunder] give __eq__+__lt__, get all 6 comparisons
@dataclass(frozen=True)                     # [Value object] immutable + auto __eq__/__hash__
class Money:
    amount: float
    currency: str = "INR"

    def __add__(self, o):                   # [Dunder] m1 + m2
        if self.currency != o.currency: raise ValueError("currency mismatch")
        return Money(self.amount + o.amount, self.currency)
    def __lt__(self, o): return self.amount < o.amount
    def __str__(self): return f"₹{self.amount:,.2f}"

@dataclass
class LineItem:
    name: str
    price: Money
    qty: int = 1
    @property
    def total(self): return Money(self.price.amount * self.qty)

# ── Strategy pattern: pluggable discounts ──
class Discount(ABC):
    @abstractmethod
    def apply(self, subtotal: Money) -> Money: ...

class NoDiscount(Discount):
    def apply(self, s): return s

class PercentDiscount(Discount):            # inject behavior at runtime
    def __init__(self, pct): self.pct = pct
    def apply(self, s): return Money(s.amount * (1 - self.pct/100), s.currency)

class FlatDiscount(Discount):
    def __init__(self, off): self.off = off
    def apply(self, s): return Money(max(0, s.amount - self.off), s.currency)

class Cart:
    def __init__(self, discount: Discount = None):
        self._items = []
        self.discount = discount or NoDiscount()      # [Dependency Injection]

    def add(self, item, qty=1):
        self._items.append(LineItem(**item) if isinstance(item, dict) else item)
        # ^ accepts dicts OR LineItems — flexible API
        return self                                       # chaining

    def __len__(self): return len(self._items)            # len(cart)
    def __iter__(self): return iter(self._items)          # for item in cart

    @property
    def subtotal(self):
        return sum((i.total for i in self._items), Money(0))  # generator expr!

    @property
    def total(self):
        return self.discount.apply(self.subtotal)            # polymorphic call

    def checkout(self):
        return f"Subtotal {self.subtotal} → Total {self.total}"

cart = Cart(PercentDiscount(10))
cart.add({"name": "Laptop", "price": Money(60000)}) \
    .add({"name": "Mouse",  "price": Money(1000), "qty": 2})

print(cart.checkout())    # Subtotal ₹62,000.00 → Total ₹55,800.00
print(len(cart))          # 2
```

## ⚡ JavaScript

```js
class Money {
  constructor(amount, currency = "INR") {
    Object.assign(this, { amount, currency });
    Object.freeze(this);                        // [Value object] frozen = immutable
  }
  add = (o) => {
    if (this.currency !== o.currency) throw new Error("currency mismatch");
    return new Money(this.amount + o.amount, this.currency);
  };
  toString = () => `₹${this.amount.toLocaleString("en-IN")}`;
  valueOf = () => this.amount;                  // enables m1 > m2, +m etc.
}

class LineItem {
  constructor({ name, price, qty = 1 }) {       // destructured params
    Object.assign(this, { name, price, qty });
  }
  get total() { return new Money(this.price.amount * this.qty); }
}

// Discount strategies as plain objects/classes — duck typing
const NoDiscount = { apply: (s) => s };
const percentDiscount = (pct) => ({             // factory fn creating strategies
  apply: (s) => new Money(s.amount * (1 - pct / 100), s.currency),
});
const flatDiscount = (off) => ({
  apply: (s) => new Money(Math.max(0, s.amount - off), s.currency),
});

class Cart {
  #items = [];

  constructor(discount = NoDiscount) {
    this.discount = discount;                   // [DI] any object with .apply()
  }

  add = (item, qty = 1) => {                    // arrow field — keeps `this`
    this.#items.push(new LineItem(item));
    return this;                                // chaining
  };

  *[Symbol.iterator]() { yield* this.#items; }  // for..of, spread, destructuring

  get size() { return this.#items.length; }

  get subtotal() {
    return this.#items.reduce((sum, i) => sum.add(i.total), new Money(0));
  }

  get total() { return this.discount.apply(this.subtotal); }

  checkout = () => `Subtotal ${this.subtotal} → Total ${this.total}`;
}

const cart = new Cart(percentDiscount(10));
cart.add({ name: "Laptop", price: new Money(60000) })
    .add({ name: "Mouse", price: new Money(1000), qty: 2 });

console.log(cart.checkout());   // Subtotal ₹62,000 → Total ₹55,800
console.log([...cart].map(i => i.name));        // iterator + spread + map
```

🆚 **Compare:** Python's `Money` uses `@dataclass(frozen=True)` for immutability; JS uses `Object.freeze`. Python's `__add__`/`__lt__` give real `+`/`<`; JS uses `.add()` + `valueOf()` workarounds. Both implement Strategy the same way — inject a `.apply()` object.

---

# PROJECT 3 — Notification Engine 🔔

*Polymorphism (send via any channel), mixins (retry/logging), ABC contract, observer pattern, async dispatch.*

## 🐍 Python

```python
from abc import ABC, abstractmethod
from functools import wraps
import time, random

# ── Mixins ── [Mixin]
class Loggable:
    def log(self, msg):
        print(f"[{type(self).__name__}] {msg}")

class Retryable:                                     # retry behavior for any sender
    max_retries = 3
    def send_with_retry(self, msg):
        for attempt in range(1, self.max_retries + 1):
            try:
                return self.send(msg)                # calls subclass's send!
            except Exception as e:
                self.log(f"attempt {attempt} failed: {e}")
                time.sleep(0.1 * attempt)            # backoff
        raise RuntimeError("all retries failed")

# ── Contract ── [Abstraction]
class Notifier(ABC):
    @abstractmethod
    def send(self, msg): ...
    channel = "generic"

# ── Channels ── [Polymorphism]
class EmailNotifier(Retryable, Loggable, Notifier):
    channel = "email"
    def send(self, msg):
        if random.random() < 0.3:
            raise ConnectionError("SMTP timeout")    # simulate flakiness
        return f"📧 {msg}"

class SMSNotifier(Retryable, Loggable, Notifier):
    channel = "sms"
    def send(self, msg): return f"📱 {msg}"

class PushNotifier(Loggable, Notifier):
    channel = "push"
    def send(self, msg): return f"🔔 {msg}"

# ── Observer pattern: event bus ──
class EventBus:
    def __init__(self):
        self._subscribers = {}                       # event → list of callables

    def on(self, event, handler):                    # subscribe
        self._subscribers.setdefault(event, []).append(handler)
        return self

    def emit(self, event, **payload):                # publish
        for h in self._subscribers.get(event, []):
            h(**payload)

# ── Wiring it together ──
bus = EventBus()
senders = [EmailNotifier(), SMSNotifier(), PushNotifier()]

# every "server_down" event → all channels notified (polymorphic fan-out)
for s in senders:
    bus.on("server_down", lambda msg, s=s: s.send_with_retry(msg)
                             if isinstance(s, Retryable) else s.send(msg))

bus.emit("server_down", msg="DB connection lost!")
# [EmailNotifier] attempt 1 failed: SMTP timeout
# 📧 DB connection lost!   📱 DB connection lost!   🔔 DB connection lost!
```

## ⚡ JavaScript

```js
// ── Mixins ──
const Loggable = (Base) => class extends Base {
  log = (msg) => console.log(`[${this.constructor.name}] ${msg}`);
};

const Retryable = (Base) => class extends Base {
  static maxRetries = 3;
  async sendWithRetry(msg) {
    for (let attempt = 1; attempt <= this.constructor.maxRetries; attempt++) {
      try { return this.send(msg); }
      catch (e) {
        this.log?.(`attempt ${attempt} failed: ${e.message}`);
        await new Promise(r => setTimeout(r, 100 * attempt));   // backoff
      }
    }
    throw new Error("all retries failed");
  }
};

// ── Contract (JS-style: assert shape) ──
class Notifier {
  constructor() {
    if (new.target === Notifier) throw new Error("abstract");
    if (typeof this.send !== "function" || this.send === Notifier.prototype.send)
      throw new Error("must implement send()");
  }
  send() { throw new Error("implement send()"); }
}

// ── Channels ──
class EmailNotifier extends Retryable(Loggable(Notifier)) {
  send(msg) {
    if (Math.random() < 0.3) throw new Error("SMTP timeout");
    return `📧 ${msg}`;
  }
}
class SMSNotifier extends Retryable(Loggable(Notifier)) {
  send = (msg) => `📱 ${msg}`;
}
class PushNotifier extends Loggable(Notifier) {
  send = (msg) => `🔔 ${msg}`;
}

// ── Observer — Node-style event bus in ~15 lines ──
class EventBus {
  #subs = new Map();
  on(event, handler) {
    this.#subs.set(event, [...(this.#subs.get(event) ?? []), handler]);
    return this;
  }
  emit(event, payload = {}) {
    return (this.#subs.get(event) ?? []).map(h => h(payload));
  }
}

const bus = new EventBus();
const senders = [new EmailNotifier(), new SMSNotifier(), new PushNotifier()];

for (const s of senders) {
  bus.on("server_down", ({ msg }) =>
    s.sendWithRetry ? s.sendWithRetry(msg) : s.send(msg));   // capability check
}

await bus.emit("server_down", { msg: "DB connection lost!" });
```

🆚 **Compare the mixin styles:** Python — `class E(Retryable, Loggable, Notifier)` (real multiple inheritance, MRO handles order). JS — `class E extends Retryable(Loggable(Notifier))` (nested factory functions, fake-multiple-inheritance).

---

# 📋 Concept coverage checklist

| Concept | File | Used in project |
|---------|------|-----------------|
| Classes, objects, ctor | 03 | all |
| `self`/`this`, binding | 03, 05 | all |
| Instance/class/static | 05 | `#nextId`, `fromString`, `maxRetries` |
| Encapsulation, `#`/`__`/`_` | 04 | `#balance`, `#items`, `_history` |
| Getters/setters/`@property` | 04 | `balance`, `total`, `subtotal` |
| Inheritance, `super` | 06 | `SavingsAccount(Account)` |
| MRO / prototype chain | 06, 09 | mixin resolution |
| Polymorphism, duck typing | 07 | `send()`, `discount.apply()` |
| Dunders / Symbols | 07, 09 | `__add__`, `__eq__`, `Symbol.iterator`, `valueOf` |
| Abstraction / ABC | 08 | `Account`, `Notifier` |
| `@dataclass`, `__slots__` | 03, 09 | `Money`, `LineItem` |
| Composition / DI | 10 | `Cart(discount)`, `Checkout(gateway)` |
| Mixins | 10 | `Loggable`, `Retryable` |
| Strategy, Observer, Factory | 10, 11 | discounts, `EventBus`, `fromString` |
| Lambdas, comprehensions, arrow fns, spread | 01 | `map(String)`, `[...cart]`, generator `sum(...)` |

---

## 🏁 Where to go next

1. **Rebuild each project from memory** — peek only when stuck
2. **Extend them:** add `UPI` payment to project 1, `CouponDiscount` to project 2, `SlackNotifier` to project 3 — feel how polymorphism makes it painless
3. **Break things deliberately:** remove `send()` from a notifier — watch ABC fail fast; subclass `#balance` access in JS — feel why `protected` exists
4. Then: `async`/`await` in classes, `typing.Protocol` (Python), TypeScript interfaces (JS)

You've got the full picture — from `class Product:` down to descriptors and prototype chains. Go build something. 🚀
