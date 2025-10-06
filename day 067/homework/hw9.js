// ვქმნით ობიექტების სიას სახელით products
const products = [
{ name: "ლეპტოპი", price: 2500 },
{ name: "ტელეფონი", price: 1200 },
{ name: "ტელევიზორი", price: 1800 },
{ name: "ყურსასმენი", price: 300 }
];

// ვპოულობთ ყველაზე ძვირ პროდუქტს
let mostExpensive = products[0]; // პირველ ელემენტს ვიღებთ საწყისად

for (let i = 1; i < products.length; i++) {
if (products[i].price > mostExpensive.price) {
    mostExpensive = products[i];
}
}

// ვბეჭდავთ შედეგს
console.log("ყველაზე ძვირი პროდუქტია:", mostExpensive.name, "| ფასი:", mostExpensive.price);
