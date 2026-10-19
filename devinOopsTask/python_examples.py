"""
╔══════════════════════════════════════════════════════════════════╗
║   PYTHON OOP — COMPLETE RUNNABLE EXAMPLES (Beginner → Advanced)   ║
║   Companion to the devinOopsTask/*.md guide.                      ║
║                                                                  ║
║   HOW TO USE:                                                    ║
║     python3 python_examples.py        → runs everything          ║
║     OR copy a SECTION into your own file to study it alone.      ║
║                                                                  ║
║   Every section prints its title so you can match console output ║
║   to the code. Comments show expected output with  # →           ║
╚══════════════════════════════════════════════════════════════════╝
"""

import math
import copy
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, replace
from functools import total_ordering, singledispatchmethod


def section(title):
    """Pretty section header — helper so output is easy to follow."""
    print(f"\n{'═' * 62}\n  {title}\n{'═' * 62}")


# ════════════════════════════════════════════════════════════════════
# SECTION 0 — MODERN SYNTAX QUICK TOUR (used everywhere below)
# ════════════════════════════════════════════════════════════════════
section("0 · Modern syntax: lambda / comprehension / ternary / generator / unpacking")

# --- lambda: tiny anonymous function, ONE expression only -----------
square = lambda x: x * x
print(square(9))                                       # → 81

items = [{"n": "Mouse", "p": 500}, {"n": "Laptop", "p": 60000}, {"n": "KB", "p": 2000}]
print(sorted(items, key=lambda i: i["p"]))             # sorted by price
print(list(map(lambda i: i["n"], items)))              # ['Mouse','Laptop','KB']
print(list(filter(lambda i: i["p"] > 1000, items)))    # Laptop + KB

# --- comprehensions: one-line loops that build collections ----------
prices = [i["p"] for i in items]                       # list comp
catalog = {i["n"]: i["p"] for i in items}              # dict comp
cheap = [i["n"] for i in items if i["p"] < 5000]       # transform + filter
print(prices, catalog, cheap)

# --- ternary: one-line if/else --------------------------------------
price = -5
label = "invalid" if price < 0 else ("free" if price == 0 else "paid")
print(label)                                           # → invalid

# --- generator expression: lazy — nothing computed until pulled -----
lazy = (i["p"] * 2 for i in items)
print(next(lazy))                                      # → 1000 (first item only)
total = sum(i["p"] for i in items)                     # no intermediate list
print(total)                                           # → 62500

# --- unpacking -------------------------------------------------------
first, *rest = [10, 20, 30]                            # first=10, rest=[20,30]
merged = {**catalog, "GiftCard": 250}                  # dict spread + add
print(merged)


# ════════════════════════════════════════════════════════════════════
# SECTION 1 — CLASSES, OBJECTS, self, AND WHAT REALLY HAPPENS
# ════════════════════════════════════════════════════════════════════
section("1 · Classes & objects — internals")

class Product:
    currency = "INR"                                   # CLASS attr — one shared copy

    def __init__(self, name, price):                   # runs AFTER object exists
        self.name = name                               # self = the new object
        self.price = price                             # INSTANCE attrs

    def total(self, qty=1):                            # instance method
        return self.price * qty

laptop = Product("Laptop", 60000)
mouse = Product("Mouse", 500)

# 🔬 What Python did for `Product("Laptop", 60000)`:
#   1. obj = Product.__new__(Product)            ← create empty object
#   2. Product.__init__(obj, "Laptop", 60000)    ← fill it  (obj IS self)
#   3. return obj → bound to `laptop`

print(laptop.__dict__)          # {'name': 'Laptop', 'price': 60000} — instance data only
print(laptop.currency)          # 'INR' — not in instance → found on class
print(Product.__dict__["total"] is not None)   # True — method lives ON THE CLASS

# 🔬 self is injected — these two calls are IDENTICAL:
print(laptop.total(2))          # → 120000  (normal way)
print(Product.total(laptop, 2)) # → 120000  (explicit way — proof!)

# 🔬 bound method vs function:
print(laptop.total)             # <bound method Product.total of ...>
print(Product.total)            # <function Product.total ...>
print(laptop.total.__self__ is laptop)         # True — self pre-attached
print(laptop.total.__func__ is Product.total)  # True — same function

# ⚠️ Mutable class attribute trap:
class BadCart:
    items = []                                     # SHARED by all carts!

b1, b2 = BadCart(), BadCart()
b1.items.append("x")
print(b2.items)              # ['x'] — LEAKED! fix: self.items = [] in __init__


# ════════════════════════════════════════════════════════════════════
# SECTION 2 — INSTANCE / CLASS / STATIC METHODS
# ════════════════════════════════════════════════════════════════════
section("2 · instance vs @classmethod vs @staticmethod")

class User:
    count = 0                                          # class-level state

    def __init__(self, name):
        self.name = name
        User.count += 1

    # instance — receives the OBJECT (self)
    def greet(self):
        return f"Hi, I'm {self.name}"

    # class — receives the CLASS (cls). Great for alternative constructors.
    @classmethod
    def from_csv(cls, line):                           # "name,age" → User
        name, _age = line.split(",")
        return cls(name)                               # cls(...) → subclass-aware!

    @classmethod
    def how_many(cls):
        return f"{cls.count} users created"

    # static — receives NOTHING. Utility that belongs to the class.
    @staticmethod
    def is_valid_name(n):
        return isinstance(n, str) and len(n.strip()) > 0

u = User.from_csv("Shiv,25")
print(u.greet())                    # → Hi, I'm Shiv
print(User.how_many())              # → 1 users created
print(User.is_valid_name("  "))     # → False

# cls vs hardcoded name — why it matters:
class Admin(User): pass
a = Admin.from_csv("Boss,40")
print(type(a).__name__)             # → Admin! (cls was Admin, not User)


# ════════════════════════════════════════════════════════════════════
# SECTION 3 — ENCAPSULATION: _, __, @property
# ════════════════════════════════════════════════════════════════════
section("3 · Encapsulation & @property")

class Wallet:
    def __init__(self, owner):
        self.owner = owner                 # public — anyone
        self._pin_hint = "4 digits"        # protected — "please don't touch" (convention)
        self.__balance = 0                 # private — name-mangled

    @property                              # GETTER — wallet.balance reads here
    def balance(self):
        return self.__balance

    @balance.setter                        # SETTER — wallet.balance = x writes here
    def balance(self, value):
        raise AttributeError("balance is read-only — use deposit()/pay()")

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("deposit must be > 0")
        self.__balance += amount
        return self

    def pay(self, amount):
        if amount > self.__balance:
            raise ValueError(f"need ₹{amount}, have ₹{self.__balance}")
        self.__balance -= amount
        return self

w = Wallet("Shiv")
w.deposit(1000).pay(300)                   # chaining — methods return self
print(w.balance)                           # → 700  (getter)

try:
    w.balance = 0
except AttributeError as e:
    print("blocked:", e)

try:
    w.__balance                            # AttributeError — mangled!
except AttributeError:
    print("w.__balance → AttributeError (mangled to _Wallet__balance)")

# 🔬 name mangling revealed — obfuscation, not a real vault:
print(w._Wallet__balance)                  # → 700 — reachable if you know the trick
print(w.__dict__)                          # shows '_Wallet__balance': 700

# @property for COMPUTED values (never stored):
class Circle:
    def __init__(self, r):
        self.radius = r                    # goes through setter → validated in ctor too

    @property
    def radius(self):  return self._r

    @radius.setter
    def radius(self, v):
        if v < 0: raise ValueError("radius < 0")
        self._r = v                        # underscore = real storage (avoid recursion!)

    @property
    def area(self):                        # computed on the fly
        return math.pi * self._r ** 2

c = Circle(2)
print(f"{c.area:.2f}")                     # → 12.57
c.radius = 3
print(f"{c.area:.2f}")                     # → 28.27


# ════════════════════════════════════════════════════════════════════
# SECTION 4 — INHERITANCE, super(), MRO
# ════════════════════════════════════════════════════════════════════
section("4 · Inheritance & super()")

class Vehicle:
    def __init__(self, brand, wheels):
        self.brand, self.wheels = brand, wheels
    def describe(self):
        return f"{self.brand}, {self.wheels} wheels"

class Car(Vehicle):
    def __init__(self, brand, doors):
        super().__init__(brand, wheels=4)  # parent fills its part first
        self.doors = doors                  # then child adds its own
    def describe(self):                     # override...
        return super().describe() + f", {self.doors} doors"   # ...but reuse parent

print(Car("Tata", 4).describe())           # → Tata, 4 wheels, 4 doors
print(isinstance(Car("x", 2), Vehicle))    # True — Car IS-A Vehicle
print(Car.__mro__)                         # (Car, Vehicle, object)


# --- Diamond problem + cooperative super() ---------------------------
class A:
    def hello(self):
        print("A", end=" ")
        # no super().hello() — object has none

class B(A):
    def hello(self):
        print("B", end=" ")
        super().hello()                    # goes to NEXT in MRO — which is C, not A!

class C(A):
    def hello(self):
        print("C", end=" ")
        super().hello()

class D(B, C): pass

print("\nMRO:", [k.__name__ for k in D.__mro__])   # [D, B, C, A, object]
D().hello()                                        # prints: B C A
print()                                            # newline


# ════════════════════════════════════════════════════════════════════
# SECTION 5 — POLYMORPHISM & DUCK TYPING
# ════════════════════════════════════════════════════════════════════
section("5 · Polymorphism & duck typing")

class EmailNotifier:
    def send(self, msg): return f"📧 Email → {msg}"
class SMSNotifier:
    def send(self, msg): return f"📱 SMS → {msg}"
class Pigeon:                                       # NO shared parent!
    def send(self, msg): return f"🕊️ Pigeon → {msg}"

def broadcast(notifiers, msg):
    # duck typing: works with ANYTHING that has .send()
    return [n.send(msg) for n in notifiers]

for line in broadcast([EmailNotifier(), SMSNotifier(), Pigeon()], "Deploy done"):
    print(line)


# ════════════════════════════════════════════════════════════════════
# SECTION 6 — DUNDER METHODS (operator overloading)
# ════════════════════════════════════════════════════════════════════
section("6 · Dunder methods — your objects speak Python")

@total_ordering                              # give __eq__ + __lt__, get all 6 for free
class Money:
    """Value object — immutable, comparable, printable, addable."""
    def __init__(self, amount, currency="INR"):
        self.amount, self.currency = amount, currency

    def __add__(self, other):                # m1 + m2
        if self.currency != other.currency:
            raise ValueError("currency mismatch")
        return Money(self.amount + other.amount, self.currency)

    def __eq__(self, other):                 # ==
        return isinstance(other, Money) and (self.amount, self.currency) == (other.amount, other.currency)

    def __lt__(self, other):                 # <  (total_ordering derives >,<=,>=,!=)
        return self.amount < other.amount

    def __hash__(self):                      # needed for set/dict keys
        return hash((self.amount, self.currency))

    def __repr__(self):                      # developer view
        return f"Money({self.amount}, '{self.currency}')"

    def __str__(self):                       # print() view
        return f"₹{self.amount:,.2f}"

m1, m2 = Money(500), Money(300)
print(m1 + m2)              # ₹800.00        → __add__ then __str__
print(repr(m1))             # Money(500, 'INR') → __repr__
print(m1 > m2)              # True           → __lt__ flipped by total_ordering
print(sorted([m2, m1]))     # [Money(300...), Money(500...)]
print({m1, Money(500)})     # {Money(500,'INR')} — dedup via __eq__+__hash__

# A class behaving like a container:
class Playlist:
    def __init__(self, *songs): self._songs = list(songs)
    def __len__(self):      return len(self._songs)        # len(pl)
    def __getitem__(self, i): return self._songs[i]        # pl[0], slicing free!
    def __contains__(self, s): return s in self._songs     # "x" in pl
    def __iter__(self):     return iter(self._songs)       # for s in pl
    def __call__(self):     return f"▶ {len(self)} songs"  # pl()

pl = Playlist("song1", "song2", "song3")
print(len(pl), pl[0], "song2" in pl, pl())
print([s.upper() for s in pl])               # iteration powers comprehensions


# ════════════════════════════════════════════════════════════════════
# SECTION 7 — ABSTRACTION (ABC + abstractmethod + template method)
# ════════════════════════════════════════════════════════════════════
section("7 · Abstract base classes")

class Exporter(ABC):
    """Contract: every exporter MUST parse() and format_row().
       The export() template is fixed — children fill in the steps."""

    def export(self, rows):                                # TEMPLATE METHOD
        data = self.parse(rows)                            # child step 1
        return "\n".join(self.format_row(r) for r in data) # child step 2

    @abstractmethod
    def parse(self, rows): ...

    @abstractmethod
    def format_row(self, row): ...

class CSVExporter(Exporter):
    def parse(self, rows):      return rows
    def format_row(self, row):  return ",".join(str(c) for c in row)

class MarkdownExporter(Exporter):
    def parse(self, rows):      return rows
    def format_row(self, row):  return "| " + " | ".join(str(c) for c in row) + " |"

try:
    Exporter()                 # ❌ TypeError: abstract class
except TypeError as e:
    print("blocked:", e)

rows = [["name", "price"], ["mouse", 500]]
print(CSVExporter().export(rows))
print(MarkdownExporter().export(rows))

# 🔬 internals — ABCMeta collects abstracts into a frozenset:
print(Exporter.__abstractmethods__)        # frozenset({'parse','format_row'})
print(CSVExporter.__abstractmethods__)     # frozenset() — empty → instantiable


# ════════════════════════════════════════════════════════════════════
# SECTION 8 — DATACLASSES (auto-generated boilerplate)
# ════════════════════════════════════════════════════════════════════
section("8 · @dataclass — let Python write the boilerplate")

@dataclass
class Product2:
    """__init__, __repr__, __eq__ all generated automatically."""
    name: str
    price: float
    tags: list = field(default_factory=list)    # safe mutable default
    in_stock: bool = True

p = Product2("Mouse", 500)
print(p)                                     # Product2(name='Mouse', price=500, ...)
print(p == Product2("Mouse", 500))           # True — free __eq__
p2 = replace(p, price=450)                   # clone with changes (like {...p})
print(p2.price, p.price)                     # 450 500 — original untouched

@dataclass(frozen=True)                      # immutable value object
class Color:
    r: int; g: int; b: int
    def hex(self): return f"#{self.r:02x}{self.g:02x}{self.b:02x}"

red = Color(255, 0, 0)
print(red.hex())                             # → #ff0000
# red.r = 0                                  # FrozenInstanceError!

@dataclass(order=True)                       # generates <,<=,>,>= from fields (in order)
class Task:
    priority: int
    title: str = field(compare=False)        # excluded from ordering
print(sorted([Task(2, "b"), Task(1, "a")]))  # priority 1 first


# ════════════════════════════════════════════════════════════════════
# SECTION 9 — COMPOSITION, MIXINS, DEPENDENCY INJECTION
# ════════════════════════════════════════════════════════════════════
section("9 · Composition > inheritance, mixins")

# --- Composition: HAS-A ---------------------------------------------
class Engine:
    def start(self): return "engine on"
class GPS:
    def route(self, dest): return f"routing→{dest}"

class SmartCar:                              # Car HAS parts — not IS parts
    def __init__(self, engine=None):
        self.engine = engine or Engine()     # injectable — swap for tests!
        self.gps = GPS()
    def drive(self, dest):
        return f"{self.engine.start()}, {self.gps.route(dest)}"

class ElectricEngine(Engine):
    def start(self): return "silent hum"

print(SmartCar().drive_to if False else SmartCar().drive("office"))
print(SmartCar(ElectricEngine()).drive("gym"))   # runtime swap!

# --- Mixins: small reusable feature packs ----------------------------
class JsonMixin:
    def to_dict(self): return dict(self.__dict__)

class ReprMixin:
    def __repr__(self): return f"{type(self).__name__}({self.__dict__})"

class Employee(JsonMixin, ReprMixin):        # mix in both features
    def __init__(self, name, salary):
        self.name, self.salary = name, salary

e = Employee("Shiv", 80000)
print(e.to_dict())                           # from JsonMixin
print(e)                                     # from ReprMixin


# ════════════════════════════════════════════════════════════════════
# SECTION 10 — ADVANCED: __new__, __slots__, __init_subclass__, descriptor
# ════════════════════════════════════════════════════════════════════
section("10 · Deep internals")

# --- __new__ : the object CREATED before __init__ fills it -----------
class NormalizedEmail(str):                  # str is immutable → must override __new__
    def __new__(cls, value):
        return super().__new__(cls, value.strip().lower())

email = NormalizedEmail("  Shiv@EXAMPLE.com ")
print(email)                                 # → shiv@example.com (already normalized!)

# --- Singleton via __new__ -------------------------------------------
class DBConnection:
    _instance = None
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.queries = 0
        return cls._instance

d1, d2 = DBConnection(), DBConnection()
d1.queries += 1
print(d1 is d2, d2.queries)                  # True 1 — same object

# --- __slots__ : fixed memory layout ----------------------------------
class Point3D:
    __slots__ = ("x", "y", "z")
    def __init__(self, x, y, z): self.x, self.y, self.z = x, y, z

pt = Point3D(1, 2, 3)
try:
    pt.w = 4                                 # no __dict__ → AttributeError
except AttributeError as e:
    print("slots blocked:", e)

# --- __init_subclass__ : run code when someone SUBCLASSES you --------
class Plugin:
    registry = {}
    def __init_subclass__(cls, **kw):        # fires on every `class X(Plugin)`
        super().__init_subclass__(**kw)
        Plugin.registry[cls.__name__] = cls

class AuthPlugin(Plugin):
    def run(self): return "auth running"
class CachePlugin(Plugin):
    def run(self): return "cache running"

print(list(Plugin.registry))                 # ['AuthPlugin','CachePlugin'] auto-registered!

# --- Hand-rolled descriptor (what @property is built on) -------------
class Positive:
    """Descriptor: __set__ intercepts EVERY assignment."""
    def __set_name__(self, owner, name):     # learn which attr name I guard
        self.name = "_" + name
    def __get__(self, obj, cls):
        return getattr(obj, self.name)
    def __set__(self, obj, value):
        if value < 0: raise ValueError(f"{self.name} must be ≥ 0")
        setattr(obj, self.name, value)

class Item:
    price = Positive()                       # descriptor instance on the class
    stock = Positive()
    def __init__(self, price, stock):
        self.price, self.stock = price, stock   # both validated!

item = Item(500, 10)
try:
    item.stock = -1
except ValueError as e:
    print("descriptor blocked:", e)


# ════════════════════════════════════════════════════════════════════
# SECTION 11 — ITERATORS, CONTEXT MANAGERS, REFLECTION
# ════════════════════════════════════════════════════════════════════
section("11 · Iteration protocol, with-statement, reflection")

class Countdown:
    def __init__(self, n): self.n = n
    def __iter__(self):                      # for x in Countdown(3)
        while self.n > 0:
            yield self.n                     # generator method!
            self.n -= 1

print(list(Countdown(3)))                    # [3, 2, 1]

class ManagedResource:
    def __enter__(self):                     # with R() as r: → this runs first
        print("acquired")
        return self
    def __exit__(self, exc_type, exc, tb):   # runs on exit — EVEN on error
        print("released (even if error above)")
        return False                         # don't suppress exceptions

with ManagedResource() as r:
    print("working...")

# reflection / introspection
print(laptop.__class__.__name__)             # 'Product'
print(getattr(laptop, "name"))               # dynamic read
setattr(laptop, "price", 55000)              # dynamic write
print(hasattr(laptop, "total"))              # True
print([m for m in dir(laptop) if not m.startswith("_")][:4])


# ════════════════════════════════════════════════════════════════════
# SECTION 12 — SHALLOW vs DEEP COPY
# ════════════════════════════════════════════════════════════════════
section("12 · shallow vs deep copy")

orig = {"cart": ["a", "b"], "user": {"name": "shiv"}}
shallow = copy.copy(orig)                    # new outer box — inner refs SHARED
deep = copy.deepcopy(orig)                   # fully independent

shallow["cart"].append("X")
shallow["user"]["name"] = "HACKED"
print(orig["cart"], orig["user"]["name"])    # ['a','b','X'] HACKED — leaked!
print(deep["cart"], deep["user"]["name"])    # ['a','b'] shiv — safe ✅


# ════════════════════════════════════════════════════════════════════
# SECTION 13 — MINI PROJECT: E-commerce (puts it all together)
# ════════════════════════════════════════════════════════════════════
section("13 · Mini project — Cart with Strategy discounts")

@total_ordering
@dataclass(frozen=True)
class Price:                                 # immutable value object
    amount: float
    def __add__(self, o): return Price(self.amount + o.amount)
    def __lt__(self, o):  return self.amount < o.amount
    def __str__(self):    return f"₹{self.amount:,.2f}"

class Discount(ABC):                         # Strategy contract
    @abstractmethod
    def apply(self, subtotal: Price) -> Price: ...

class NoDiscount(Discount):
    def apply(self, s): return s

class PercentOff(Discount):
    def __init__(self, pct): self.pct = pct
    def apply(self, s): return Price(s.amount * (1 - self.pct / 100))

class FlatOff(Discount):
    def __init__(self, off): self.off = off
    def apply(self, s): return Price(max(0, s.amount - self.off))

@dataclass
class LineItem:
    name: str
    price: Price
    qty: int = 1
    @property
    def total(self): return Price(self.price.amount * self.qty)

class Cart:
    def __init__(self, discount: Discount = None):
        self._items = []
        self.discount = discount or NoDiscount()      # dependency injection

    def add(self, name, price, qty=1):
        self._items.append(LineItem(name, Price(price), qty))
        return self                                    # chaining

    def __len__(self):  return len(self._items)
    def __iter__(self): return iter(self._items)

    @property
    def subtotal(self):
        return sum((i.total for i in self), Price(0))  # generator inside sum!

    @property
    def total(self):
        return self.discount.apply(self.subtotal)      # polymorphic call

cart = Cart(PercentOff(10))
cart.add("Laptop", 60000).add("Mouse", 500, qty=2).add("Keyboard", 2000)

print(f"items: {len(cart)}")
for i in cart:
    print(f"  {i.name:10} {i.qty}× {i.price} = {i.total}")
print(f"subtotal: {cart.subtotal}")
print(f"total (−10%): {cart.total}")

# swap strategy at runtime — no code change to Cart:
cart.discount = FlatOff(5000)
print(f"total (−₹5000): {cart.total}")

print("\n✅ All sections executed — OOP in Python: covered end to end.\n")
