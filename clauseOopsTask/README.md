# 🏗️ Complete OOP Guide — Python & JavaScript
### Beginner → Advanced | Real-Life Examples | Deep Internals | Visual Dry-Runs

---

## 📚 Table of Contents

1. [What is OOP? (The Big Picture)](#1-what-is-oop)
2. [Python Advanced Syntax First](#2-python-advanced-syntax-first)
   - Lambda, Comprehensions, Ternary, Generator Expressions
3. [JavaScript Advanced Syntax First](#3-javascript-advanced-syntax-first)
   - Arrow Functions, Spread, Destructuring, Optional Chaining
4. [Classes & Objects](#4-classes--objects)
5. [Constructor — `__init__` vs `constructor`](#5-constructor)
6. [Instance vs Class vs Static Variables](#6-instance-vs-class-vs-static-variables)
7. [Methods — Instance, Class, Static](#7-methods)
8. [Properties — Getters & Setters](#8-properties--getters--setters)
9. [Encapsulation — Hiding Data](#9-encapsulation)
10. [Inheritance — Reusing Code](#10-inheritance)
11. [Multiple Inheritance & MRO (Python)](#11-multiple-inheritance--mro)
12. [Mixins in JavaScript](#12-mixins-in-javascript)
13. [Polymorphism — Same Name, Different Behavior](#13-polymorphism)
14. [Abstraction — Hiding Complexity](#14-abstraction)
15. [Magic / Dunder Methods (Python)](#15-magic--dunder-methods)
16. [Symbols & WeakMap (JS Private-like)](#16-symbols--weakmap)
17. [Dataclasses (Python)](#17-dataclasses)
18. [Proxy & Reflect (JS Advanced)](#18-proxy--reflect)
19. [Metaclasses (Python — Expert Level)](#19-metaclasses)
20. [Design Patterns (Real World)](#20-design-patterns)

---

## 1. What is OOP?

> **One-line**: OOP is a way to organise code as *things* (objects) that have *data* (properties) and *behaviour* (methods).

### Real-Life Analogy 🏠

Think of a **House Blueprint** and **Real Houses**:

```
BLUEPRINT (Class)           REAL HOUSE (Object / Instance)
─────────────────           ──────────────────────────────
bedrooms: int       ──▶     bedrooms = 3
color: str          ──▶     color = "white"
open_door()         ──▶     house1.open_door()  →  "Door opens"
```

A **class** is the blueprint. An **object** is the actual house built from it.

### The 4 Pillars of OOP

```
┌─────────────────────────────────────────────────────┐
│                   4 PILLARS OF OOP                  │
├──────────────┬──────────────┬──────────┬────────────┤
│ ENCAPSULATION│  INHERITANCE │POLYMORPHISM│ABSTRACTION│
│              │              │          │            │
│ Hide data    │ Child reuses │Same name,│ Show only  │
│ inside class │ parent code  │diff behav│ what needed│
│              │              │          │            │
│ 🔒 Bank safe │ 🧬 DNA genes │🔌 Plug   │ 📱 Phone UI│
└──────────────┴──────────────┴──────────┴────────────┘
```

---

## 2. Python Advanced Syntax First

> Before we code OOP, learn these Python power tools. We'll USE them throughout the guide.

### 2.1 Lambda Functions — One-Line Functions

```python
# Normal function
def square(x):
    return x * x

# Lambda — same thing, one line
square = lambda x: x * x

print(square(5))   # 25

# With two arguments
add = lambda a, b: a + b
print(add(3, 4))   # 7

# Real use: sorting a list of dicts by price
products = [
    {"name": "Mouse",   "price": 500},
    {"name": "Laptop",  "price": 60000},
    {"name": "Keyboard","price": 2000},
]
# Sort by price using lambda
sorted_products = sorted(products, key=lambda p: p["price"])
print(sorted_products)
# [Mouse 500, Keyboard 2000, Laptop 60000]
```

**Dry Run of `sorted(products, key=lambda p: p["price"])`:**
```
Step 1: Python calls lambda on each item
  lambda {"name":"Mouse","price":500}   → 500
  lambda {"name":"Laptop","price":60000}→ 60000
  lambda {"name":"Keyboard","price":2000}→2000

Step 2: Sort by those keys: [500, 2000, 60000]
Step 3: Return items in that order ✅
```

---

### 2.2 List Comprehensions — One-Line Loops

```python
# Normal loop
squares = []
for x in range(1, 6):
    squares.append(x * x)

# List comprehension — same thing
squares = [x * x for x in range(1, 6)]
print(squares)  # [1, 4, 9, 16, 25]

# With condition (filter)
even_squares = [x * x for x in range(1, 11) if x % 2 == 0]
print(even_squares)  # [4, 16, 36, 64, 100]

# Nested comprehension — 2D grid
matrix = [[row * col for col in range(1, 4)] for row in range(1, 4)]
# [[1,2,3], [2,4,6], [3,6,9]]

# Dict comprehension
name_lengths = {name: len(name) for name in ["Alice", "Bob", "Charlie"]}
# {"Alice": 5, "Bob": 3, "Charlie": 7}

# Set comprehension (no duplicates)
unique_lengths = {len(name) for name in ["Alice", "Bob", "Charlie", "Ann"]}
# {3, 5, 7}  ← Ann and Bob both 3, only one 3
```

**Visual — How comprehension works internally:**
```
[x * x  for  x  in  range(1,6)  if  x % 2 == 0]
 ──┬──        ┬       ─────┬───      ────┬───────
   │          │            │             │
   │     variable      iterable      condition
   │          │            │             │
   ▼          ▼            ▼             ▼
 result    x=1,2,3,4,5  [1,2,3,4,5]  keep if even
           ↓
        x=2 → 4  ✅
        x=4 → 16 ✅
        x=1,3,5 → skip ❌
```

---

### 2.3 Ternary Operator — One-Line If/Else

```python
# Normal if-else
age = 20
if age >= 18:
    status = "Adult"
else:
    status = "Minor"

# Ternary — one line
status = "Adult" if age >= 18 else "Minor"
print(status)  # Adult

# Nested ternary (use carefully!)
score = 75
grade = "A" if score >= 90 else "B" if score >= 75 else "C" if score >= 60 else "F"
print(grade)  # B

# Real use in class
class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def label(self):
        return "Expensive" if self.price > 10000 else "Affordable"
```

---

### 2.4 Generator Expressions — Lazy Evaluation

```python
# List comprehension — creates ALL items in memory at once
squares_list = [x * x for x in range(1_000_000)]  # 8 MB in memory 😱

# Generator expression — creates ONE item at a time (lazy)
squares_gen = (x * x for x in range(1_000_000))   # ~100 bytes in memory 😊

# Use next() to get one at a time
gen = (x * x for x in range(5))
print(next(gen))  # 0
print(next(gen))  # 1
print(next(gen))  # 4

# Or iterate with for
for val in (x * x for x in range(5)):
    print(val)

# sum() works directly on generators — no list needed
total = sum(x * x for x in range(1_000_001))
print(total)
```

**Visual — Generator vs List:**
```
LIST COMPREHENSION [x*x for x in range(5)]:
Memory: [0, 1, 4, 9, 16]  ← All stored immediately

GENERATOR (x*x for x in range(5)):
Memory: (state: x=0)  ← Just knows WHERE it is

next() →  compute 0*0=0, advance to x=1
next() →  compute 1*1=1, advance to x=2
next() →  compute 2*2=4, advance to x=3
... computes only when asked! 🔋
```

---

### 2.5 Walrus Operator `:=` (Python 3.8+)

```python
# Assign AND use in one expression
import re

data = ["hello123", "world", "python456"]

# Without walrus
results = []
for item in data:
    match = re.search(r'\d+', item)
    if match:
        results.append(match.group())

# With walrus (:=) — assign inside if
results = [m.group() for item in data if (m := re.search(r'\d+', item))]
print(results)  # ['123', '456']
```

---

## 3. JavaScript Advanced Syntax First

### 3.1 Arrow Functions

```javascript
// Normal function
function square(x) {
    return x * x;
}

// Arrow function — same thing
const square = (x) => x * x;

// If one parameter, parens optional
const square = x => x * x;

// If body has multiple lines, use {} and return
const greet = (name) => {
    const message = `Hello, ${name}!`;
    return message;
};

// ⚠️ KEY DIFFERENCE: Arrow functions don't have their own `this`
// They inherit `this` from surrounding scope (lexical this)
class Timer {
    constructor() {
        this.seconds = 0;
    }
    
    start() {
        // ✅ Arrow function — `this` refers to Timer instance
        setInterval(() => {
            this.seconds++;  // works!
        }, 1000);
        
        // ❌ Regular function — `this` is undefined (strict mode)
        setInterval(function() {
            this.seconds++;  // this is undefined or global!
        }, 1000);
    }
}
```

---

### 3.2 Spread Operator `...`

```javascript
// 1. Spread array into another array
const nums1 = [1, 2, 3];
const nums2 = [4, 5, 6];
const combined = [...nums1, ...nums2];  // [1,2,3,4,5,6]

// 2. Spread to copy object (shallow)
const original = { name: "Shiv", age: 25 };
const copy = { ...original, city: "Delhi" };
// { name:"Shiv", age:25, city:"Delhi" }

// 3. Spread in function call
const numbers = [10, 20, 30];
Math.max(...numbers);  // same as Math.max(10, 20, 30) → 30

// 4. Rest parameters (opposite of spread — collects into array)
const sum = (...nums) => nums.reduce((total, n) => total + n, 0);
sum(1, 2, 3, 4, 5);  // 15

// Real OOP use — merging config in constructor
class Config {
    constructor(options = {}) {
        this.settings = {
            theme: "light",
            language: "en",
            ...options          // override defaults with user options
        };
    }
}
const c = new Config({ theme: "dark" });
console.log(c.settings);  // { theme: "dark", language: "en" }
```

---

### 3.3 Destructuring

```javascript
// Array destructuring
const [first, second, ...rest] = [10, 20, 30, 40, 50];
// first=10, second=20, rest=[30,40,50]

// Object destructuring
const { name, age, city = "Unknown" } = { name: "Shiv", age: 25 };
// name="Shiv", age=25, city="Unknown" (default)

// Rename while destructuring
const { name: userName } = { name: "Shiv" };
// userName = "Shiv"

// In class methods
class User {
    constructor({ name, email, role = "user" }) {
        this.name = name;
        this.email = email;
        this.role = role;
    }
    
    getInfo() {
        const { name, email } = this;  // destructure from this
        return `${name} <${email}>`;
    }
}
const u = new User({ name: "Shiv", email: "s@a.com" });
```

---

### 3.4 Optional Chaining `?.` & Nullish Coalescing `??`

```javascript
// Optional chaining — safe access without crashing
const user = {
    profile: {
        address: {
            city: "Delhi"
        }
    }
};

// Without optional chaining (danger!)
user.profile.address.city          // "Delhi" ✅
user.settings.theme                // TypeError: Cannot read properties of undefined 💥

// With optional chaining (safe)
user?.settings?.theme              // undefined (no crash) ✅
user?.profile?.address?.city       // "Delhi" ✅

// Works with methods too
user?.getName?.()                  // won't crash if getName doesn't exist

// Nullish coalescing — default for null/undefined only
const theme = user?.settings?.theme ?? "light";  // "light"
// (NOT like || which also catches 0 and "")
const count = 0 ?? 10;   // 0   (0 is not null/undefined)
const count2 = 0 || 10;  // 10  (|| treats 0 as falsy)
```

---

### 3.5 Template Literals & Tagged Templates

```javascript
const name = "Shiv";
const price = 60000;

// Template literal
const msg = `Product for ${name} costs ₹${price.toLocaleString("en-IN")}`;
// "Product for Shiv costs ₹60,000"

// Multi-line
const html = `
  <div class="product">
    <h2>${name}</h2>
    <p>Price: ₹${price}</p>
  </div>
`;
```

---

## 4. Classes & Objects

### Python

```python
# Define a class
class Dog:
    # Class body
    species = "Canis lupus familiaris"  # class variable (shared)
    
    def __init__(self, name, breed, age):  # constructor
        self.name = name    # instance variable (unique per dog)
        self.breed = breed
        self.age = age
    
    def bark(self):
        return f"{self.name} says: Woof!"
    
    def info(self):
        return f"{self.name} ({self.breed}), {self.age} years old"

# Create objects (instances)
dog1 = Dog("Bruno", "German Shepherd", 3)
dog2 = Dog("Bella", "Labrador", 2)

print(dog1.bark())    # Bruno says: Woof!
print(dog2.info())    # Bella (Labrador), 2 years old
print(Dog.species)    # Canis lupus familiaris (from class)
```

**Memory Visual — What happens when you create `dog1 = Dog("Bruno", ...)`:**
```
RAM Memory
──────────────────────────────────────────────
Dog CLASS object (in memory once):
┌─────────────────────────────┐
│ Dog                         │
│  species = "Canis lupus..." │
│  __init__ = <function>      │
│  bark = <function>          │
│  info = <function>          │
└─────────────────────────────┘
           │ dog1 = Dog("Bruno", ...)
           ▼
┌─────────────────────────────┐
│ dog1 instance               │
│  __class__ → Dog            │ ← points back to class
│  name = "Bruno"             │
│  breed = "German Shepherd"  │
│  age = 3                    │
└─────────────────────────────┘
           │ dog2 = Dog("Bella", ...)
           ▼
┌─────────────────────────────┐
│ dog2 instance               │
│  __class__ → Dog            │
│  name = "Bella"             │
│  breed = "Labrador"         │
│  age = 2                    │
└─────────────────────────────┘
```

### JavaScript

```javascript
class Dog {
    static species = "Canis lupus familiaris";  // class variable
    
    constructor(name, breed, age) {
        this.name = name;    // instance variable
        this.breed = breed;
        this.age = age;
    }
    
    bark() {
        return `${this.name} says: Woof!`;
    }
    
    info() {
        return `${this.name} (${this.breed}), ${this.age} years old`;
    }
    
    // Arrow method (keeps `this` binding safe)
    greet = () => `Hi, I'm ${this.name}!`;
}

const dog1 = new Dog("Bruno", "German Shepherd", 3);
const dog2 = new Dog("Bella", "Labrador", 2);

console.log(dog1.bark());    // Bruno says: Woof!
console.log(Dog.species);    // Canis lupus familiaris
```

**Internally — How JavaScript classes work:**
```
JavaScript class syntax is "syntactic sugar" over prototypes.

class Dog { bark() {...} }

IS EQUIVALENT TO:

function Dog(name, breed, age) {
    this.name = name;
    this.breed = breed;
    this.age = age;
}
Dog.prototype.bark = function() { return `${this.name} says Woof!`; };

Prototype chain for dog1:
dog1 ──→ Dog.prototype ──→ Object.prototype ──→ null
          (bark, info)      (toString, etc.)

When you call dog1.bark():
1. JS looks for bark on dog1 directly → not found
2. Looks on Dog.prototype → FOUND! ✅ Calls it with this = dog1
```

---

## 5. Constructor

> The constructor runs automatically when you create an object. It "sets up" the object.

### Python `__init__`

```python
class BankAccount:
    def __init__(self, owner, initial_balance=0):
        self.owner = owner
        self.balance = initial_balance
        self.transactions = []          # fresh list per account!
    
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"+{amount}")
    
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.balance -= amount
        self.transactions.append(f"-{amount}")
    
    def statement(self):
        return f"{self.owner}: ₹{self.balance} | {self.transactions}"

acc1 = BankAccount("Shiv", 10000)
acc2 = BankAccount("Raj")        # default balance = 0

acc1.deposit(5000)
acc1.withdraw(2000)
print(acc1.statement())  # Shiv: ₹13000 | [+5000, -2000]
```

### ⚠️ Classic Python Bug — Mutable Default Argument

```python
# WRONG! — list is shared across all instances
class BadAccount:
    def __init__(self, owner, transactions=[]):  # ← DANGER!
        self.transactions = transactions  # same list for ALL objects!

a = BadAccount("Shiv")
b = BadAccount("Raj")
a.transactions.append("deposit")
print(b.transactions)  # ['deposit']  😱 Raj's account shows Shiv's deposit!

# CORRECT — create new list each time
class GoodAccount:
    def __init__(self, owner, transactions=None):
        self.transactions = transactions if transactions is not None else []
```

### JavaScript `constructor`

```javascript
class BankAccount {
    constructor(owner, initialBalance = 0) {
        this.owner = owner;
        this.balance = initialBalance;
        this.transactions = [];
    }
    
    deposit(amount) {
        this.balance += amount;
        this.transactions.push(`+${amount}`);
        return this;  // enable chaining!
    }
    
    withdraw(amount) {
        if (amount > this.balance) throw new Error("Insufficient funds");
        this.balance -= amount;
        this.transactions.push(`-${amount}`);
        return this;
    }
    
    get statement() {
        return `${this.owner}: ₹${this.balance} | [${this.transactions}]`;
    }
}

const acc = new BankAccount("Shiv", 10000);
acc.deposit(5000).withdraw(2000);  // method chaining!
console.log(acc.statement);  // Shiv: ₹13000 | [+5000, -2000]
```

---

## 6. Instance vs Class vs Static Variables

```
Variable Type    | Belongs To | Shared? | Example
─────────────────┼────────────┼─────────┼──────────────────
Instance variable| object     | No      | self.name = "Bruno"
Class variable   | class      | Yes     | Dog.count = 0
Static variable  | static     | Yes (JS)| static count = 0
```

### Python Example

```python
class Employee:
    company = "Aquera Inc"     # class variable — shared by ALL
    total_employees = 0        # class variable — track count
    
    def __init__(self, name, salary):
        self.name = name               # instance variable
        self.salary = salary           # instance variable
        Employee.total_employees += 1  # modify class variable
    
    @classmethod
    def get_company_info(cls):
        return f"{cls.company} — {cls.total_employees} employees"
    
    @staticmethod
    def is_valid_salary(amount):
        return isinstance(amount, (int, float)) and amount > 0

e1 = Employee("Shiv", 80000)
e2 = Employee("Raj", 90000)
e3 = Employee("Priya", 75000)

print(Employee.total_employees)       # 3
print(Employee.get_company_info())    # Aquera Inc — 3 employees
print(Employee.is_valid_salary(-100)) # False

# Change class variable for one instance — creates SHADOW copy
e1.company = "Freelancer"   # creates instance variable, hides class var
print(e1.company)            # Freelancer (instance shadow)
print(e2.company)            # Aquera Inc (class variable unchanged)
print(Employee.company)      # Aquera Inc (class unchanged)
```

**Visual — Class vs Instance Variable lookup:**
```
e1.company → lookup:
  1. Check e1.__dict__ → {"company": "Freelancer", "name":...} → FOUND ✅

e2.company → lookup:
  1. Check e2.__dict__ → {"name": "Raj", "salary": 90000} → NOT found
  2. Check Employee.__dict__ → {"company": "Aquera Inc"} → FOUND ✅
```

### JavaScript Example

```javascript
class Employee {
    static company = "Aquera Inc";    // class-level (static)
    static #totalEmployees = 0;       // private static
    
    constructor(name, salary) {
        this.name = name;             // instance variable
        this.salary = salary;
        Employee.#totalEmployees++;
    }
    
    static getCompanyInfo() {
        return `${Employee.company} — ${Employee.#totalEmployees} employees`;
    }
    
    static isValidSalary(amount) {
        return typeof amount === "number" && amount > 0;
    }
    
    // Instance method
    getDetails = () => `${this.name}: ₹${this.salary}`;
}

const e1 = new Employee("Shiv", 80000);
const e2 = new Employee("Raj", 90000);

console.log(Employee.getCompanyInfo());   // Aquera Inc — 2 employees
console.log(Employee.isValidSalary(-5)); // false
console.log(e1.getDetails());            // Shiv: ₹80000
```

---

## 7. Methods

### Python — Three Types

```python
class Temperature:
    # ──────────────────────────────────────────────────
    # 1. INSTANCE METHOD — receives `self` (the object)
    # ──────────────────────────────────────────────────
    def __init__(self, celsius):
        self.celsius = celsius
    
    def to_fahrenheit(self):              # instance method
        return self.celsius * 9/5 + 32
    
    # ──────────────────────────────────────────────────
    # 2. CLASS METHOD — receives `cls` (the class itself)
    #    Used as alternative constructors
    # ──────────────────────────────────────────────────
    @classmethod
    def from_fahrenheit(cls, fahrenheit): # class method
        celsius = (fahrenheit - 32) * 5/9
        return cls(celsius)
    
    @classmethod
    def from_kelvin(cls, kelvin):
        return cls(kelvin - 273.15)
    
    # ──────────────────────────────────────────────────
    # 3. STATIC METHOD — receives neither self nor cls
    #    Pure utility function, logically belongs here
    # ──────────────────────────────────────────────────
    @staticmethod
    def is_below_freezing(celsius):       # static method
        return celsius < 0
    
    def __repr__(self):
        return f"Temperature({self.celsius:.2f}°C)"

# Instance method — called on object
t1 = Temperature(100)
print(t1.to_fahrenheit())        # 212.0

# Class method — called on class (alternative constructors!)
t2 = Temperature.from_fahrenheit(212)
print(t2)                        # Temperature(100.00°C)

t3 = Temperature.from_kelvin(373.15)
print(t3)                        # Temperature(100.00°C)

# Static method — called on class
print(Temperature.is_below_freezing(-5))  # True
print(Temperature.is_below_freezing(25))  # False
```

**Visual — Method types:**
```
                    ┌──────────────┐
                    │  Temperature │
                    │   CLASS      │
                    └──────┬───────┘
                           │
        ┌──────────────────┼──────────────────┐
        │                  │                  │
   @classmethod      instance method     @staticmethod
   from_fahrenheit() to_fahrenheit()    is_below_freezing()
        │                  │                  │
   receives cls       receives self      receives nothing
   (the class)        (the object)       (pure function)
        │                  │
        ▼                  ▼
  Temperature(...)    self.celsius
  creates new obj      uses instance data
```

### JavaScript — Same Concept

```javascript
class Temperature {
    constructor(celsius) {
        this.celsius = celsius;
    }
    
    // Instance method
    toFahrenheit() {
        return this.celsius * 9/5 + 32;
    }
    
    // Static method (plays role of both classmethod and staticmethod)
    static fromFahrenheit(fahrenheit) {
        return new Temperature((fahrenheit - 32) * 5/9);
    }
    
    static fromKelvin(kelvin) {
        return new Temperature(kelvin - 273.15);
    }
    
    static isBelowFreezing(celsius) {
        return celsius < 0;
    }
    
    toString() {
        return `Temperature(${this.celsius.toFixed(2)}°C)`;
    }
}

const t1 = new Temperature(100);
console.log(t1.toFahrenheit());              // 212
console.log(Temperature.fromFahrenheit(212).toString());  // Temperature(100.00°C)
console.log(Temperature.isBelowFreezing(-5)); // true
```

---

## 8. Properties — Getters & Setters

> Properties let you control what happens when someone reads or writes a value. Looks like a variable, acts like a function.

### Python `@property`

```python
class Circle:
    def __init__(self, radius):
        self._radius = radius    # _radius = "private by convention"
    
    # GETTER — access like attribute, not function call
    @property
    def radius(self):
        return self._radius
    
    # SETTER — validate before setting
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError(f"Radius cannot be negative, got {value}")
        self._radius = value
    
    # Computed property (no setter — read only)
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2
    
    @property
    def circumference(self):
        import math
        return 2 * math.pi * self._radius
    
    # DELETER
    @radius.deleter
    def radius(self):
        print("Deleting radius!")
        del self._radius

c = Circle(5)
print(c.radius)        # 5     (getter called)
print(c.area)          # 78.54 (computed, no setter)
c.radius = 10          # (setter called, validates)
print(c.radius)        # 10
c.radius = -3          # ValueError: Radius cannot be negative!
```

**Dry Run — `c.radius = 10`:**
```
c.radius = 10
  ↓
Python sees: "radius" has a setter defined?  → YES
  ↓
Calls: radius.setter(c, 10)
  ↓
  value = 10
  if 10 < 0: → False, skip error
  self._radius = 10  ← stored here!
  ↓
Done ✅

c.radius  (read)
  ↓
Python sees: "radius" has a getter defined?  → YES
  ↓
Calls: radius.getter(c)
  return self._radius  → returns 10
```

### JavaScript Getters & Setters

```javascript
class Circle {
    #radius;  // private field
    
    constructor(radius) {
        this.radius = radius;  // uses setter!
    }
    
    get radius() {
        return this.#radius;
    }
    
    set radius(value) {
        if (value < 0) throw new Error(`Radius cannot be negative: ${value}`);
        this.#radius = value;
    }
    
    get area() {
        return Math.PI * this.#radius ** 2;
    }
    
    get circumference() {
        return 2 * Math.PI * this.#radius;
    }
}

const c = new Circle(5);
console.log(c.radius);       // 5
console.log(c.area);         // 78.54
c.radius = 10;               // setter called
console.log(c.radius);       // 10
// c.area = 100;             // TypeError: no setter (read-only)
```

---

## 9. Encapsulation

> **Real life**: An ATM machine — you can press buttons (public interface) but cannot touch the internal cash mechanism (private).

### Levels of Access

```
Access Level    | Python        | JavaScript
────────────────┼───────────────┼─────────────────
Public          | name          | name
Protected(conv) | _name         | (no built-in)
Private         | __name        | #name
```

### Python Encapsulation

```python
class ATM:
    def __init__(self, balance):
        self.__balance = balance    # PRIVATE — name-mangled to _ATM__balance
        self._pin = "1234"          # PROTECTED — convention only
        self.bank_name = "HDFC"    # PUBLIC
    
    # Public interface
    def withdraw(self, amount, pin):
        if not self.__verify_pin(pin):    # call private method
            raise PermissionError("Wrong PIN!")
        if not self.__has_funds(amount):  # call private method
            raise ValueError("Insufficient funds!")
        self.__balance -= amount
        return f"Withdrawn ₹{amount}. Balance: ₹{self.__balance}"
    
    def check_balance(self, pin):
        if not self.__verify_pin(pin):
            raise PermissionError("Wrong PIN!")
        return self.__balance
    
    # Private methods — internal implementation
    def __verify_pin(self, pin):
        return pin == self._pin
    
    def __has_funds(self, amount):
        return amount <= self.__balance

atm = ATM(50000)
print(atm.withdraw(10000, "1234"))  # Works!
# print(atm.__balance)              # AttributeError: no attribute '__balance'
print(atm._ATM__balance)            # 40000 — still accessible (name mangling, not truly private)

# Advanced: using slots for memory efficiency
class Point:
    __slots__ = ('x', 'y')  # restrict attributes, save memory
    
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # point.z = 5  ← AttributeError! Only x, y allowed
```

### JavaScript Private Fields (`#`)

```javascript
class ATM {
    #balance;         // truly private — cannot be accessed outside
    #pin;
    bankName;         // public
    
    constructor(balance, pin) {
        this.#balance = balance;
        this.#pin = pin;
        this.bankName = "HDFC";
    }
    
    withdraw(amount, pin) {
        if (!this.#verifyPin(pin)) throw new Error("Wrong PIN!");
        if (amount > this.#balance) throw new Error("Insufficient funds!");
        this.#balance -= amount;
        return `Withdrawn ₹${amount}. Balance: ₹${this.#balance}`;
    }
    
    checkBalance(pin) {
        if (!this.#verifyPin(pin)) throw new Error("Wrong PIN!");
        return this.#balance;
    }
    
    #verifyPin(pin) {        // private method
        return pin === this.#pin;
    }
}

const atm = new ATM(50000, "1234");
console.log(atm.withdraw(10000, "1234"));  // Works!
// console.log(atm.#balance);              // SyntaxError — truly private
// console.log(atm["#balance"]);           // undefined (not accessible!)
```

---

## 10. Inheritance

> **Real life**: A child inherits traits from parents but also has their own unique traits.

### Python Single Inheritance

```python
# PARENT (Base) class
class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def breathe(self):
        return f"{self.name} breathes"
    
    def eat(self):
        return f"{self.name} eats"
    
    def __str__(self):
        return f"{self.__class__.__name__}({self.name}, {self.age})"

# CHILD (Derived) class
class Dog(Animal):              # Dog INHERITS from Animal
    def __init__(self, name, age, breed):
        super().__init__(name, age)   # call parent constructor!
        self.breed = breed
    
    def bark(self):             # NEW method, unique to Dog
        return f"{self.name} says: Woof!"
    
    def eat(self):              # OVERRIDE parent method
        return f"{self.name} eats dog food"

class Cat(Animal):
    def __init__(self, name, age, indoor):
        super().__init__(name, age)
        self.indoor = indoor
    
    def purr(self):
        return f"{self.name} purrs..."
    
    def eat(self):              # OVERRIDE
        return f"{self.name} eats cat food"

dog = Dog("Bruno", 3, "Labrador")
cat = Cat("Whiskers", 5, True)

print(dog.breathe())     # Bruno breathes   (inherited from Animal)
print(dog.eat())         # Bruno eats dog food  (overridden)
print(dog.bark())        # Bruno says: Woof! (Dog-specific)
print(cat.purr())        # Whiskers purrs...
print(dog)               # Dog(Bruno, 3)    (uses Animal.__str__)
```

**Visual — Inheritance chain:**
```
Animal
│  name, age
│  breathe(), eat(), __str__()
│
├── Dog
│    breed
│    bark(), eat() [overrides Animal.eat]
│
└── Cat
     indoor
     purr(), eat() [overrides Animal.eat]

LOOKUP for dog.breathe():
  1. Check Dog class → not found
  2. Check Animal class → FOUND ✅

LOOKUP for dog.eat():
  1. Check Dog class → FOUND ✅ (overridden, stops here)
```

### JavaScript Inheritance

```javascript
class Animal {
    constructor(name, age) {
        this.name = name;
        this.age = age;
    }
    
    breathe() { return `${this.name} breathes`; }
    eat()     { return `${this.name} eats`; }
    
    toString() { return `${this.constructor.name}(${this.name}, ${this.age})`; }
}

class Dog extends Animal {
    constructor(name, age, breed) {
        super(name, age);       // MUST call super() before using `this`
        this.breed = breed;
    }
    
    bark() { return `${this.name} says: Woof!`; }
    
    eat() { return `${this.name} eats dog food`; }  // override
}

class Cat extends Animal {
    constructor(name, age, indoor) {
        super(name, age);
        this.indoor = indoor;
    }
    
    purr() { return `${this.name} purrs...`; }
    eat()  { return `${this.name} eats cat food`; }
}

const dog = new Dog("Bruno", 3, "Labrador");
console.log(dog.breathe());    // Bruno breathes (inherited)
console.log(dog.eat());        // Bruno eats dog food (overridden)
console.log(dog instanceof Dog);    // true
console.log(dog instanceof Animal); // true (prototype chain)
```

**JavaScript Prototype Chain Visualized:**
```
dog ──→ Dog.prototype ──→ Animal.prototype ──→ Object.prototype ──→ null
         bark()            breathe()            toString()
         eat()             eat()                hasOwnProperty()
         (overrides)       (original)

When dog.breathe() is called:
1. dog has own property "breathe"? → No
2. Dog.prototype has "breathe"? → No
3. Animal.prototype has "breathe"? → YES ✅
```

### Multilevel Inheritance (Python)

```python
class LivingThing:
    def breathe(self): return "Breathes oxygen"

class Animal(LivingThing):
    def __init__(self, name): self.name = name
    def eat(self): return f"{self.name} eats"

class Mammal(Animal):
    def feed_young(self): return f"{self.name} feeds young with milk"

class Dog(Mammal):
    def bark(self): return f"{self.name}: Woof!"

dog = Dog("Rex")
print(dog.breathe())      # Breathes oxygen     (from LivingThing)
print(dog.eat())          # Rex eats             (from Animal)
print(dog.feed_young())   # Rex feeds young...   (from Mammal)
print(dog.bark())         # Rex: Woof!           (from Dog)

print(Dog.__mro__)
# (<class 'Dog'>, <class 'Mammal'>, <class 'Animal'>, <class 'LivingThing'>, <class 'object'>)
```

---

## 11. Multiple Inheritance & MRO

> Python allows a class to inherit from MORE than one parent. JavaScript doesn't support this natively (use Mixins instead).

### Python Multiple Inheritance

```python
class Flyable:
    def fly(self): return "I can fly!"
    def describe(self): return "Flyable creature"

class Swimmable:
    def swim(self): return "I can swim!"
    def describe(self): return "Swimmable creature"

class Duck(Flyable, Swimmable):   # inherits from BOTH
    def quack(self): return "Quack!"
    # What does Duck.describe() return? MRO decides!

duck = Duck()
print(duck.fly())       # I can fly!
print(duck.swim())      # I can swim!
print(duck.quack())     # Quack!
print(duck.describe())  # Flyable creature  ← Flyable wins (listed first)
```

### MRO — Method Resolution Order (The C3 Algorithm)

```python
# MRO = the ORDER Python searches classes for a method
print(Duck.__mro__)
# (Duck, Flyable, Swimmable, object)
#   ↑       ↑         ↑        ↑
#   1st     2nd       3rd      4th → searched in this order

# More complex example
class A:
    def greet(self): return "Hello from A"

class B(A):
    def greet(self): return "Hello from B"

class C(A):
    def greet(self): return "Hello from C"

class D(B, C):    # Diamond inheritance!
    pass

print(D.__mro__)
# (D, B, C, A, object)
#  D → B → C → A (not D → B → A → C → A, which would visit A twice!)

d = D()
print(d.greet())  # Hello from B (B is first after D in MRO)
```

**Diamond Problem Visual:**
```
        A
       / \
      B   C
       \ /
        D

Without C3/MRO:  D → B → A (STOP), C → A  ← A called twice! ❌

With MRO (C3):   D → B → C → A             ← A called once! ✅
                 Left-to-right, depth-first, with linearization
```

### `super()` in Multiple Inheritance

```python
class Animal:
    def __init__(self, name):
        print(f"Animal.__init__({name})")
        self.name = name

class Flyable:
    def __init__(self, *args, **kwargs):
        print("Flyable.__init__")
        super().__init__(*args, **kwargs)  # passes to next in MRO!

class Swimmable:
    def __init__(self, *args, **kwargs):
        print("Swimmable.__init__")
        super().__init__(*args, **kwargs)

class Duck(Flyable, Swimmable, Animal):
    def __init__(self, name):
        print("Duck.__init__")
        super().__init__(name)  # starts MRO chain

# MRO: Duck → Flyable → Swimmable → Animal → object
d = Duck("Donald")
# Prints:
# Duck.__init__
# Flyable.__init__
# Swimmable.__init__
# Animal.__init__(Donald)
```

---

## 12. Mixins in JavaScript

> JavaScript uses Mixins (composition) instead of multiple inheritance.

```javascript
// Mixin — a plain object with methods to mix in
const Flyable = {
    fly() { return `${this.name} is flying!`; },
    land() { return `${this.name} landed.`; }
};

const Swimmable = {
    swim() { return `${this.name} is swimming!`; },
    dive() { return `${this.name} dived.`; }
};

// Mixin helper
const mix = (BaseClass, ...mixins) => {
    class Mixed extends BaseClass {}
    mixins.forEach(mixin => Object.assign(Mixed.prototype, mixin));
    return Mixed;
};

class Animal {
    constructor(name) { this.name = name; }
    breathe() { return `${this.name} breathes`; }
}

class Duck extends mix(Animal, Flyable, Swimmable) {
    quack() { return "Quack!"; }
}

const duck = new Duck("Donald");
console.log(duck.breathe());  // Donald breathes
console.log(duck.fly());      // Donald is flying!
console.log(duck.swim());     // Donald is swimming!
console.log(duck.quack());    // Quack!
```

---

## 13. Polymorphism

> **Poly = many, morph = forms** — Same method name, different behaviour per class.

### Python Polymorphism

```python
# Duck typing — "If it quacks like a duck, it's a duck"
class Circle:
    def __init__(self, radius): self.radius = radius
    def area(self):
        import math
        return math.pi * self.radius ** 2

class Rectangle:
    def __init__(self, w, h): self.width = w; self.height = h
    def area(self): return self.width * self.height

class Triangle:
    def __init__(self, base, height): self.base = base; self.height = height
    def area(self): return 0.5 * self.base * self.height

# Polymorphic function — works with ANY shape that has .area()
def print_area(shape):
    print(f"{type(shape).__name__}: area = {shape.area():.2f}")

shapes = [Circle(5), Rectangle(4, 6), Triangle(3, 8)]
for shape in shapes:
    print_area(shape)
# Circle:    area = 78.54
# Rectangle: area = 24.00
# Triangle:  area = 12.00

# Advanced — using ABC for enforced polymorphism
from abc import ABC, abstractmethod

class Shape(ABC):
    @abstractmethod
    def area(self): pass    # ALL subclasses MUST implement this
    
    @abstractmethod
    def perimeter(self): pass
    
    def describe(self):     # concrete method — shared by all
        return f"I am a {type(self).__name__} with area {self.area():.2f}"

class Square(Shape):
    def __init__(self, side): self.side = side
    def area(self): return self.side ** 2
    def perimeter(self): return 4 * self.side

# Shape()  # TypeError: Can't instantiate abstract class!
sq = Square(5)
print(sq.describe())  # I am a Square with area 25.00
```

### JavaScript Polymorphism

```javascript
class Shape {
    area() { throw new Error("area() must be implemented"); }
    
    describe() {
        return `I am a ${this.constructor.name} with area ${this.area().toFixed(2)}`;
    }
}

class Circle extends Shape {
    constructor(radius) { super(); this.radius = radius; }
    area() { return Math.PI * this.radius ** 2; }
}

class Rectangle extends Shape {
    constructor(w, h) { super(); this.width = w; this.height = h; }
    area() { return this.width * this.height; }
}

const shapes = [new Circle(5), new Rectangle(4, 6)];
shapes.forEach(s => console.log(s.describe()));
// I am a Circle with area 78.54
// I am a Rectangle with area 24.00
```

### Operator Overloading (Python)

```python
class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def __add__(self, other):      # v1 + v2
        return Vector(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):      # v1 - v2
        return Vector(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):     # v * 3
        return Vector(self.x * scalar, self.y * scalar)
    
    def __rmul__(self, scalar):    # 3 * v
        return self.__mul__(scalar)
    
    def __abs__(self):             # abs(v) = magnitude
        return (self.x**2 + self.y**2) ** 0.5
    
    def __eq__(self, other):       # v1 == v2
        return self.x == other.x and self.y == other.y
    
    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

v1 = Vector(1, 2)
v2 = Vector(3, 4)
print(v1 + v2)     # Vector(4, 6)
print(v1 * 3)      # Vector(3, 6)
print(3 * v1)      # Vector(3, 6)
print(abs(v2))     # 5.0
```

---

## 14. Abstraction

> Show only what is necessary. Hide implementation details behind a clean interface.

### Python ABC (Abstract Base Classes)

```python
from abc import ABC, abstractmethod

class PaymentGateway(ABC):   # Abstract class — blueprint only
    
    @abstractmethod
    def connect(self): pass
    
    @abstractmethod
    def charge(self, amount): pass
    
    @abstractmethod
    def refund(self, transaction_id): pass
    
    # Concrete method — shared, not overridden
    def process_payment(self, amount):
        self.connect()
        tx_id = self.charge(amount)
        return tx_id

class StripeGateway(PaymentGateway):
    def connect(self):
        print("Connecting to Stripe API...")
    
    def charge(self, amount):
        print(f"Charging ₹{amount} via Stripe")
        return "stripe_tx_001"
    
    def refund(self, tx_id):
        print(f"Refunding {tx_id} via Stripe")

class RazorpayGateway(PaymentGateway):
    def connect(self):
        print("Connecting to Razorpay API...")
    
    def charge(self, amount):
        print(f"Charging ₹{amount} via Razorpay")
        return "rp_tx_001"
    
    def refund(self, tx_id):
        print(f"Refunding {tx_id} via Razorpay")

# Usage — code doesn't care WHICH gateway, just calls .process_payment()
def checkout(gateway: PaymentGateway, amount):
    tx = gateway.process_payment(amount)
    print(f"Payment complete: {tx}")

checkout(StripeGateway(), 5000)
checkout(RazorpayGateway(), 3000)
# PaymentGateway()  ← TypeError! Cannot instantiate abstract class
```

---

## 15. Magic / Dunder Methods

> Methods with `__double_underscore__` — Python calls them automatically in certain situations.

```python
class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self._current_page = 0
    
    # ── String representations ──────────────────────
    def __str__(self):
        # Called by print() and str()
        return f'"{self.title}" by {self.author}'
    
    def __repr__(self):
        # Called by repr() and in REPL — for developers
        return f'Book(title="{self.title}", author="{self.author}", pages={self.pages})'
    
    # ── Comparison operators ────────────────────────
    def __eq__(self, other):       # ==
        return self.title == other.title and self.author == other.author
    
    def __lt__(self, other):       # <
        return self.pages < other.pages
    
    def __le__(self, other):       # <=
        return self.pages <= other.pages
    
    # ── Container methods ────────────────────────────
    def __len__(self):             # len(book)
        return self.pages
    
    def __contains__(self, word): # "word" in book
        return word.lower() in self.title.lower()
    
    # ── Math operators ───────────────────────────────
    def __add__(self, other):      # book1 + book2 → merged book
        combined_title = f"{self.title} & {other.title}"
        return Book(combined_title, "Various", self.pages + other.pages)
    
    # ── Callable ─────────────────────────────────────
    def __call__(self, page):     # book(42) → go to page 42
        if 1 <= page <= self.pages:
            self._current_page = page
            return f"Opened to page {page}"
        raise ValueError(f"Page {page} out of range")
    
    # ── Context Manager ──────────────────────────────
    def __enter__(self):          # with book as b:
        print(f"Opening: {self.title}")
        return self
    
    def __exit__(self, exc_type, exc_val, exc_tb):
        print(f"Closing: {self.title}")
        return False  # don't suppress exceptions
    
    # ── Iterator ─────────────────────────────────────
    def __iter__(self):           # for page in book:
        self._current_page = 0
        return self
    
    def __next__(self):
        self._current_page += 1
        if self._current_page > self.pages:
            raise StopIteration
        return self._current_page
    
    # ── Attribute access ─────────────────────────────
    def __getattr__(self, name):  # called when attr NOT found
        return f"'{name}' not found in Book"
    
    def __setattr__(self, name, value):  # called on EVERY attribute set
        if name == "pages" and isinstance(value, int) and value < 0:
            raise ValueError("Pages cannot be negative!")
        super().__setattr__(name, value)  # actual storage

b1 = Book("Python Crash Course", "Eric Matthes", 544)
b2 = Book("Clean Code", "Robert Martin", 431)
b3 = Book("Python Crash Course", "Eric Matthes", 544)

print(b1)            # "Python Crash Course" by Eric Matthes
print(repr(b2))      # Book(title="Clean Code", ...)
print(len(b1))       # 544
print(b1 == b3)      # True
print(b1 > b2)       # True (544 > 431)
print("Python" in b1) # True
print(b1(100))       # Opened to page 100

merged = b1 + b2
print(merged.title)  # Python Crash Course & Clean Code

with b1 as book:
    print(book.pages)  # 544
# → Closing: Python Crash Course

for i, page in enumerate(b1):
    if i > 2: break
    print(f"Page {page}")  # Page 1, Page 2, Page 3
```

**Complete Dunder Methods Reference:**

```
Category        | Dunder          | Triggered by
────────────────┼─────────────────┼──────────────────
Init/Del        | __init__        | ClassName(...)
                | __new__         | object creation (before init)
                | __del__         | garbage collection
────────────────┼─────────────────┼──────────────────
String          | __str__         | str(obj), print(obj)
                | __repr__        | repr(obj), REPL output
                | __format__      | f"{obj:spec}"
────────────────┼─────────────────┼──────────────────
Comparison      | __eq__          | ==
                | __ne__          | !=
                | __lt__          | <
                | __le__          | <=
                | __gt__          | >
                | __ge__          | >=
────────────────┼─────────────────┼──────────────────
Math            | __add__         | +
                | __sub__         | -
                | __mul__         | *
                | __truediv__     | /
                | __floordiv__    | //
                | __mod__         | %
                | __pow__         | **
                | __radd__        | 3 + obj (right-side)
────────────────┼─────────────────┼──────────────────
Container       | __len__         | len(obj)
                | __getitem__     | obj[key]
                | __setitem__     | obj[key] = val
                | __delitem__     | del obj[key]
                | __contains__    | x in obj
                | __iter__        | iter(obj), for loop
                | __next__        | next(obj)
────────────────┼─────────────────┼──────────────────
Attribute       | __getattr__     | obj.name (not found)
                | __getattribute__| obj.name (every access)
                | __setattr__     | obj.name = val
                | __delattr__     | del obj.name
────────────────┼─────────────────┼──────────────────
Context         | __enter__       | with obj:
                | __exit__        | end of with block
────────────────┼─────────────────┼──────────────────
Callable        | __call__        | obj()
────────────────┼─────────────────┼──────────────────
Descriptors     | __get__         | (descriptor protocol)
                | __set__         | (used by @property)
                | __delete__      |
```

---

## 16. Symbols & WeakMap

> JavaScript's way to create truly private-like behaviour.

```javascript
// SYMBOL — unique identifier, can use as property key
const _secret = Symbol("secret");

class SafeBox {
    constructor(value) {
        this[_secret] = value;       // stored under Symbol key
        this.label = "Safe Box";
    }
    
    reveal(password) {
        if (password !== "opensesame") throw new Error("Wrong password!");
        return this[_secret];
    }
}

const box = new SafeBox("treasure");
console.log(box.label);              // "Safe Box"
console.log(Object.keys(box));       // ["label"] ← symbol not in keys!
console.log(box[_secret]);           // "treasure" (if you have the symbol)
// console.log(box._secret);         // undefined (string key, not symbol)

// WEAKMAP — truly private, no leak
const _balance = new WeakMap();

class BankAccount {
    constructor(owner, balance) {
        this.owner = owner;
        _balance.set(this, balance);  // stored outside object entirely
    }
    
    deposit(amount) {
        _balance.set(this, _balance.get(this) + amount);
    }
    
    get balance() {
        return _balance.get(this);
    }
}

const acc = new BankAccount("Shiv", 10000);
acc.deposit(5000);
console.log(acc.balance);   // 15000
// There is NO way to access _balance from outside this module
// JSON.stringify(acc) → {"owner":"Shiv"}  — balance not included!
```

---

## 17. Dataclasses

> Python 3.7+ feature — auto-generates `__init__`, `__repr__`, `__eq__` and more.

```python
from dataclasses import dataclass, field, asdict, astuple
from typing import List

@dataclass
class Product:
    name: str
    price: float
    category: str = "General"       # default value
    tags: List[str] = field(default_factory=list)  # mutable default
    
    # Auto-generated: __init__, __repr__, __eq__

p1 = Product("Laptop", 60000, "Electronics", ["portable", "fast"])
p2 = Product("Mouse", 500)

print(p1)            # Product(name='Laptop', price=60000, category='Electronics', tags=['portable','fast'])
print(p1 == p2)      # False (compares all fields)

# Convert to dict/tuple
print(asdict(p1))    # {'name': 'Laptop', 'price': 60000, ...}
print(astuple(p1))   # ('Laptop', 60000, 'Electronics', [...])

# Frozen dataclass — immutable (like namedtuple but better)
@dataclass(frozen=True, order=True)
class Point:
    x: float
    y: float
    
    @property
    def magnitude(self):
        return (self.x**2 + self.y**2) ** 0.5

pts = [Point(3, 4), Point(1, 1), Point(0, 5)]
print(sorted(pts))   # [Point(0,5), Point(1,1), Point(3,4)] ← sorted by x then y!
# Point(1,1).x = 99  # FrozenInstanceError!

# Post-init processing
@dataclass
class Circle:
    radius: float
    area: float = field(init=False)   # not in __init__ args
    
    def __post_init__(self):           # runs after __init__
        import math
        self.area = math.pi * self.radius ** 2

c = Circle(5)
print(c.area)   # 78.53...
```

---

## 18. Proxy & Reflect

> JavaScript's most powerful meta-programming tools — intercept any operation on an object.

```javascript
// Proxy — wrap an object, intercept operations
const validator = {
    set(target, prop, value) {
        if (prop === "age") {
            if (typeof value !== "number") throw new TypeError("age must be a number");
            if (value < 0 || value > 150) throw new RangeError("age must be 0-150");
        }
        if (prop === "email") {
            if (!value.includes("@")) throw new TypeError("Invalid email");
        }
        Reflect.set(target, prop, value);  // default behaviour
        return true;
    },
    
    get(target, prop) {
        if (prop in target) {
            return Reflect.get(target, prop);
        }
        return `Property '${prop}' doesn't exist`;
    }
};

class User {
    constructor(name) { this.name = name; }
}

const user = new Proxy(new User("Shiv"), validator);
user.age = 25;            // ✅
user.email = "s@a.com";   // ✅
// user.age = "old";      // TypeError
// user.age = 200;        // RangeError
console.log(user.phone);  // Property 'phone' doesn't exist

// Observable pattern with Proxy
function makeObservable(target) {
    const listeners = {};
    
    return new Proxy(target, {
        set(obj, prop, value) {
            const old = obj[prop];
            Reflect.set(obj, prop, value);
            if (listeners[prop]) {
                listeners[prop].forEach(fn => fn(value, old));
            }
            return true;
        },
        
        get(obj, prop) {
            if (prop === "onChange") {
                return (key, fn) => {
                    listeners[key] = listeners[key] || [];
                    listeners[key].push(fn);
                };
            }
            return Reflect.get(obj, prop);
        }
    });
}

const state = makeObservable({ count: 0, name: "Shiv" });
state.onChange("count", (newVal, oldVal) => {
    console.log(`count: ${oldVal} → ${newVal}`);
});
state.count = 1;   // count: 0 → 1
state.count = 5;   // count: 1 → 5
```

---

## 19. Metaclasses

> Classes of classes. Controls HOW a class is created. Expert-level Python.

```python
# A metaclass is to a class what a class is to an object
# class → creates objects
# metaclass → creates classes

# Default metaclass is `type`
print(type(int))    # <class 'type'>
print(type(str))    # <class 'type'>

# Creating a class with type directly (low-level)
Dog = type("Dog", (object,), {
    "species": "Canis",
    "bark": lambda self: f"{self.name} barks!"
})
d = Dog()
d.name = "Rex"
print(d.bark())  # Rex barks!

# Custom metaclass — auto-adds validation
class ValidatedMeta(type):
    def __new__(mcs, name, bases, namespace):
        # Check all methods have docstrings
        for key, value in namespace.items():
            if callable(value) and not key.startswith("_"):
                if not getattr(value, "__doc__", None):
                    raise TypeError(
                        f"Method '{name}.{key}' must have a docstring!"
                    )
        return super().__new__(mcs, name, bases, namespace)

class API(metaclass=ValidatedMeta):
    def get_user(self, user_id):
        """Fetch user by ID."""
        pass
    
    def delete_user(self, user_id):
        """Delete a user."""  # ← required by metaclass!
        pass
    
    # def bad_method(self):   # ← would raise TypeError!
    #     pass

# Singleton metaclass — only one instance ever
class SingletonMeta(type):
    _instances = {}
    
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self, url):
        self.url = url

db1 = DatabaseConnection("postgres://localhost/mydb")
db2 = DatabaseConnection("postgres://localhost/mydb")
print(db1 is db2)  # True — same object!
```

---

## 20. Design Patterns (Real World)

### Singleton Pattern

```python
# Python — using class
class Config(metaclass=SingletonMeta):
    def __init__(self):
        self.debug = False
        self.db_url = "postgres://localhost"

# JavaScript — using module (modules are singletons by default)
// config.js
class Config {
    #debug = false;
    #dbUrl = "postgres://localhost";
    
    get debug() { return this.#debug; }
    set debug(v) { this.#debug = v; }
}
export default new Config();  // one instance, exported once
```

### Factory Pattern

```python
class Notification:
    def send(self, message): raise NotImplementedError

class EmailNotification(Notification):
    def __init__(self, email): self.email = email
    def send(self, message): print(f"Email to {self.email}: {message}")

class SMSNotification(Notification):
    def __init__(self, phone): self.phone = phone
    def send(self, message): print(f"SMS to {self.phone}: {message}")

class PushNotification(Notification):
    def __init__(self, device_id): self.device_id = device_id
    def send(self, message): print(f"Push to {self.device_id}: {message}")

class NotificationFactory:
    _registry = {
        "email": EmailNotification,
        "sms":   SMSNotification,
        "push":  PushNotification,
    }
    
    @classmethod
    def create(cls, type_, *args):
        klass = cls._registry.get(type_)
        if not klass:
            raise ValueError(f"Unknown notification type: {type_}")
        return klass(*args)

n = NotificationFactory.create("email", "shiv@aquera.com")
n.send("Hello!")  # Email to shiv@aquera.com: Hello!
```

### Observer Pattern

```python
from typing import Callable, List

class EventEmitter:
    def __init__(self):
        self._listeners: dict[str, List[Callable]] = {}
    
    def on(self, event: str, callback: Callable):
        self._listeners.setdefault(event, []).append(callback)
        return self  # chainable
    
    def off(self, event: str, callback: Callable):
        if event in self._listeners:
            self._listeners[event].remove(callback)
    
    def emit(self, event: str, *args, **kwargs):
        for listener in self._listeners.get(event, []):
            listener(*args, **kwargs)

class ShoppingCart(EventEmitter):
    def __init__(self):
        super().__init__()
        self.items = []
        self.total = 0
    
    def add_item(self, item, price):
        self.items.append({"item": item, "price": price})
        self.total += price
        self.emit("item_added", item, price)
        self.emit("total_changed", self.total)

cart = ShoppingCart()
cart.on("item_added", lambda item, price: print(f"Added: {item} ₹{price}"))
cart.on("total_changed", lambda total: print(f"New total: ₹{total}"))

cart.add_item("Laptop", 60000)
# Added: Laptop ₹60000
# New total: ₹60000
cart.add_item("Mouse", 500)
# Added: Mouse ₹500
# New total: ₹60500
```

### Decorator Pattern (not Python's @decorator syntax)

```python
# Wrapping objects to add behaviour without changing them
class Coffee:
    def cost(self): return 50
    def description(self): return "Coffee"

class MilkDecorator:
    def __init__(self, coffee): self._coffee = coffee
    def cost(self): return self._coffee.cost() + 20
    def description(self): return self._coffee.description() + ", Milk"

class SugarDecorator:
    def __init__(self, coffee): self._coffee = coffee
    def cost(self): return self._coffee.cost() + 10
    def description(self): return self._coffee.description() + ", Sugar"

class WhipDecorator:
    def __init__(self, coffee): self._coffee = coffee
    def cost(self): return self._coffee.cost() + 30
    def description(self): return self._coffee.description() + ", Whip"

# Build a custom coffee
my_coffee = WhipDecorator(SugarDecorator(MilkDecorator(Coffee())))
print(my_coffee.description())  # Coffee, Milk, Sugar, Whip
print(f"₹{my_coffee.cost()}")   # ₹110
```

---

## Summary — Quick Reference

```
CONCEPT          PYTHON                          JAVASCRIPT
─────────────────┼──────────────────────────────┼───────────────────────────
Class            class Dog:                      class Dog {
Constructor      def __init__(self):               constructor() {}
Inheritance      class Dog(Animal):               class Dog extends Animal {
Super            super().__init__()               super()
Private          self.__name                     #name
Protected (conv) self._name                      (use WeakMap or closure)
Class var        species = "Canis"               static species = "Canis"
Class method     @classmethod + cls              static method()
Static method    @staticmethod                   static method()
Getter           @property                       get propName()
Setter           @propName.setter                set propName(val)
Abstract class   from abc import ABC             throw new Error("implement!")
Dunder/magic     __str__, __add__, __len__       toString(), Symbol.iterator
Multiple inherit class D(B, C)                   Mixins (Object.assign)
MRO              __mro__ / C3 algorithm          Prototype chain
Dataclass        @dataclass                      (use plain class or library)
Metaclass        class Meta(type)                Proxy + Reflect
```

---

*See `python_examples.py` and `js_examples.js` for all runnable code examples.*
