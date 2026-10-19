/**
 * Complete OOP Examples in JavaScript — Beginner to Advanced
 * Run with: node js_examples.js
 */

// ══════════════════════════════════════════════════════════════════════
// SECTION 1: JAVASCRIPT ADVANCED SYNTAX
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 1: JAVASCRIPT ADVANCED SYNTAX");
console.log("═".repeat(60));

// ── Arrow Functions ────────────────────────────────────────────────
console.log("\n--- Arrow Functions ---");

const square   = x => x * x;
const add      = (a, b) => a + b;
const greet    = name => `Hello, ${name}!`;
const identity = x => x;

// Multi-line arrow
const clamp = (val, lo, hi) => {
    if (val < lo) return lo;
    if (val > hi) return hi;
    return val;
};

console.log(square(5));          // 25
console.log(add(3, 4));          // 7
console.log(greet("Shiv"));      // Hello, Shiv!
console.log(clamp(15, 0, 10));   // 10

// Arrow functions with array methods
const products = [
    { name: "Mouse",    price: 500 },
    { name: "Laptop",   price: 60000 },
    { name: "Keyboard", price: 2000 },
];

const sorted     = [...products].sort((a, b) => a.price - b.price);
const expensive  = products.filter(p => p.price > 1000);
const names      = products.map(p => p.name);
const total      = products.reduce((sum, p) => sum + p.price, 0);
const hasLaptop  = products.some(p => p.name === "Laptop");
const allPos     = products.every(p => p.price > 0);

console.log("Sorted:", sorted.map(p => p.name));
console.log("Expensive:", expensive.map(p => p.name));
console.log("Total: ₹" + total);
console.log("Has Laptop?", hasLaptop);
console.log("All positive?", allPos);


// ── Spread & Rest ──────────────────────────────────────────────────
console.log("\n--- Spread & Rest ---");

const nums1 = [1, 2, 3];
const nums2 = [4, 5, 6];
const combined = [...nums1, ...nums2];
console.log(combined);           // [1, 2, 3, 4, 5, 6]

const obj1 = { name: "Shiv", age: 25 };
const obj2 = { ...obj1, city: "Delhi", age: 26 };  // age overridden
console.log(obj2);               // { name:'Shiv', age:26, city:'Delhi' }

const [first, second, ...rest] = [10, 20, 30, 40, 50];
console.log(first, second, rest); // 10 20 [30,40,50]

// Rest parameters
const sum = (...nums) => nums.reduce((acc, n) => acc + n, 0);
console.log(sum(1, 2, 3, 4, 5));  // 15
console.log(Math.max(...nums1));   // 3


// ── Destructuring ──────────────────────────────────────────────────
console.log("\n--- Destructuring ---");

const { name: userName, age = 0, city = "Unknown" } = { name: "Shiv", age: 25 };
console.log(userName, age, city);   // Shiv 25 Unknown

// Nested
const { profile: { address: { city: userCity = "N/A" } = {} } = {} } =
    { profile: { address: { city: "Delhi" } } };
console.log(userCity);  // Delhi

// Swap variables
let a = 1, b = 2;
[a, b] = [b, a];
console.log(a, b);  // 2 1

// In function parameters
const displayProduct = ({ name, price, category = "General" }) =>
    `${name} - ₹${price} (${category})`;
console.log(displayProduct({ name: "Laptop", price: 60000, category: "Electronics" }));


// ── Optional Chaining & Nullish Coalescing ─────────────────────────
console.log("\n--- Optional Chaining & Nullish Coalescing ---");

const user = {
    name: "Shiv",
    profile: {
        address: { city: "Delhi" }
    },
    getName: () => "Shiv Singh",
};

console.log(user?.profile?.address?.city);     // Delhi
console.log(user?.settings?.theme);            // undefined (no crash)
console.log(user?.getName?.());                // Shiv Singh
console.log(user?.getAge?.() ?? 25);           // 25 (method doesn't exist)

// ?? vs ||
console.log(0 ?? "default");    // 0   (0 is NOT null/undefined)
console.log(0 || "default");    // "default" (0 is falsy)
console.log("" ?? "default");   // ""  (empty string is not null)
console.log("" || "default");   // "default" (empty string is falsy)

// ??= logical assignment
let config = null;
config ??= { theme: "dark" };
console.log(config);   // { theme: 'dark' }


// ── Template Literals ──────────────────────────────────────────────
console.log("\n--- Template Literals ---");

const price = 60000;
const msg   = `Laptop costs ₹${price.toLocaleString("en-IN")}`;
console.log(msg);   // Laptop costs ₹60,000

// Multi-line
const table = `
┌─────────────┬──────────┐
│ Product     │ Price    │
├─────────────┼──────────┤
${products.map(p => `│ ${p.name.padEnd(11)} │ ₹${String(p.price).padStart(7)} │`).join("\n")}
└─────────────┴──────────┘`.trim();
console.log(table);


// ══════════════════════════════════════════════════════════════════════
// SECTION 2: CLASSES & OBJECTS
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 2: CLASSES & OBJECTS");
console.log("═".repeat(60));

class Dog {
    static species = "Canis lupus familiaris";
    static #count  = 0;

    constructor(name, breed, age) {
        this.name  = name;
        this.breed = breed;
        this.age   = age;
        Dog.#count++;
    }

    bark   = () => `${this.name} says: Woof!`;        // arrow — safe this binding
    info   = () => `${this.name} (${this.breed}), ${this.age}yrs`;
    static getCount = () => Dog.#count;

    toString() {
        return `Dog<${this.name}>`;
    }
}

const dog1 = new Dog("Bruno", "German Shepherd", 3);
const dog2 = new Dog("Bella", "Labrador", 2);

console.log(dog1.bark());          // Bruno says: Woof!
console.log(dog2.info());          // Bella (Labrador), 2yrs
console.log(Dog.species);          // Canis lupus familiaris
console.log(Dog.getCount());       // 2
console.log(`${dog1}`);            // Dog<Bruno>   (toString)
console.log(dog1 instanceof Dog);  // true


// ══════════════════════════════════════════════════════════════════════
// SECTION 3: INSTANCE / CLASS / STATIC
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 3: INSTANCE / CLASS / STATIC");
console.log("═".repeat(60));

class Employee {
    static company = "Aquera Inc";
    static #total  = 0;

    constructor(name, salary) {
        this.name   = name;
        this.salary = salary;
        Employee.#total++;
    }

    // Class (static) methods
    static getInfo     = () => `${Employee.company} — ${Employee.#total} employees`;
    static fromObject  = ({ name, salary }) => new Employee(name, salary);
    static isValidSalary = amount => typeof amount === "number" && amount > 0;

    // Instance method
    getDetails = () => `${this.name}: ₹${this.salary.toLocaleString("en-IN")}`;

    toString() { return `Employee(${this.name})`; }
}

const e1 = new Employee("Shiv", 80000);
const e2 = Employee.fromObject({ name: "Raj", salary: 90000 });

console.log(Employee.getInfo());          // Aquera Inc — 2 employees
console.log(Employee.isValidSalary(-5)); // false
console.log(e1.getDetails());             // Shiv: ₹80,000


// ══════════════════════════════════════════════════════════════════════
// SECTION 4: PROPERTIES — GETTERS & SETTERS
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 4: PROPERTIES");
console.log("═".repeat(60));

class Temperature {
    #celsius;

    constructor(celsius) {
        this.celsius = celsius;  // uses setter
    }

    get celsius()     { return this.#celsius; }
    set celsius(val)  {
        if (val < -273.15) throw new RangeError(`Below absolute zero: ${val}`);
        this.#celsius = val;
    }

    get fahrenheit()  { return this.#celsius * 9/5 + 32; }
    set fahrenheit(f) { this.celsius = (f - 32) * 5/9; }

    get kelvin()      { return this.#celsius + 273.15; }
    set kelvin(k)     { this.celsius = k - 273.15; }

    toString() { return `${this.#celsius.toFixed(2)}°C`; }
}

const t = new Temperature(100);
console.log(`${t}`);           // 100.00°C
console.log(t.fahrenheit);     // 212
console.log(t.kelvin);         // 373.15

t.fahrenheit = 32;
console.log(`${t}`);           // 0.00°C

try {
    t.celsius = -300;
} catch (e) {
    console.log("Error:", e.message);
}


// ══════════════════════════════════════════════════════════════════════
// SECTION 5: ENCAPSULATION — PRIVATE FIELDS
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 5: ENCAPSULATION");
console.log("═".repeat(60));

class BankAccount {
    #owner;
    #balance;
    #pin;
    #history = [];

    constructor(owner, balance, pin) {
        this.#owner   = owner;
        this.#balance = balance;
        this.#pin     = pin;
    }

    deposit(amount) {
        if (amount <= 0) throw new Error("Amount must be positive");
        this.#balance += amount;
        this.#history.push(`+ ₹${amount}`);
        return this;  // enable chaining
    }

    withdraw(amount, pin) {
        if (!this.#verifyPin(pin)) throw new Error("Wrong PIN!");
        if (amount > this.#balance) throw new Error("Insufficient funds");
        this.#balance -= amount;
        this.#history.push(`- ₹${amount}`);
        return this;
    }

    #verifyPin(pin) { return pin === this.#pin; }  // private method

    get balance()   { return this.#balance; }
    get owner()     { return this.#owner; }
    get history()   { return [...this.#history]; }  // return copy

    toString() {
        return `${this.#owner}: ₹${this.#balance.toLocaleString("en-IN")}`;
    }
}

const acc = new BankAccount("Shiv", 10000, "1234");
acc.deposit(5000).withdraw(2000, "1234");
console.log(`${acc}`);        // Shiv: ₹13,000
console.log(acc.history);     // ['+ ₹5000', '- ₹2000']
// console.log(acc.#balance)  // SyntaxError — truly private

try {
    acc.withdraw(100, "wrong");
} catch (e) {
    console.log("Error:", e.message);
}


// ══════════════════════════════════════════════════════════════════════
// SECTION 6: INHERITANCE
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 6: INHERITANCE");
console.log("═".repeat(60));

class Animal2 {
    constructor(name, age) {
        this.name = name;
        this.age  = age;
    }

    breathe = () => `${this.name} breathes`;
    eat     = () => `${this.name} eats`;
    sleep   = () => `${this.name} sleeps`;
    toString()   { return `${this.constructor.name}(${this.name}, ${this.age}yrs)`; }
}

class Dog2 extends Animal2 {
    constructor(name, age, breed) {
        super(name, age);
        this.breed = breed;
    }

    bark = () => `${this.name}: Woof!`;
    eat  = () => `${this.name} eats dog food`;   // override
    fetch = item => `${this.name} fetches the ${item}!`;
}

class Cat2 extends Animal2 {
    #indoor;
    constructor(name, age, indoor = true) {
        super(name, age);
        this.#indoor = indoor;
    }

    purr    = () => `${this.name} purrrs...`;
    eat     = () => `${this.name} eats cat food`;
    get indoor() { return this.#indoor; }
}

class Guidedog extends Dog2 {
    #owner;
    constructor(name, age, breed, owner) {
        super(name, age, breed);
        this.#owner = owner;
    }

    guide = () => `${this.name} guides ${this.#owner}`;
    eat() { return super.eat() + " (special diet)"; }  // regular method to use super
}

const animals = [
    new Dog2("Bruno", 3, "Labrador"),
    new Cat2("Whiskers", 5),
    new Guidedog("Rex", 4, "Golden Retriever", "Meena"),
];

animals.forEach(a => {
    console.log(`${a} → ${a.eat()}`);
    if (a instanceof Dog2) console.log("  Bark:", a.bark());
});

console.log("Guidedog instanceof Dog2:", animals[2] instanceof Dog2);       // true
console.log("Guidedog instanceof Animal2:", animals[2] instanceof Animal2); // true


// ══════════════════════════════════════════════════════════════════════
// SECTION 7: MIXINS
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 7: MIXINS (Multiple Inheritance)");
console.log("═".repeat(60));

// Mixin factories (functions returning objects with methods)
const Serializable = (superclass) => class extends superclass {
    serialize()            { return JSON.stringify(this); }
    static deserialize(json) { return Object.assign(new this(), JSON.parse(json)); }
};

const Validatable = (superclass) => class extends superclass {
    validate() {
        for (const [key, rule] of Object.entries(this.constructor.rules || {})) {
            const val = this[key];
            if (rule.required && (val === undefined || val === null)) {
                throw new Error(`${key} is required`);
            }
            if (rule.min !== undefined && val < rule.min) {
                throw new Error(`${key} must be ≥ ${rule.min}`);
            }
            if (rule.max !== undefined && val > rule.max) {
                throw new Error(`${key} must be ≤ ${rule.max}`);
            }
        }
        return true;
    }
};

const Timestamped = (superclass) => class extends superclass {
    constructor(...args) {
        super(...args);
        this.createdAt = new Date().toISOString();
    }
};

// Compose mixins
class Product extends Serializable(Validatable(Timestamped(class {}))) {
    static rules = {
        price: { required: true, min: 0 },
        name:  { required: true },
    };

    constructor(name, price) {
        super();
        this.name  = name;
        this.price = price;
    }
}

const p = new Product("Laptop", 60000);
p.validate();
console.log("Valid product:", p.name, "₹" + p.price);
console.log("Created at:", p.createdAt);

try {
    const bad = new Product("Mouse", -5);
    bad.validate();
} catch (e) {
    console.log("Validation error:", e.message);
}


// ══════════════════════════════════════════════════════════════════════
// SECTION 8: POLYMORPHISM
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 8: POLYMORPHISM");
console.log("═".repeat(60));

class Shape {
    area()      { throw new Error(`${this.constructor.name}.area() not implemented`); }
    perimeter() { throw new Error(`${this.constructor.name}.perimeter() not implemented`); }

    describe = () =>
        `${this.constructor.name}: area=${this.area().toFixed(2)}, perimeter=${this.perimeter().toFixed(2)}`;

    compareTo = (other) => this.area() - other.area();
}

class Circle extends Shape {
    constructor(r) { super(); this.r = r; }
    area()         { return Math.PI * this.r ** 2; }
    perimeter()    { return 2 * Math.PI * this.r; }
}

class Rectangle extends Shape {
    constructor(w, h) { super(); this.w = w; this.h = h; }
    area()            { return this.w * this.h; }
    perimeter()       { return 2 * (this.w + this.h); }
}

class Triangle extends Shape {
    constructor(a, b, c) { super(); this.a = a; this.b = b; this.c = c; }
    area() {
        const s = (this.a + this.b + this.c) / 2;
        return Math.sqrt(s * (s - this.a) * (s - this.b) * (s - this.c));
    }
    perimeter() { return this.a + this.b + this.c; }
}

const shapes = [new Circle(5), new Rectangle(4, 6), new Triangle(3, 4, 5)];
shapes.forEach(s => console.log(s.describe()));

// Sort polymorphically
const sorted_shapes = [...shapes].sort((a, b) => a.compareTo(b));
console.log("Sorted by area:", sorted_shapes.map(s => s.constructor.name));

// Total area — polymorphic reduce
const totalArea = shapes.reduce((sum, s) => sum + s.area(), 0);
console.log(`Total area: ${totalArea.toFixed(2)}`);


// ══════════════════════════════════════════════════════════════════════
// SECTION 9: SYMBOLS & WEAKMAP (Advanced Privacy)
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 9: SYMBOLS & WEAKMAP");
console.log("═".repeat(60));

// Symbol-based privacy (soft private)
const _secret = Symbol("secret");
const _hash   = Symbol("hash");

class SafeBox {
    constructor(value, password) {
        this[_secret]   = value;
        this[_hash]     = password;
        this.label      = "Safe Box";
    }

    open(password) {
        if (password !== this[_hash]) throw new Error("Wrong password!");
        return this[_secret];
    }

    toJSON() { return { label: this.label }; }  // symbol keys NOT in JSON
}

const box = new SafeBox("my secret treasure", "opensesame");
console.log(box.label);              // Safe Box
console.log(Object.keys(box));       // ['label']  ← symbols hidden
console.log(box.open("opensesame")); // my secret treasure
console.log(JSON.stringify(box));    // {"label":"Safe Box"}

// WeakMap privacy (truly private, no reference leak)
const _data = new WeakMap();

class Observable {
    constructor(value) {
        _data.set(this, { value, listeners: [] });
    }

    get value() { return _data.get(this).value; }

    set value(newVal) {
        const state   = _data.get(this);
        const oldVal  = state.value;
        state.value   = newVal;
        state.listeners.forEach(fn => fn(newVal, oldVal));
    }

    subscribe(fn) {
        _data.get(this).listeners.push(fn);
        return () => {  // returns unsubscribe function
            const listeners = _data.get(this).listeners;
            const idx       = listeners.indexOf(fn);
            if (idx > -1) listeners.splice(idx, 1);
        };
    }
}

const obs = new Observable(10);
const unsub = obs.subscribe((newVal, oldVal) =>
    console.log(`  Observable: ${oldVal} → ${newVal}`)
);
obs.value = 20;    // Observable: 10 → 20
obs.value = 30;    // Observable: 20 → 30
unsub();           // unsubscribed
obs.value = 40;    // (no output)
console.log("Final value:", obs.value);  // 40


// ══════════════════════════════════════════════════════════════════════
// SECTION 10: PROXY & REFLECT
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 10: PROXY & REFLECT");
console.log("═".repeat(60));

// Validation proxy
function createValidated(rules) {
    return (target) => new Proxy(target, {
        set(obj, prop, value) {
            const rule = rules[prop];
            if (rule) {
                if (rule.type && typeof value !== rule.type) {
                    throw new TypeError(`${prop} must be ${rule.type}, got ${typeof value}`);
                }
                if (rule.min !== undefined && value < rule.min) {
                    throw new RangeError(`${prop} must be ≥ ${rule.min}`);
                }
                if (rule.pattern && !rule.pattern.test(value)) {
                    throw new Error(`${prop} format invalid`);
                }
            }
            return Reflect.set(obj, prop, value);
        },

        get(obj, prop) {
            if (!(prop in obj) && typeof prop === "string" && !prop.startsWith("_")) {
                console.warn(`  ⚠ Accessing non-existent property: ${prop}`);
            }
            return Reflect.get(obj, prop);
        }
    });
}

class UserModel {
    constructor(data = {}) {
        Object.assign(this, data);
    }
}

const validatedUser = createValidated({
    age:   { type: "number", min: 0 },
    email: { type: "string", pattern: /^[^\s@]+@[^\s@]+\.[^\s@]+$/ },
    name:  { type: "string" },
})(new UserModel());

validatedUser.name  = "Shiv";
validatedUser.email = "shiv@aquera.com";
validatedUser.age   = 25;
console.log("Valid user set");

try {
    validatedUser.age = -5;
} catch (e) {
    console.log("Proxy blocked:", e.message);
}

// Reactive state with Proxy
function reactive(state, onUpdate) {
    return new Proxy(state, {
        set(obj, prop, value) {
            const old = obj[prop];
            Reflect.set(obj, prop, value);
            if (old !== value) onUpdate(prop, value, old);
            return true;
        }
    });
}

const appState = reactive(
    { count: 0, user: null },
    (prop, newVal, oldVal) => console.log(`  State[${prop}]: ${oldVal} → ${newVal}`)
);

appState.count = 1;   // State[count]: 0 → 1
appState.count = 5;   // State[count]: 1 → 5
appState.user = "Shiv"; // State[user]: null → Shiv


// ══════════════════════════════════════════════════════════════════════
// SECTION 11: DESIGN PATTERNS
// ══════════════════════════════════════════════════════════════════════
console.log("\n" + "═".repeat(60));
console.log("SECTION 11: DESIGN PATTERNS");
console.log("═".repeat(60));

// ── Singleton ──────────────────────────────────────────────────────
class Singleton {
    static #instance = null;

    constructor(data) {
        if (Singleton.#instance) return Singleton.#instance;
        this.data = data;
        Singleton.#instance = this;
    }

    static getInstance(data) {
        if (!Singleton.#instance) new Singleton(data);
        return Singleton.#instance;
    }
}

const s1 = new Singleton({ theme: "dark" });
const s2 = new Singleton({ theme: "light" });
console.log(s1 === s2);       // true
console.log(s2.data.theme);   // dark (first one wins)


// ── Observer (EventEmitter) ────────────────────────────────────────
class EventEmitter {
    #events = new Map();

    on(event, fn) {
        if (!this.#events.has(event)) this.#events.set(event, new Set());
        this.#events.get(event).add(fn);
        return () => this.off(event, fn);  // returns unsubscribe fn
    }

    off(event, fn) {
        this.#events.get(event)?.delete(fn);
    }

    emit(event, ...args) {
        this.#events.get(event)?.forEach(fn => fn(...args));
    }

    once(event, fn) {
        const wrapper = (...args) => { fn(...args); this.off(event, wrapper); };
        return this.on(event, wrapper);
    }
}

class ShoppingCart extends EventEmitter {
    #items = [];
    #total = 0;

    add(name, price) {
        this.#items.push({ name, price });
        this.#total += price;
        this.emit("added", { name, price });
        this.emit("total", this.#total);
        return this;
    }

    remove(name) {
        const idx = this.#items.findIndex(i => i.name === name);
        if (idx > -1) {
            const [item] = this.#items.splice(idx, 1);
            this.#total -= item.price;
            this.emit("removed", item);
            this.emit("total", this.#total);
        }
        return this;
    }

    get total() { return this.#total; }
    get items()  { return [...this.#items]; }
}

const cart = new ShoppingCart();
cart.on("added",   item  => console.log(`  + ${item.name} ₹${item.price}`));
cart.on("removed", item  => console.log(`  - ${item.name}`));
cart.on("total",   total => console.log(`  Total: ₹${total}`));
cart.add("Laptop", 60000).add("Mouse", 500);
cart.remove("Mouse");


// ── Factory ────────────────────────────────────────────────────────
class NotificationFactory {
    static #registry = new Map();

    static register(type, cls) {
        NotificationFactory.#registry.set(type, cls);
        return NotificationFactory;
    }

    static create(type, ...args) {
        const Cls = NotificationFactory.#registry.get(type);
        if (!Cls) throw new Error(`Unknown notification type: ${type}`);
        return new Cls(...args);
    }
}

class EmailNotification {
    constructor(email) { this.email = email; }
    send = msg => console.log(`  Email → ${this.email}: ${msg}`);
}

class SMSNotification {
    constructor(phone) { this.phone = phone; }
    send = msg => console.log(`  SMS  → ${this.phone}: ${msg}`);
}

class PushNotification {
    constructor(deviceId) { this.deviceId = deviceId; }
    send = msg => console.log(`  Push → ${this.deviceId}: ${msg}`);
}

// Register
NotificationFactory
    .register("email", EmailNotification)
    .register("sms",   SMSNotification)
    .register("push",  PushNotification);

console.log();
NotificationFactory.create("email", "shiv@aquera.com").send("Welcome to Aquera!");
NotificationFactory.create("sms",   "+91-9876543210").send("OTP: 4532");
NotificationFactory.create("push",  "device_abc123").send("New message!");


// ── Builder Pattern ────────────────────────────────────────────────
class QueryBuilder {
    #table = "";
    #conditions = [];
    #fields     = ["*"];
    #limit      = null;
    #orderBy    = null;

    from(table)       { this.#table = table; return this; }
    select(...fields) { this.#fields = fields; return this; }
    where(cond)       { this.#conditions.push(cond); return this; }
    orderBy(field, dir = "ASC") { this.#orderBy = `${field} ${dir}`; return this; }
    limit(n)          { this.#limit = n; return this; }

    build() {
        let query = `SELECT ${this.#fields.join(", ")} FROM ${this.#table}`;
        if (this.#conditions.length) query += ` WHERE ${this.#conditions.join(" AND ")}`;
        if (this.#orderBy) query += ` ORDER BY ${this.#orderBy}`;
        if (this.#limit)   query += ` LIMIT ${this.#limit}`;
        return query;
    }
}

const query = new QueryBuilder()
    .from("users")
    .select("id", "name", "email")
    .where("age > 18")
    .where("active = true")
    .orderBy("name", "ASC")
    .limit(10)
    .build();

console.log("\nBuilt query:", query);


// ── Strategy Pattern ───────────────────────────────────────────────
class Sorter {
    #strategy;

    constructor(strategy) { this.#strategy = strategy; }
    setStrategy(strategy) { this.#strategy = strategy; return this; }
    sort(data)            { return this.#strategy([...data]); }
}

const strategies = {
    bubble: arr => {
        for (let i = 0; i < arr.length; i++)
            for (let j = 0; j < arr.length - i - 1; j++)
                if (arr[j] > arr[j+1]) [arr[j], arr[j+1]] = [arr[j+1], arr[j]];
        return arr;
    },
    native: arr => arr.sort((a, b) => a - b),
    reverse: arr => arr.sort((a, b) => b - a),
};

const data = [5, 2, 8, 1, 9, 3];
const sorter = new Sorter(strategies.bubble);
console.log("\nBubble sort:", sorter.sort(data));
console.log("Native sort:", sorter.setStrategy(strategies.native).sort(data));
console.log("Reverse sort:", sorter.setStrategy(strategies.reverse).sort(data));


// ── Iterator Protocol ──────────────────────────────────────────────
class Range {
    constructor(start, end, step = 1) {
        this.start = start;
        this.end   = end;
        this.step  = step;
    }

    [Symbol.iterator]() {
        let current = this.start;
        const { end, step } = this;
        return {
            next() {
                if (current <= end) {
                    const value = current;
                    current += step;
                    return { value, done: false };
                }
                return { value: undefined, done: true };
            }
        };
    }
}

const range = new Range(1, 10, 2);
console.log("\nRange 1-10 step 2:", [...range]);  // [1,3,5,7,9]
for (const n of new Range(1, 5)) process.stdout.write(n + " ");
console.log();  // 1 2 3 4 5


// ── Generator as Iterator ──────────────────────────────────────────
class InfiniteCounter {
    constructor(start = 0) { this.start = start; }

    *[Symbol.iterator]() {
        let n = this.start;
        while (true) yield n++;
    }
}

const counter = new InfiniteCounter(5);
const first5  = [];
for (const n of counter) {
    first5.push(n);
    if (first5.length === 5) break;
}
console.log("Infinite counter (first 5):", first5);  // [5,6,7,8,9]


console.log("\n" + "═".repeat(60));
console.log("All JavaScript OOP examples complete!");
console.log("═".repeat(60));
