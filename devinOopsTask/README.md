# OOP Mastery — Python 🐍 + JavaScript ⚡

A complete, beginner-to-advanced guide to **Object-Oriented Programming** in both Python and JavaScript — side by side.

Every concept is explained in the **easiest possible language**, with:

- 🏠 **Real-life analogies** (restaurants, banks, cars, phones)
- 🔬 **Internals** — what actually happens in memory
- 🏃 **Dry runs** — line-by-line execution traces
- 📊 **Visual diagrams** — Mermaid + ASCII memory maps
- ⚡ **Modern syntax** — arrow functions, spread, lambdas, comprehensions

---

## 📚 Reading Order

| # | File | What you'll learn |
|---|------|-------------------|
| 0 | `01-modern-syntax-toolkit.md` | **Read this FIRST.** Arrow functions, spread/rest, destructuring, template literals (JS). Lambdas, comprehensions, ternary, generator expressions, unpacking (Python). |
| 1 | `02-why-oop.md` | What OOP is, why it exists, the 4 pillars, procedural vs OOP thinking |
| 2 | `03-classes-and-objects.md` | Classes, objects, `constructor` / `__init__`, `this` / `self`, how `new` and `()` work internally |
| 3 | `04-encapsulation.md` | Data hiding, `#private` / `__private`, getters/setters, `@property`, name mangling |
| 4 | `05-methods-deep-dive.md` | Instance vs class vs static methods, `this` binding rules, `cls`, method vs function |
| 5 | `06-inheritance.md` | `extends`/`super`, prototype chain, `super()` MRO, multiple inheritance, Diamond problem |
| 6 | `07-polymorphism.md` | Method overriding, duck typing, operator overloading, dunder methods |
| 7 | `08-abstraction.md` | Abstract classes, `ABC`, interfaces, duck-typed interfaces in JS |
| 8 | `09-internals-advanced.md` | `__new__`, descriptors, `__slots__`, metaclasses, `Object.create`, prototype internals |
| 9 | `10-composition-solid.md` | Composition vs inheritance, SOLID principles, mixins, design pattern intro |
| 10 | `11-capstone-projects.md` | 3 full projects in BOTH languages: Bank System, E-commerce Cart, Notification Engine |

---

## 🧭 How to use this guide

```mermaid
flowchart LR
    A[01 Syntax Toolkit] --> B[02 Why OOP]
    B --> C[03 Classes & Objects]
    C --> D[04 Encapsulation]
    D --> E[05 Methods Deep Dive]
    E --> F[06 Inheritance]
    F --> G[07 Polymorphism]
    G --> H[08 Abstraction]
    H --> I[09 Internals]
    I --> J[10 Composition + SOLID]
    J --> K[11 Projects]
```

- 🟢 **Beginner sections** — read everything top to bottom
- 🟡 **Intermediate** — skip to Encapsulation onwards
- 🔴 **Advanced** — files 09–11

## 🛠️ Run the code

Two fully-runnable example files mirror every section of the guide — heavily commented, with expected output shown as `→` comments:

```bash
# Python — 13 sections, ~650 lines
python3 python_examples.py

# JavaScript — 12 sections, ~560 lines
node js_examples.js
```

Each file prints labeled section banners so you can match console output to code line-by-line.

## 💡 Legend used throughout

| Symbol | Meaning |
|--------|---------|
| 🐍 | Python code / concept |
| ⚡ | JavaScript code / concept |
| 🔬 | Internal / under-the-hood explanation |
| 🏃 | Dry run (step-by-step trace) |
| 🏠 | Real-life analogy |
| ⚠️ | Common trap / gotcha |
| 🆚 | Comparison between languages |
