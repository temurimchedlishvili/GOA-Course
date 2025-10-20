// სინტაქსი

// Template literal-ები იწყება (backtick)** სიმბოლოთი, და არა'ან". ცვლადების ჩასასმელად გამოიყენება **${variable}`.
// const name = "Temuri";
// const age = 20;
//ჩვეულებრივი სტრიქონებით
// console.log("Hello, my name is " + name + " and I am " + age + " years old.");
// Template literals-ის გამოყენებით
// console.log(`Hello, my name is ${name} and I am ${age} years old.`);
// გამოსავალი ორივეში ერთნაირია:
// Hello, my name is Temuri and I am 20 years old.


// მრავალსტრიქონიანი ტექსტი
// ჩვეულ სტრიქონებში მრავალსტრიქონიანი ტექსტი უნდა გაწყვეტილი იყოს \n-ით:
// console.log("Hello\nWorld");
// Template literals-ით ეს ბევრად მარტივია:
// console.log(`Hello
// World`);

// დინამიური გამოხმაურება
// Template literals-ით შეგიძლიათ პირდაპირ ჩასვათ გამოთვლები ${}-ში:
// const a = 5;
// const b = 10;
// console.log(`5 + 10 = ${a + b}`);
// გამოსავალი:
// 5 + 10 = 15