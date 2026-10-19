# 01 — Modern Syntax Toolkit 🧰

> **Read this before anything else.**
> Throughout this guide we use modern JS (arrow functions, spread, destructuring) and modern Python (lambdas, comprehensions, ternary, generator expressions). This file teaches you ALL of them first — in the easiest way possible — so the OOP chapters never confuse you.

---

# PART A — JavaScript ⚡

## A1. Arrow Functions `=>`

### The idea
An arrow function is just a **shorter way to write a function**.

```js
// OLD way (function expression)
const add = function (a, b) {
  return a + b;
};

// NEW way (arrow function)
const addArrow = (a, b) => {
  return a + b;
};

// EVEN shorter — if body is one expression, drop {} and return
const addShort = (a, b) => a + b;

console.log(addShort(2, 3)); // 5
```

### Rules to remember

```js
// One parameter → parentheses optional
const square = x => x * x;
const square2 = (x) => x * x;   // same thing

// Zero parameters → parentheses REQUIRED
const greet = () => "Hello!";

// Returning an object → wrap it in () or JS thinks {} is a function body!
const makeUser = name => ({ name: name, role: "admin" });
//                        ↑ without (), {name: ...} would be parsed as a code block

// Multi-line body → need {} and explicit return
const discount = (price, pct) => {
  const cut = price * (pct / 100);
  return price - cut;
};
```

### 🔬 The BIG difference: `this` inside arrow functions

This is the #1 thing that matters for OOP:

> **Normal functions get their OWN `this`. Arrow functions BORROW `this` from wherever they were written.**

```js
const person = {
  name: "Shiv",

  normalSay() {
    return `Normal: ${this.name}`;   // `this` = person ✅
  },

  arrowSay: () => {
    return `Arrow: ${this.name}`;    // `this` = outer scope (not person!) ❌
  }
};

console.log(person.normalSay()); // "Normal: Shiv"
console.log(person.arrowSay());  // "Arrow: undefined"
```

**Memory picture:**

```
normalSay()  →  its own `this` box  →  filled by WHOEVER calls it (person)
arrowSay     →  NO `this` box       →  looks outside, captures parent's `this`
```

**Where arrow functions SHINE in OOP** — inside callbacks:

```js
class Counter {
  count = 0;

  start() {
    // Arrow borrows `this` from start() → points to the Counter object ✅
    setTimeout(() => {
      this.count++;
      console.log(this.count); // works!
    }, 1000);

    // Normal function would get `this` = undefined/global ❌
    // setTimeout(function() { this.count++; }, 1000); // breaks
  }
}
```

> ⚠️ **Rule of thumb:** use normal methods for class methods, arrow functions for callbacks *inside* methods.

---

## A2. Default Parameters

```js
function greet(name = "Guest") {
  return `Hello, ${name}`;
}

greet();          // "Hello, Guest"
greet("Shiv");    // "Hello, Shiv"

// Your index.js bug you already saw:
// total_price() with no quantity → quantity = undefined → price * undefined = NaN
// Fix:
const total = (price, quantity = 1) => price * quantity;
total(500);       // 500  (quantity defaults to 1)
total(500, 3);    // 1500
```

---

## A3. Template Literals `` ` `` (backticks)

```js
const name = "Laptop";
const price = 60000;

// OLD — ugly string concat
console.log("Product: " + name + ", Price: " + price);

// NEW — template literal with ${}
console.log(`Product: ${name}, Price: ${price}`);

// Can put ANY expression inside ${}
console.log(`With 18% GST: ${price * 1.18}`);  // 70800

// Multi-line strings
const html = `
  <div>
    <h1>${name}</h1>
  </div>`;
```

---

## A4. Spread `...` and Rest `...`

Same three dots, two opposite jobs:

- **Spread** = *unpack* (spread items OUT)
- **Rest** = *pack* (gather leftover items IN)

### Spread — unpacking

```js
// Arrays
const arr1 = [1, 2, 3];
const arr2 = [...arr1, 4, 5];       // [1,2,3,4,5] — copy + add
const merged = [...arr1, ...arr2];

// Objects
const user = { name: "Shiv", age: 25 };
const admin = { ...user, role: "admin" };
// { name:"Shiv", age:25, role:"admin" }

// Override a key — put it AFTER the spread
const updated = { ...user, age: 26 };   // age overwritten to 26
```

### Rest — packing

```js
// Collect remaining args into an array
function sum(...numbers) {          // rest: packs all args → array
  return numbers.reduce((a, b) => a + b, 0);
}
sum(1, 2, 3, 4);  // 10

// In destructuring (next section)
const [first, ...rest] = [10, 20, 30, 40];
// first = 10, rest = [20, 30, 40]
```

---

## A5. Destructuring — unpack values in one line

```js
// OBJECT destructuring
const product = { name: "Mouse", price: 1000, stock: 50 };

const { name, price } = product;         // name="Mouse", price=1000
const { name: productName } = product;   // rename → productName="Mouse"
const { rating = 5 } = product;          // default if missing → rating=5

// ARRAY destructuring
const colors = ["red", "green", "blue"];
const [primary, , tertiary] = colors;    // primary="red", skip green, tertiary="blue"

// Swapping without temp variable 🎉
let a = 1, b = 2;
[a, b] = [b, a];   // a=2, b=1

// Function parameters
const show = ({ name, price }) => `${name} costs ₹${price}`;
show(product);  // "Mouse costs ₹1000"
```

---

## A6. Shorthand & modern tricks used in this guide

```js
const name = "Shiv", age = 25;

// Object shorthand — key name = variable name
const user = { name, age };       // same as { name: name, age: age }

// Method shorthand in objects/classes
const calc = {
  add(a, b) { return a + b; }     // same as add: function(a,b){...}
};

// Optional chaining ?.  — safe access, no crash if null/undefined
const settings = {};
console.log(settings.theme?.color);   // undefined (no error!)

// Nullish coalescing ?? — default ONLY for null/undefined
const port = settings.port ?? 3000;   // 3000
// vs || which also rejects 0, "", false
0 || 3000   // → 3000 (wrong if 0 was valid!)
0 ?? 3000   // → 0 ✅

// Array methods you'll see constantly
[1,2,3].map(x => x * 2);              // [2,4,6]  transform each
[1,2,3].filter(x => x > 1);           // [2,3]    keep matching
[1,2,3].reduce((acc, x) => acc + x);  // 6        fold to one value
[1,2,3].find(x => x > 1);             // 2        first match
[1,2,3].forEach(x => console.log(x)); // loop, no return
```

---

# PART B — Python 🐍

## B1. Lambda Functions — one-line anonymous functions

Same idea as arrow functions: **small function, no name, one expression**.

```python
# Normal function
def add(a, b):
    return a + b

# Lambda — same thing, one line
add_lambda = lambda a, b: a + b

print(add_lambda(2, 3))  # 5
```

**Syntax:** `lambda parameters: single_expression`
(no `return` keyword — the expression IS returned automatically)

```python
square = lambda x: x * x
greet = lambda: "Hello"                    # zero params
first = lambda pair: pair[0]               # works on tuples
clamp = lambda x: max(0, min(x, 100))      # any expression
```

### Where lambdas are actually used

Almost always as a **quick throwaway argument**:

```python
products = [
    {"name": "Laptop", "price": 60000},
    {"name": "Mouse",  "price": 1000},
    {"name": "Keyboard", "price": 2500},
]

# sort by price — lambda extracts the key
cheapest_first = sorted(products, key=lambda p: p["price"])

# map / filter
names = list(map(lambda p: p["name"], products))
expensive = list(filter(lambda p: p["price"] > 2000, products))

# In OOP: default sort keys, callbacks, key functions
```

> ⚠️ Lambda = **ONE expression only**. No statements (`if` blocks, loops, assignments). If it needs more → write a `def`.

---

## B2. Ternary (Conditional Expression) — one-line if/else

```python
# Normal
if age >= 18:
    status = "adult"
else:
    status = "minor"

# Ternary — same thing, one line
status = "adult" if age >= 18 else "minor"
```

**Syntax:** `value_if_true if CONDITION else value_if_false`

```python
price = -50
label = "free" if price == 0 else ("invalid" if price < 0 else "paid")
#       ↑ nesting works but gets unreadable — max 1 level of nesting!

# Common OOP use: defaults in __init__
def __init__(self, price=None):
    self.price = price if price is not None else 0
# (modern idiom: `price if price is not None else 0` or just `price or 0` when 0 is invalid anyway)
```

⚠️ `x or default` trap: `0 or 99` → `99` because `0` is falsy. Use the explicit `is not None` check when `0`/`""`/`[]` are valid values.

---

## B3. Comprehensions — one-line loops that build collections

This is Python's superpower. The pattern:

```
[ expression  for item in iterable  if condition ]
   ↑ what you      ↑ loop              ↑ optional
     keep                                 filter
```

### List comprehension

```python
# Normal loop
squares = []
for x in range(5):
    squares.append(x * x)

# Comprehension — same thing, ONE line
squares = [x * x for x in range(5)]          # [0,1,4,9,16]

# With filter
evens = [x for x in range(10) if x % 2 == 0] # [0,2,4,6,8]

# Transform + filter together
prices = [100, 2500, 60000, 800]
big_gst = [p * 1.18 for p in prices if p > 1000]   # [2950.0, 70800.0]
```

### Dict comprehension

```python
names = ["laptop", "mouse"]
prices = [60000, 1000]

catalog = {n: p for n, p in zip(names, prices)}
# {'laptop': 60000, 'mouse': 1000}

# Flip keys/values
flipped = {v: k for k, v in catalog.items()}
```

### Set comprehension

```python
tags = ["sale", "SALE", "new", "New", "NEW"]
unique = {t.lower() for t in tags}   # {'sale', 'new'}
```

### 🏃 Dry run — read a comprehension like a sentence

```python
[p["price"] * 2 for p in products if p["price"] > 1000]
```

Read it backwards as English:
*"For each `p` in `products`, **if** price > 1000, **keep** `price * 2`."*

```
products = [{price:60000}, {price:1000}, {price:2500}]

p=Laptop   → 60000 > 1000? YES → keep 120000
p=Mouse    →  1000 > 1000? NO  → skip
p=Keyboard →  2500 > 1000? YES → keep 5000

Result: [120000, 5000]
```

---

## B4. Generator Expressions — lazy comprehensions

Change `[]` to `()` and the comprehension becomes **lazy** — it produces items one at a time instead of building the whole list in memory.

```python
# List — ALL items computed NOW, stored in memory
big_list = [x * x for x in range(1_000_000)]   # ~8 MB in RAM immediately

# Generator — NOTHING computed yet, computes on demand
big_gen = (x * x for x in range(1_000_000))    # tiny — just a recipe

next(big_gen)   # 0   — computes ONE item
next(big_gen)   # 1
# for x in big_gen: ... — pulls items one by one
```

**Why it matters:** processing a 10 GB log file — a list would crash your RAM; a generator sips one line at a time.

```python
total = sum(p["price"] for p in products)   # generator inside sum() — no list built
```

🔬 **Internals:** a generator object stores the loop's *state* and pauses at each `yield`-equivalent point. Calling `next()` resumes it. It's a **one-shot** — once exhausted, it's empty forever.

---

## B5. Unpacking (`*`, `**`) — Python's spread/rest

```python
# * unpacks iterables, ** unpacks dicts
nums = [1, 2, 3]
print(*nums)                    # 1 2 3  (same as print(1,2,3))

merged = [*nums, 4, 5]          # [1,2,3,4,5]  — like JS [...nums, 4, 5]

defaults = {"debug": True, "port": 3000}
config = {**defaults, "port": 8080}   # override port

# Rest in assignment
first, *rest = [10, 20, 30, 40]       # first=10, rest=[20,30,40]

# Rest in function params
def total(*prices):              # packs args into a tuple
    return sum(prices)
total(100, 200, 300)             # 600

def settings(**opts):            # packs kwargs into a dict
    return opts
settings(theme="dark", lang="en")  # {'theme':'dark','lang':'en'}
```

---

## B6. f-strings — Python's template literals

```python
name, price = "Laptop", 60000

print(f"Product: {name}, Price: ₹{price}")
print(f"GST: {price * 0.18:.2f}")        # expression + formatting
print(f"{name=}")                        # debug trick → name='Laptop'
```

---

## B7. map / filter / sorted / any / all — with lambdas

```python
nums = [1, 2, 3, 4]

list(map(lambda x: x * 2, nums))       # [2,4,6,8]
list(filter(lambda x: x % 2 == 0, nums))  # [2,4]

any(x > 3 for x in nums)               # True  — at least one
all(x > 0 for x in nums)               # True  — every one

max(products, key=lambda p: p["price"])    # richest item
```

> 💡 **Style note:** comprehension `[x*2 for x in nums]` is usually preferred over `map(lambda...)` — more readable. Use whichever fits.

---

## 🆚 Cheat-sheet: JS ↔ Python equivalents

| Task | JavaScript ⚡ | Python 🐍 |
|------|--------------|-----------|
| Tiny function | `(a,b) => a+b` | `lambda a,b: a+b` |
| One-line if/else | `c ? a : b` | `a if c else b` |
| Transform list | `arr.map(x => x*2)` | `[x*2 for x in arr]` |
| Filter list | `arr.filter(x => x>1)` | `[x for x in arr if x>1]` |
| Fold to value | `arr.reduce((a,x)=>a+x,0)` | `sum(arr)` / `functools.reduce` |
| String template | `` `${x}` `` | `f"{x}"` |
| Unpack array | `[...arr]` | `[*arr]` |
| Unpack object | `{...obj}` | `{**d}` |
| Rest params | `function(...args)` | `def f(*args)` |
| Kwargs pack | `{...opts}` param | `def f(**kw)` |
| Default param | `(x = 1)` | `def f(x=1)` |
| Safe access | `obj?.a?.b` | `getattr(obj,'a',None)` / `try` |
| Fallback | `a ?? b` | `a if a is not None else b` |
| Lazy sequence | `function*` generator | generator expression `(...)` |

---

## ✅ Self-check before moving on

```python
# Python — can you predict these?
[x**2 for x in range(6) if x % 2]                    # ?
{w: len(w) for w in ["hi", "hello"]}                  # ?
(v := sum(p for p in [10, 20, 30]))                   # ?
```

```js
// JS — predict these
const {a, ...rest} = {a:1, b:2, c:3};                 // rest = ?
const f = ({x=5}) => x * 2;  f({})                    // ?
[...[1,2], ...[3]]                                    // ?
```

<details><summary>Answers</summary>

- `[1, 9, 25]`, `{'hi':2, 'hello':5}`, `60`
- `rest = {b:2, c:3}`, `10`, `[1,2,3]`
</details>

---

➡️ **Next:** `02-why-oop.md`
