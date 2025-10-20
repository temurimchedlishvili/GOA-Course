// ობიექტის შექმნა
const calculator = {
a: 10,
b: 5,

add() {
    return this.a + this.b;
},

subtract() {
    return this.a - this.b;
},

multiply() {
    return this.a * this.b;
},

divide() {
    return this.a / this.b;
}
};

// თითოეული მეთოდის გამოძახება და შედეგის დაბეჭდვა
console.log("Addition:", calculator.add());
console.log("Subtraction:", calculator.subtract());
console.log("Multiplication:", calculator.multiply());
console.log("Division:", calculator.divide());
