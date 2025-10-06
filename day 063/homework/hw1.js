// მომხმარებლის მიერ შემოტანილი რიცხვი (მაგალითად prompt-ით)
let number = prompt("შეიყვანეთ რიცხვი:");

// prompt ყოველთვის აბრუნებს ტექსტს, ამიტომ გადავიყვანოთ რიცხვად
number = Number(number);

// შევამოწმოთ რიცხვი if-else გამოყენებით
if (number > 0) {
console.log("დადებითი");
alert("დადებითი");
} else if (number < 0) {
console.log("უარყოფითი");
alert("უარყოფითი");
} else {
console.log("ნულის ტოლია");
alert("ნულის ტოლია");
}
