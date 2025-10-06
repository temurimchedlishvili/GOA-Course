// მომხმარებელს შევეკითხოთ ასაკი
let age = prompt("შეიყვანეთ თქვენი ასაკი:");

// გადავაქციოთ რიცხვად
age = Number(age);

// პირობის შემოწმება
if (age >= 0 && age <= 12) {
console.log("ბავშვი");
alert("ბავშვი");
} else if (age >= 13 && age <= 19) {
console.log("მოზარდი");
alert("მოზარდი");
} else if (age >= 20) {
console.log("ზრდასრული");
alert("ზრდასრული");
} else {
console.log("არასწორი ასაკი");
alert("არასწორი ასაკი");
}
