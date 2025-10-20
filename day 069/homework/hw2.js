// ობიექტის შექმნა
const calculatorWithSymbol = {
number1: 0,
number2: 0,
userSymbol: '',

  // მეთოდი რომელიც ამოწმებს სიმბოლოს და აბრუნებს შედეგს
calculate() {
    switch (this.userSymbol) {
    case '+':
        return this.number1 + this.number2;
    case '-':
        return this.number1 - this.number2;
    case '*':
        return this.number1 * this.number2;
    case '/':
        return this.number1 / this.number2;
    default:
        return 'არასწორი სიმბოლო!';
    }
}
};

// მომხმარებელთან ინტერაქცია prompt()-ით
calculatorWithSymbol.number1 = Number(prompt("შეიყვანე პირველი რიცხვი:"));
calculatorWithSymbol.number2 = Number(prompt("შეიყვანე მეორე რიცხვი:"));
calculatorWithSymbol.userSymbol = prompt("შეიყვანე ოპერაციის სიმბოლო (+, -, *, /):");

// შედეგის ჩვენება
console.log("შედეგი არის:", calculatorWithSymbol.calculate());
