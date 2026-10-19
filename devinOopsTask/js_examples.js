/**
 * ╔══════════════════════════════════════════════════════════════════╗
 * ║  JAVASCRIPT OOP — COMPLETE RUNNABLE EXAMPLES (Beginner → Advanced)║
 * ║  Companion to the devinOopsTask/*.md guide.                       ║
 * ║                                                                 ║
 * ║  HOW TO USE:                                                    ║
 * ║    node js_examples.js            → runs everything             ║
 * ║    OR copy a SECTION into your own file to study it alone.      ║
 * ║                                                                 ║
 * ║  Expected output is shown in comments with  // →                ║
 * ╚══════════════════════════════════════════════════════════════════╝
 */

const section = (title) =>
  console.log(`\n${"═".repeat(62)}\n  ${title}\n${"═".repeat(62)}`);


// ════════════════════════════════════════════════════════════════════
// SECTION 0 — MODERN SYNTAX QUICK TOUR (used everywhere below)
// ════════════════════════════════════════════════════════════════════
section("0 · Modern syntax: arrow fns, spread/rest, destructuring, template literals");

// --- arrow functions: shorter functions, borrow `this` --------------
const square = (x) => x * x;
const add = (a, b) => a + b;                       // implicit return
const makeUser = (name) => ({ name, role: "user" }); // () wraps returned object!
console.log(square(9), add(2, 3), makeUser("shiv"));

// --- spread: unpack --------------------------------------------------
const nums = [1, 2, 3];
const more = [...nums, 4];                          // [1,2,3,4]
const base = { name: "Mouse", price: 500 };
const sale = { ...base, price: 400 };               // override AFTER spread
console.log(more, sale);

// --- rest: pack ------------------------------------------------------
const sum = (...ns) => ns.reduce((a, b) => a + b, 0);
console.log(sum(1, 2, 3, 4));                       // → 10
const [head, ...tail] = [10, 20, 30];               // head=10, tail=[20,30]

// --- destructuring ---------------------------------------------------
const { name, price, rating = 5 } = base;           // rename/defaults
const showItem = ({ name, price }) => `${name}: ₹${price}`;
console.log(showItem(base));                        // → Mouse: ₹500

// --- array methods (you'll see these constantly) ---------------------
const products = [
  { n: "Mouse", p: 500 },
  { n: "Laptop", p: 60000 },
  { n: "KB", p: 2000 },
];
console.log(products.map((i) => i.n));                     // names
console.log(products.filter((i) => i.p > 1000));           // Laptop, KB
console.log(products.reduce((t, i) => t + i.p, 0));        // 62500
console.log(products.find((i) => i.p > 1000));             // Laptop

// --- optional chaining & nullish coalescing --------------------------
const cfg = {};
console.log(cfg.theme?.color);    // undefined — no crash
console.log(cfg.port ?? 3000);    // 3000 — ?? only skips null/undefined
console.log(0 ?? 99, 0 || 99);    // 0 99 — || wrongly rejects 0!


// ════════════════════════════════════════════════════════════════════
// SECTION 1 — CLASSES, OBJECTS, `this`, AND WHAT `new` REALLY DOES
// ════════════════════════════════════════════════════════════════════
section("1 · Classes & objects — internals");

class Product {
  static taxRate = 0.18;                       // class-level (static) field
  #category = "electronics";                   // PRIVATE field — invisible outside

  constructor(name, price) {
    this.name = name;                          // instance fields
    this.price = price;
  }

  total(qty = 1) {                             // instance method (on prototype)
    return this.price * qty * (1 + Product.taxRate);
  }

  get category() { return this.#category; }    // read-only window into private
}

const laptop = new Product("Laptop", 60000);

// 🔬 What `new` did — 4 steps:
//   1. obj = {}
//   2. obj.__proto__ = Product.prototype        ← link the chain
//   3. Product.call(obj, "Laptop", 60000)       ← this = obj inside ctor
//   4. return obj

console.log(Object.keys(laptop));                            // ['name','price']
console.log(laptop.category);                                // 'electronics'
// console.log(laptop.#category);                            // ❌ SyntaxError (uncomment = crash)

// 🔬 methods live on Product.prototype — ONE shared copy:
console.log(Object.getPrototypeOf(laptop) === Product.prototype); // true
console.log(laptop.hasOwnProperty("total"));                        // false — on prototype!
console.log(laptop.total === Product.prototype.total);              // true — same fn
console.log(laptop.total(2));                                       // 141600 (with tax)

// 🔬 the prototype chain:
// laptop → Product.prototype → Object.prototype → null
console.log(Object.getPrototypeOf(Product.prototype) === Object.prototype); // true
console.log(laptop instanceof Product, laptop instanceof Object);           // true true


// ════════════════════════════════════════════════════════════════════
// SECTION 2 — `this` BINDING: THE 4 RULES
// ════════════════════════════════════════════════════════════════════
section("2 · this — implicit / explicit / new / arrow");

const shop = {
  name: "TechStore",
  describe() { return `shop: ${this.name}`; },
};

console.log(shop.describe());                 // 'shop: TechStore' — implicit binding

const stolen = shop.describe;
try {
  console.log(stolen());                      // this = undefined in strict → TypeError
} catch (e) {
  console.log("stolen() broke:", e.message);
}

// Fix 1 — bind() glues `this` permanently:
const bound = shop.describe.bind(shop);
console.log(bound());                         // 'shop: TechStore'

// Fix 2 — arrow field captures `this` at creation:
class Counter {
  count = 0;
  increment = () => {                          // arrow → `this` locked to instance
    this.count++;
    return this.count;
  };
}
const c = new Counter();
const ref = c.increment;
console.log(ref(), ref());                     // 1 2 — works even detached!

// 🔬 inside methods, arrows borrow the method's `this`:
class Ticker {
  label = "tick";
  start() {
    // setTimeout(function(){ this.label }, ...) would LOSE this
    setTimeout(() => console.log("arrow sees:", this.label), 0);  // 'tick' ✅
  }
}
new Ticker().start();


// ════════════════════════════════════════════════════════════════════
// SECTION 3 — ENCAPSULATION: #, _, get/set
// ════════════════════════════════════════════════════════════════════
section("3 · Encapsulation — #private vs _convention vs getters");

class BankAccount {
  #balance = 0;                                // HARD private — SyntaxError outside
  #history = [];

  constructor(owner) {
    this.owner = owner;                        // public
  }

  deposit(amount) {
    if (amount <= 0) throw new Error("deposit must be > 0");
    this.#balance += amount;
    this.#history.push(`+₹${amount}`);
    return this;                               // chaining
  }

  pay(amount) {
    if (amount > this.#balance)
      throw new Error(`need ₹${amount}, have ₹${this.#balance}`);
    this.#balance -= amount;
    this.#history.push(`-₹${amount}`);
    return this;
  }

  get balance() { return this.#balance; }      // read-only view
  get history() { return [...this.#history]; } // defensive copy — spread!
  set balance(v) { throw new Error("use deposit()/pay()"); }
}

const acc = new BankAccount("Shiv");
acc.deposit(1000).pay(300);
console.log(acc.balance);                      // → 700 (getter)
console.log(acc.history);                      // ['+₹1000','-₹300']

try { acc.balance = 0; }    catch (e) { console.log("blocked:", e.message); }
try { acc.pay(9999); }      catch (e) { console.log("blocked:", e.message); }
console.log(Object.keys(acc));                 // ['owner'] — #fields INVISIBLE even to keys!

// private METHOD too:
class Order {
  checkout() {
    this.#fraudCheck();
    return "order placed";
  }
  #fraudCheck() { /* internal — invisible outside */ }
}
console.log(new Order().checkout());

// get/set that VALIDATE (your Product pattern, fixed):
class SafeProduct {
  #price = 0;
  constructor(name, price) {
    this.name = name;
    this.price = price;                        // goes through setter
  }
  get price() { return this.#price; }
  set price(v) {
    if (v < 0) throw new Error("price < 0");
    this.#price = v;
  }
  get priceWithGST() { return this.#price * 1.18; }  // computed, not stored
}
const sp = new SafeProduct("Mouse", 1000);
sp.price = 1500;
console.log(sp.priceWithGST);                  // 1770
try { sp.price = -5; } catch (e) { console.log("blocked:", e.message); }


// ════════════════════════════════════════════════════════════════════
// SECTION 4 — INHERITANCE: extends, super, prototype chain
// ════════════════════════════════════════════════════════════════════
section("4 · Inheritance — extends / super / the real chain");

class Vehicle {
  constructor(brand, wheels) {
    this.brand = brand;
    this.wheels = wheels;
  }
  describe() { return `${this.brand}, ${this.wheels} wheels`; }
}

class Car extends Vehicle {
  constructor(brand, doors) {
    super(brand, 4);                           // MUST call before `this`!
    this.doors = doors;
  }
  describe() {
    return `${super.describe()}, ${this.doors} doors`;  // reuse parent
  }
}

const car = new Car("Tata", 4);
console.log(car.describe());                   // Tata, 4 wheels, 4 doors

// 🔬 extends actually wires TWO chains:
console.log(Object.getPrototypeOf(car) === Car.prototype);                  // instance chain
console.log(Object.getPrototypeOf(Car.prototype) === Vehicle.prototype);    // methods chain
console.log(Object.getPrototypeOf(Car) === Vehicle);                        // STATICS chain!
console.log(car instanceof Car, car instanceof Vehicle);                    // true true

// Monkey-patch prototype — affects ALL instances, even existing:
Vehicle.prototype.honk = function () { return `${this.brand} beeps`; };
console.log(car.honk());                       // works — added AFTER creation 😮

// Static methods are inherited too (via the class chain):
class Base {
  static hello() { return "base hello"; }
}
class Child extends Base {}
console.log(Child.hello());                    // 'base hello' — inherited static!


// ════════════════════════════════════════════════════════════════════
// SECTION 5 — POLYMORPHISM & DUCK TYPING
// ════════════════════════════════════════════════════════════════════
section("5 · Polymorphism & duck typing");

class EmailNotifier { send(msg) { return `📧 Email → ${msg}`; } }
class SMSNotifier   { send(msg) { return `📱 SMS → ${msg}`; } }
// not even a class — just an object with the right shape:
const pigeon = { send: (msg) => `🕊️ Pigeon → ${msg}` };

const broadcast = (notifiers, msg) => notifiers.map((n) => n.send(msg));
broadcast([new EmailNotifier(), new SMSNotifier(), pigeon], "Deploy done")
  .forEach((l) => console.log(l));

// add a channel tomorrow → broadcast() never changes. That's the point.


// ════════════════════════════════════════════════════════════════════
// SECTION 6 — JS "DUNDERS": toString / valueOf / Symbol.iterator
// ════════════════════════════════════════════════════════════════════
section("6 · JS magic hooks — toString, valueOf, Symbol.iterator");

class Money {
  constructor(amount, currency = "INR") {
    Object.assign(this, { amount, currency });
    Object.freeze(this);                       // immutable value object
  }
  add(o) {
    if (this.currency !== o.currency) throw new Error("currency mismatch");
    return new Money(this.amount + o.amount, this.currency);
  }
  toString()  { return `₹${this.amount.toLocaleString("en-IN")}`; }  // `${m}`
  valueOf()   { return this.amount; }                                // +m, m1>m2
  toJSON()    { return { amount: this.amount, cur: this.currency }; }
}

const m1 = new Money(500), m2 = new Money(300);
console.log(`${m1}`);                          // ₹500 — toString
console.log(m1 + m2);                          // 800 — valueOf on BOTH sides!
console.log(m1 > m2);                          // true — valueOf comparison
console.log(JSON.stringify(m1));               // {"amount":500,"cur":"INR"}

// Symbol.iterator — makes objects work with for..of / spread:
class Playlist {
  #songs;
  constructor(...songs) { this.#songs = songs; }
  *[Symbol.iterator]() { yield* this.#songs; }  // generator method
  get size() { return this.#songs.length; }
}
const pl = new Playlist("s1", "s2", "s3");
console.log([...pl]);                          // spread uses the iterator!
for (const s of pl) process.stdout.write(s + " ");
console.log();
console.log(pl.size);                          // 3


// ════════════════════════════════════════════════════════════════════
// SECTION 7 — ABSTRACTION JS-STYLE (no `abstract` keyword)
// ════════════════════════════════════════════════════════════════════
section("7 · Abstraction — new.target guard + structural interfaces");

class PaymentMethod {
  constructor() {
    // 🔬 new.target = the class actually being instantiated
    if (new.target === PaymentMethod)
      throw new Error("PaymentMethod is abstract");
  }
  pay()    { throw new Error("implement pay()"); }
  refund() { throw new Error("implement refund()"); }
  receipt(amount) {                            // concrete shared method OK
    return `Receipt ₹${amount} via ${this.constructor.name}`;
  }
}

class UPI extends PaymentMethod {
  pay(a)    { return `Paid ₹${a} via UPI`; }
  refund(a) { return `Refunded ₹${a}`; }
}

try { new PaymentMethod(); } catch (e) { console.log("blocked:", e.message); }
const upi = new UPI();
console.log(upi.pay(500), "|", upi.receipt(500));

// Duck-typed "interface" — the most idiomatic JS approach:
const assertNotifier = (o) => {
  if (typeof o.send !== "function") throw new TypeError("needs send()");
  return o;
};
const notify = (n, msg) => assertNotifier(n).send(msg);
console.log(notify({ send: (m) => `webhook: ${m}` }, "ping"));  // any shape works


// ════════════════════════════════════════════════════════════════════
// SECTION 8 — COMPOSITION & MIXINS (JS multiple-inheritance pattern)
// ════════════════════════════════════════════════════════════════════
section("8 · Composition & mixins");

// --- Composition: HAS-A -------------------------------------------------
class Engine { start = () => "engine on"; }
class GPS    { route = (d) => `routing→${d}`; }

class SmartCar {
  constructor(engine = new Engine()) {          // injectable dependency!
    this.engine = engine;
    this.gps = new GPS();
  }
  drive = (dest) => `${this.engine.start()}, ${this.gps.route(dest)}`;
}

class ElectricEngine extends Engine {
  start = () => "silent hum";                   // override via field arrow
}

console.log(new SmartCar().drive("office"));
console.log(new SmartCar(new ElectricEngine()).drive("gym"));   // runtime swap

// --- Mixins: (Base) => class extends Base -------------------------------
const JsonAble = (Base) => class extends Base {
  // ⚠️ name it `serialize`, NOT `toJSON` — stringify auto-calls .toJSON() → recursion!
  serialize = () => JSON.stringify({ ...this });
};
const Loggable = (Base) => class extends Base {
  log = (m) => console.log(`[${this.constructor.name}] ${m}`);
};
const Timestamped = (Base) => class extends Base {
  touch = () => (this.updatedAt = new Date().toISOString());
};

// JS has NO `extends A, B` — compose by nesting factories:
class Employee extends Timestamped(Loggable(JsonAble(Object))) {
  constructor(name, salary) {
    super();
    this.name = name;
    this.salary = salary;
  }
}
const emp = new Employee("Shiv", 80000);
emp.touch();
emp.log("created");
console.log(emp.serialize());


// ════════════════════════════════════════════════════════════════════
// SECTION 9 — DEEP INTERNALS: Object.create, closures, Reflect
// ════════════════════════════════════════════════════════════════════
section("9 · Deep internals — prototypes, closures, reflection");

// --- hand-rolled `new` ---------------------------------------------------
const manualNew = (Cls, ...args) => {
  const obj = Object.create(Cls.prototype);     // steps 1+2
  const r = Cls.apply(obj, args);               // step 3
  return r instanceof Object ? r : obj;         // step 4
};

// --- pre-`class` inheritance (what extends compiles to) -------------------
function Animal(name) { this.name = name; }
Animal.prototype.speak = function () { return `${this.name} makes a sound`; };

function Dog(name) { Animal.call(this, name); }        // "super()"
Dog.prototype = Object.create(Animal.prototype);       // wire the chain
Dog.prototype.constructor = Dog;                        // fix the pointer
Dog.prototype.speak = function () { return `${this.name} barks`; };

console.log(new Dog("Rex").speak());                    // Rex barks
console.log(new Dog("Rex") instanceof Animal);          // true

// --- closure-based OOP: privacy WITHOUT classes ---------------------------
const createCounter = (start = 0) => {
  let count = start;                             // closure variable — TRULY private
  return {
    inc: () => ++count,
    get value() { return count; },
  };
};
const ctr = createCounter(10);
ctr.inc(); ctr.inc();
console.log(ctr.value);                          // 12
console.log(ctr.count);                          // undefined — not a prop at all!

// --- reflection ------------------------------------------------------------
console.log(Reflect.ownKeys(laptop));            // ['name','price']
console.log("name" in laptop);                   // true (walks the chain)
console.log(Object.getOwnPropertyNames(Product.prototype)); // ctor, total, category

// --- structuredClone: deep copy --------------------------------------------
const orig = { cart: ["a"], user: { name: "shiv" } };
const shallow = { ...orig };                      // inner objects SHARED
const deep = structuredClone(orig);               // fully independent
shallow.user.name = "HACKED";
console.log(orig.user.name);                     // HACKED — shallow leaked
console.log(deep.user.name);                     // shiv — safe ✅


// ════════════════════════════════════════════════════════════════════
// SECTION 10 — GENERATORS + ASYNC in OOP
// ════════════════════════════════════════════════════════════════════
section("10 · Generators & async methods");

class Range {
  constructor(start, end) { [this.start, this.end] = [start, end]; }
  *[Symbol.iterator]() {                         // makes for..of work
    for (let i = this.start; i <= this.end; i++) yield i;
  }
  static *ids() {                                // static generator
    let i = 0;
    while (true) yield ++i;
  }
}
console.log([...new Range(1, 5)]);               // [1,2,3,4,5]

const idGen = Range.ids();
console.log(idGen.next().value, idGen.next().value);  // 1 2

// async method — real-world API shape:
class UserRepo {
  async findById(id) {
    await new Promise((r) => setTimeout(r, 10)); // fake DB latency
    return { id, name: `user-${id}` };
  }
}
const repo = new UserRepo();
repo.findById(7).then((u) => console.log("fetched:", u.name));


// ════════════════════════════════════════════════════════════════════
// SECTION 11 — MINI PROJECT: Notification engine (all concepts together)
// ════════════════════════════════════════════════════════════════════
section("11 · Mini project — Notification engine");

// mixins
const Retryable = (Base) => class extends Base {
  static maxRetries = 3;
  async sendWithRetry(msg) {
    for (let i = 1; i <= this.constructor.maxRetries; i++) {
      try { return this.send(msg); }
      catch (e) { this.log?.(`attempt ${i} failed: ${e.message}`); }
    }
    throw new Error("all retries failed");
  }
};
const Log = (Base) => class extends Base {
  log = (m) => console.log(`[${this.constructor.name}] ${m}`);
};

// contract
class Notifier {
  constructor() {
    if (new.target === Notifier) throw new Error("abstract");
  }
  send() { throw new Error("implement send()"); }
}

// channels — mixin composition
class Email extends Retryable(Log(Notifier)) {
  send = (m) => `📧 ${m}`;
}
class SMS extends Retryable(Log(Notifier)) {
  send = (m) => `📱 ${m}`;
}
class Push extends Log(Notifier) {
  send = (m) => `🔔 ${m}`;
}

// observer — event bus in a few lines
class EventBus {
  #subs = new Map();
  on(evt, fn) {
    this.#subs.set(evt, [...(this.#subs.get(evt) ?? []), fn]);
    return this;
  }
  emit(evt, data = {}) {
    return Promise.all((this.#subs.get(evt) ?? []).map((f) => f(data)));
  }
}

(async () => {
  const bus = new EventBus();
  const channels = [new Email(), new SMS(), new Push()];

  for (const ch of channels) {
    // capability check — duck typing: does it have sendWithRetry?
    bus.on("deploy", ({ msg }) =>
      ch.sendWithRetry ? ch.sendWithRetry(msg) : ch.send(msg));
  }

  const results = await bus.emit("deploy", { msg: "v2.0 shipped!" });
  results.flat().forEach((r) => console.log(r));
  // 📧 v2.0 shipped!  📱 v2.0 shipped!  🔔 v2.0 shipped!

  console.log("\n✅ All sections executed — OOP in JavaScript: covered end to end.\n");
})();
