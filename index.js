// class Cars{
//     constructor(name,brand,price){
//         this.name = name;
//         this.brand = brand
//         this.price = price
//         this._discount = 15
//     }

//     // seeters and getting 
//     getdiscount(){
//         return this.price - this._discount 
//     }


//     // set discount 
//     setDiscount(discount){
//         this._discount = discount
//     }
// }

// const obj1 = new Cars()
// // console.log(obj1);

// const obj2 = new Cars("TATA" , "Balero" , 17000000 , 2024)
// console.log(obj2);
// obj2._discount = 26
// console.log(obj2);

class Product{
    #currency = "INR";
    constructor(name, price){
        this.name = name;
        this.price = price;
        this.currency = this.#currency;
    }
    
    total_price(quantity){
        // if quantity is undefined and price is number it won't throw it would become NaN 
        return this.price * quantity;
    }
}

const laptop = new Product("Laptop", 60000);
const mouse = new Product("Mouse", 1000);


console.log(laptop.currency);
laptop.currency = "USD";
console.log(laptop.currency);

// console.log(mouse.name);
// console.log(laptop.total_price()); // basically JS doesn't throw error if we don't pass quantity because if value is not passed, it will take default value as 1

