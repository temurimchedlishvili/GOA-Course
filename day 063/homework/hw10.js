// typeof ოპერატორი
// typeof გამოიყენება იმის გასარკვევად, თუ რა ტიპის მნიშვნელობა (type) აქვს ცვლადს.
// ის ყოველთვის აბრუნებს სტრინგს, მაგალითად: "number", "string", "boolean", "object", "undefined", "function", "bigint", "symbol".

// 1) რიცხვი (Number)
let num = 42;
console.log(typeof num); // "number"

// 2) ტექსტი (String)
let text = "Hello, World!";
console.log(typeof text); // "string"

// 3) ლოგიკური ტიპი (Boolean)
let isActive = true;
console.log(typeof isActive); // "boolean"

// 4) ფუნქცია (Function)
function greet() {
console.log("გამარჯობა!");
}
console.log(typeof greet); // "function"
