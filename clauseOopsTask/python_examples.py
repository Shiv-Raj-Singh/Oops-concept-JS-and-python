"""
Complete OOP Examples in Python — Beginner to Advanced
Run sections individually or all at once.
"""

import math
from abc import ABC, abstractmethod
from dataclasses import dataclass, field, asdict
from typing import List, Callable


# ══════════════════════════════════════════════════════════════════════
# SECTION 1: PYTHON ADVANCED SYNTAX
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 1: PYTHON ADVANCED SYNTAX")
print("═"*60)

# ── Lambda ─────────────────────────────────────────────────────────
print("\n--- Lambda Functions ---")

square = lambda x: x * x
add = lambda a, b: a + b
clamp = lambda val, lo, hi: lo if val < lo else hi if val > hi else val

print(square(5))           # 25
print(add(3, 4))           # 7
print(clamp(15, 0, 10))    # 10

products = [
    {"name": "Mouse",    "price": 500},
    {"name": "Laptop",   "price": 60000},
    {"name": "Keyboard", "price": 2000},
]
by_price      = sorted(products, key=lambda p: p["price"])
by_name       = sorted(products, key=lambda p: p["name"])
expensive     = list(filter(lambda p: p["price"] > 1000, products))
doubled       = list(map(lambda p: {**p, "price": p["price"] * 2}, products))
total         = __import__("functools").reduce(lambda acc, p: acc + p["price"], products, 0)

print("Sorted by price:", [p["name"] for p in by_price])
print("Expensive items:", [p["name"] for p in expensive])
print("Total price:", total)


# ── List / Dict / Set Comprehensions ───────────────────────────────
print("\n--- Comprehensions ---")

# List comprehension
squares        = [x * x for x in range(1, 6)]
even_squares   = [x * x for x in range(1, 11) if x % 2 == 0]
flat           = [n for row in [[1,2],[3,4],[5,6]] for n in row]
print(squares)       # [1, 4, 9, 16, 25]
print(even_squares)  # [4, 16, 36, 64, 100]
print(flat)          # [1, 2, 3, 4, 5, 6]

# Dict comprehension
name_len  = {name: len(name) for name in ["Alice", "Bob", "Charlie"]}
inv_dict  = {v: k for k, v in {"a": 1, "b": 2}.items()}
print(name_len)   # {'Alice': 5, 'Bob': 3, 'Charlie': 7}
print(inv_dict)   # {1: 'a', 2: 'b'}

# Set comprehension
unique_len = {len(name) for name in ["Alice", "Bob", "Ann", "Charlie"]}
print(unique_len)  # {3, 5, 7}

# Nested comprehension — multiplication table
matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
print(matrix)  # [[1,2,3],[2,4,6],[3,6,9]]


# ── Ternary Operator ───────────────────────────────────────────────
print("\n--- Ternary Operator ---")

age    = 20
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

score = 75
grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "F"
print(grade)   # B

numbers = [1, -2, 3, -4, 5]
abs_nums = [n if n >= 0 else -n for n in numbers]
print(abs_nums)  # [1, 2, 3, 4, 5]


# ── Generator Expressions ──────────────────────────────────────────
print("\n--- Generator Expressions ---")

gen = (x * x for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4
print(list(gen))  # [9, 16]  ← remaining

# sum on generator (no list created)
total = sum(x * x for x in range(1, 101))
print(f"Sum of squares 1-100: {total}")  # 338350

# Generator function (yield)
def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

fib = fibonacci()
first_10 = [next(fib) for _ in range(10)]
print("Fibonacci:", first_10)  # [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# ══════════════════════════════════════════════════════════════════════
# SECTION 2: CLASSES & OBJECTS
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 2: CLASSES & OBJECTS")
print("═"*60)

class Dog:
    species = "Canis lupus familiaris"    # class variable

    def __init__(self, name, breed, age):
        self.name = name
        self.breed = breed
        self.age = age

    def bark(self):
        return f"{self.name} says: Woof!"

    def info(self):
        return f"{self.name} ({self.breed}), {self.age} yrs"

    def __str__(self):
        return f"Dog<{self.name}>"

    def __repr__(self):
        return f"Dog(name={self.name!r}, breed={self.breed!r}, age={self.age})"

dog1 = Dog("Bruno", "German Shepherd", 3)
dog2 = Dog("Bella", "Labrador", 2)

print(dog1.bark())        # Bruno says: Woof!
print(dog2.info())        # Bella (Labrador), 2 yrs
print(str(dog1))          # Dog<Bruno>
print(repr(dog1))         # Dog(name='Bruno', breed='German Shepherd', age=3)
print(Dog.species)        # Canis lupus familiaris
print(dog1.__class__)     # <class '__main__.Dog'>
print(dog1.__dict__)      # {'name': 'Bruno', 'breed': 'German Shepherd', 'age': 3}


# ══════════════════════════════════════════════════════════════════════
# SECTION 3: INSTANCE vs CLASS vs STATIC
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 3: INSTANCE / CLASS / STATIC VARIABLES")
print("═"*60)

class Employee:
    company = "Aquera Inc"
    _total  = 0

    def __init__(self, name, salary):
        self.name   = name
        self.salary = salary
        Employee._total += 1

    @classmethod
    def get_info(cls):
        return f"{cls.company} — {cls._total} employees"

    @classmethod
    def from_dict(cls, data):
        return cls(data["name"], data["salary"])

    @staticmethod
    def is_valid_salary(amount):
        return isinstance(amount, (int, float)) and amount > 0

    def __repr__(self):
        return f"Employee({self.name!r}, ₹{self.salary})"

e1 = Employee("Shiv", 80000)
e2 = Employee("Raj",  90000)
e3 = Employee.from_dict({"name": "Priya", "salary": 75000})

print(Employee.get_info())           # Aquera Inc — 3 employees
print(Employee.is_valid_salary(500)) # True
print(Employee.is_valid_salary(-50)) # False
print([e1, e2, e3])

# Shadow class variable on instance
e1.company = "Freelancer"
print(e1.company)     # Freelancer  (instance shadow)
print(e2.company)     # Aquera Inc  (class variable)
print(Employee.company)  # Aquera Inc  (unchanged)


# ══════════════════════════════════════════════════════════════════════
# SECTION 4: PROPERTIES — GETTERS & SETTERS
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 4: PROPERTIES")
print("═"*60)

class Circle:
    def __init__(self, radius):
        self.radius = radius     # uses setter immediately

    @property
    def radius(self):
        return self._radius

    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError(f"Radius must be ≥ 0, got {value}")
        self._radius = value

    @property
    def area(self):
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        return 2 * math.pi * self._radius

    def __repr__(self):
        return f"Circle(r={self._radius}, area={self.area:.2f})"

c = Circle(5)
print(c)              # Circle(r=5, area=78.54)
c.radius = 10
print(c.area)         # 314.16

try:
    c.radius = -3
except ValueError as e:
    print(f"Error: {e}")  # Error: Radius must be ≥ 0, got -3


# ══════════════════════════════════════════════════════════════════════
# SECTION 5: ENCAPSULATION
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 5: ENCAPSULATION")
print("═"*60)

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner        = owner      # public
        self._bank        = "HDFC"     # protected (convention)
        self.__balance    = balance    # private (name-mangled)
        self.__history    = []

    def deposit(self, amount):
        if amount <= 0:
            raise ValueError("Deposit must be positive")
        self.__balance += amount
        self.__history.append(f"+ ₹{amount}")
        return self

    def withdraw(self, amount):
        if amount <= 0:
            raise ValueError("Amount must be positive")
        if amount > self.__balance:
            raise ValueError("Insufficient funds")
        self.__balance -= amount
        self.__history.append(f"- ₹{amount}")
        return self

    @property
    def balance(self):
        return self.__balance

    @property
    def history(self):
        return self.__history.copy()    # return copy, not the real list!

    def __str__(self):
        return f"{self.owner} [{self._bank}]: ₹{self.__balance}"

acc = BankAccount("Shiv", 10000)
acc.deposit(5000).withdraw(2000)       # method chaining
print(acc)                             # Shiv [HDFC]: ₹13000
print(acc.balance)                     # 13000
print(acc.history)                     # ['+ ₹5000', '- ₹2000']
# print(acc.__balance)                 # AttributeError
print(acc._BankAccount__balance)       # 13000 (name-mangling bypass — bad practice!)


# ══════════════════════════════════════════════════════════════════════
# SECTION 6: INHERITANCE
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 6: INHERITANCE")
print("═"*60)

class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age  = age

    def breathe(self):  return f"{self.name} breathes"
    def eat(self):      return f"{self.name} eats"
    def sleep(self):    return f"{self.name} sleeps"

    def __str__(self):
        return f"{self.__class__.__name__}({self.name!r}, {self.age}yrs)"


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def bark(self): return f"{self.name}: Woof!"
    def eat(self):  return f"{self.name} eats dog food"  # override


class Cat(Animal):
    def __init__(self, name, age, indoor=True):
        super().__init__(name, age)
        self.indoor = indoor

    def purr(self): return f"{self.name} purrrs..."
    def eat(self):  return f"{self.name} eats cat food"  # override


class Guidedog(Dog):   # multilevel
    def __init__(self, name, age, breed, owner):
        super().__init__(name, age, breed)
        self.owner = owner

    def guide(self): return f"{self.name} guides {self.owner}"

animals = [
    Dog("Bruno", 3, "Labrador"),
    Cat("Whiskers", 5),
    Guidedog("Rex", 4, "Golden Retriever", "Meena"),
]

for a in animals:
    print(a, "→", a.eat())
    if isinstance(a, Dog):
        print("  Dog-specific:", a.bark())

# isinstance / issubclass
print(isinstance(animals[0], Dog))    # True
print(isinstance(animals[0], Animal)) # True (Dog IS-A Animal)
print(issubclass(Guidedog, Dog))      # True
print(issubclass(Guidedog, Animal))   # True


# ══════════════════════════════════════════════════════════════════════
# SECTION 7: MULTIPLE INHERITANCE & MRO
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 7: MULTIPLE INHERITANCE & MRO")
print("═"*60)

class Flyable:
    def fly(self):      return "I can fly!"
    def describe(self): return "Flyable"

class Swimmable:
    def swim(self):     return "I can swim!"
    def describe(self): return "Swimmable"

class Walkable:
    def walk(self):     return "I can walk!"

class Duck(Flyable, Swimmable, Walkable):
    def quack(self):    return "Quack!"

duck = Duck()
print(duck.fly())       # I can fly!
print(duck.swim())      # I can swim!
print(duck.walk())      # I can walk!
print(duck.quack())     # Quack!
print(duck.describe())  # Flyable (first in MRO)
print(Duck.__mro__)


# Diamond problem
class A:
    def hello(self): return "A"
    def __init__(self):
        print("A.__init__")
        super().__init__()

class B(A):
    def hello(self): return "B→" + super().hello()
    def __init__(self):
        print("B.__init__")
        super().__init__()

class C(A):
    def hello(self): return "C→" + super().hello()
    def __init__(self):
        print("C.__init__")
        super().__init__()

class D(B, C):
    def __init__(self):
        print("D.__init__")
        super().__init__()

print("\nDiamond MRO:", [cls.__name__ for cls in D.__mro__])
d = D()                  # B → C → A (each called once!)
print(d.hello())          # B→C→A


# ══════════════════════════════════════════════════════════════════════
# SECTION 8: POLYMORPHISM
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 8: POLYMORPHISM")
print("═"*60)

class Shape(ABC):
    @abstractmethod
    def area(self) -> float: pass

    @abstractmethod
    def perimeter(self) -> float: pass

    def describe(self):
        return f"{type(self).__name__}: area={self.area():.2f}, perimeter={self.perimeter():.2f}"


class Circle(Shape):
    def __init__(self, r):     self.r = r
    def area(self):            return math.pi * self.r ** 2
    def perimeter(self):       return 2 * math.pi * self.r


class Rectangle(Shape):
    def __init__(self, w, h):  self.w = w; self.h = h
    def area(self):            return self.w * self.h
    def perimeter(self):       return 2 * (self.w + self.h)


class Triangle(Shape):
    def __init__(self, a, b, c):
        self.a, self.b, self.c = a, b, c
    def area(self):
        s = (self.a + self.b + self.c) / 2
        return math.sqrt(s * (s-self.a) * (s-self.b) * (s-self.c))
    def perimeter(self):
        return self.a + self.b + self.c


shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 4, 5)]
for s in shapes:
    print(s.describe())

# Sorted by area — polymorphic comparison
shapes_sorted = sorted(shapes, key=lambda s: s.area())
print("Sorted by area:", [type(s).__name__ for s in shapes_sorted])

# Duck typing — no ABC needed
class Star:
    def area(self):       return 42.0   # not a real Shape subclass!
    def perimeter(self):  return 30.0

def total_area(shapes):
    return sum(s.area() for s in shapes)     # works with ANY object that has .area()

print(f"Total area: {total_area([Circle(5), Rectangle(4,6), Star()]):.2f}")


# ══════════════════════════════════════════════════════════════════════
# SECTION 9: MAGIC / DUNDER METHODS
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 9: DUNDER METHODS")
print("═"*60)

class Vector:
    def __init__(self, *components):
        self.components = list(components)

    def __repr__(self):
        return f"Vector{tuple(self.components)}"

    def __str__(self):
        return f"({', '.join(str(c) for c in self.components)})"

    def __len__(self):                return len(self.components)
    def __getitem__(self, i):         return self.components[i]
    def __setitem__(self, i, val):    self.components[i] = val
    def __iter__(self):               return iter(self.components)
    def __contains__(self, val):      return val in self.components
    def __bool__(self):               return any(self.components)
    def __neg__(self):                return Vector(*[-c for c in self.components])
    def __abs__(self):                return math.sqrt(sum(c**2 for c in self.components))

    def __add__(self, other):
        if len(self) != len(other):
            raise ValueError("Dimension mismatch")
        return Vector(*[a + b for a, b in zip(self, other)])

    def __sub__(self, other):
        return Vector(*[a - b for a, b in zip(self, other)])

    def __mul__(self, scalar):        return Vector(*[c * scalar for c in self])
    def __rmul__(self, scalar):       return self.__mul__(scalar)
    def __truediv__(self, scalar):    return Vector(*[c / scalar for c in self])

    def __eq__(self, other):          return self.components == other.components
    def __lt__(self, other):          return abs(self) < abs(other)

    def dot(self, other):
        return sum(a * b for a, b in zip(self, other))

v1 = Vector(1, 2, 3)
v2 = Vector(4, 5, 6)

print(v1 + v2)       # (5, 7, 9)
print(v1 - v2)       # (-3, -3, -3)
print(v1 * 3)        # (3, 6, 9)
print(3 * v1)        # (3, 6, 9)
print(abs(v1))       # 3.741...
print(v1.dot(v2))    # 32
print(v1 < v2)       # True  (|v1| < |v2|)
print(3 in v1)       # True
print(len(v1))       # 3
for c in v1: print(c, end=" ")  # 1 2 3
print()


# ══════════════════════════════════════════════════════════════════════
# SECTION 10: DATACLASSES
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 10: DATACLASSES")
print("═"*60)

@dataclass
class Product:
    name:     str
    price:    float
    category: str       = "General"
    tags:     List[str] = field(default_factory=list)

    def discount(self, pct):
        return self.price * (1 - pct / 100)

    def label(self):
        return "Expensive" if self.price > 10000 else "Affordable"


@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float

    @property
    def magnitude(self):
        return math.sqrt(self.x**2 + self.y**2)


@dataclass
class Order:
    customer: str
    items: List[Product] = field(default_factory=list)
    total: float         = field(init=False)

    def __post_init__(self):
        self.total = sum(p.price for p in self.items)

    def add_item(self, product):
        self.items.append(product)
        self.total += product.price
        return self


p1 = Product("Laptop", 60000, "Electronics", ["portable"])
p2 = Product("Mouse", 500)
print(p1)
print(p1.label())         # Expensive
print(p1.discount(10))    # 54000.0
print(asdict(p2))         # {'name': 'Mouse', 'price': 500, ...}

pts = [Point(3, 4), Point(1, 1), Point(0, 5)]
print(sorted(pts))        # sorted by (x, y) due to order=True

order = Order("Shiv", [p1, p2])
print(f"Order total: ₹{order.total}")   # ₹60500


# ══════════════════════════════════════════════════════════════════════
# SECTION 11: METACLASSES
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 11: METACLASSES")
print("═"*60)

class SingletonMeta(type):
    _instances: dict = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class AppConfig(metaclass=SingletonMeta):
    def __init__(self):
        self.debug   = False
        self.db_url  = "postgres://localhost/mydb"
        self.version = "1.0.0"

c1 = AppConfig()
c2 = AppConfig()
c1.debug = True
print(c2.debug)    # True — same object!
print(c1 is c2)    # True

# Registry metaclass — auto-register subclasses
class PluginMeta(type):
    registry: dict = {}
    def __init__(cls, name, bases, namespace):
        super().__init__(name, bases, namespace)
        if bases:    # skip the base class itself
            PluginMeta.registry[name] = cls

class Plugin(metaclass=PluginMeta): pass

class AudioPlugin(Plugin):
    def run(self): print("Playing audio")

class VideoPlugin(Plugin):
    def run(self): print("Playing video")

print("Registered plugins:", list(PluginMeta.registry.keys()))
# ['AudioPlugin', 'VideoPlugin']
for name, cls in PluginMeta.registry.items():
    cls().run()


# ══════════════════════════════════════════════════════════════════════
# SECTION 12: DESIGN PATTERNS
# ══════════════════════════════════════════════════════════════════════
print("\n" + "═"*60)
print("SECTION 12: DESIGN PATTERNS")
print("═"*60)

# ── Observer (Event Emitter) ───────────────────────────────────────
class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, List[Callable]] = {}

    def on(self, event, cb):
        self._listeners.setdefault(event, []).append(cb)
        return self

    def off(self, event, cb):
        if event in self._listeners:
            self._listeners[event].discard(cb)

    def emit(self, event, *args, **kwargs):
        for cb in self._listeners.get(event, []):
            cb(*args, **kwargs)


class ShoppingCart(EventEmitter):
    def __init__(self):
        super().__init__()
        self.items = []
        self.total = 0.0

    def add(self, name, price):
        self.items.append({"name": name, "price": price})
        self.total += price
        self.emit("item_added", name, price)
        self.emit("total_changed", self.total)
        return self


cart = ShoppingCart()
cart.on("item_added",    lambda name, p: print(f"  + {name}  ₹{p}"))
cart.on("total_changed", lambda t: print(f"  Total: ₹{t}"))
cart.add("Laptop", 60000).add("Mouse", 500)


# ── Factory ────────────────────────────────────────────────────────
class Notification(ABC):
    @abstractmethod
    def send(self, msg): pass

class EmailNotif(Notification):
    def __init__(self, email): self.email = email
    def send(self, msg): print(f"  Email → {self.email}: {msg}")

class SMSNotif(Notification):
    def __init__(self, phone): self.phone = phone
    def send(self, msg): print(f"  SMS  → {self.phone}: {msg}")

class NotifFactory:
    _map = {"email": EmailNotif, "sms": SMSNotif}

    @classmethod
    def create(cls, type_, *args) -> Notification:
        klass = cls._map.get(type_)
        if not klass: raise ValueError(f"Unknown: {type_}")
        return klass(*args)

print()
NotifFactory.create("email", "shiv@a.com").send("Welcome!")
NotifFactory.create("sms",   "+91-9876543210").send("OTP: 1234")


# ── Decorator Pattern (not @decorator) ────────────────────────────
class Coffee:
    def cost(self):        return 50
    def description(self): return "Coffee"

class Milk(Coffee):
    def __init__(self, base): self._base = base
    def cost(self):        return self._base.cost() + 20
    def description(self): return self._base.description() + ", Milk"

class Sugar(Coffee):
    def __init__(self, base): self._base = base
    def cost(self):        return self._base.cost() + 10
    def description(self): return self._base.description() + ", Sugar"

class Whip(Coffee):
    def __init__(self, base): self._base = base
    def cost(self):        return self._base.cost() + 30
    def description(self): return self._base.description() + ", Whip"

my_coffee = Whip(Sugar(Milk(Coffee())))
print(f"\n{my_coffee.description()}  →  ₹{my_coffee.cost()}")
# Coffee, Milk, Sugar, Whip  →  ₹110


# ── Context Manager Protocol ───────────────────────────────────────
class DatabaseConnection:
    def __init__(self, url):
        self.url = url
        self.connected = False

    def __enter__(self):
        print(f"  Connecting to {self.url}...")
        self.connected = True
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("  Closing connection.")
        self.connected = False
        return False    # don't suppress exceptions

    def query(self, sql):
        if not self.connected:
            raise RuntimeError("Not connected!")
        return f"Results for: {sql}"

print()
with DatabaseConnection("postgres://localhost") as db:
    print(db.query("SELECT * FROM users"))


# ── Descriptor Protocol ────────────────────────────────────────────
class Typed:
    def __init__(self, expected_type):
        self.expected_type = expected_type
        self.name = None

    def __set_name__(self, owner, name):
        self.name = name

    def __get__(self, obj, objtype=None):
        if obj is None: return self
        return obj.__dict__.get(self.name)

    def __set__(self, obj, value):
        if not isinstance(value, self.expected_type):
            raise TypeError(
                f"{self.name} must be {self.expected_type.__name__}, "
                f"got {type(value).__name__}"
            )
        obj.__dict__[self.name] = value

class Person:
    name  = Typed(str)
    age   = Typed(int)
    email = Typed(str)

    def __init__(self, name, age, email):
        self.name  = name
        self.age   = age
        self.email = email

    def __repr__(self):
        return f"Person({self.name!r}, {self.age}, {self.email!r})"

p = Person("Shiv", 25, "shiv@aquera.com")
print(f"\n{p}")

try:
    p.age = "old"   # TypeError: age must be int, got str
except TypeError as e:
    print(f"Error: {e}")


print("\n" + "═"*60)
print("All Python OOP examples complete!")
print("═"*60)
