// ვქმნით ობიექტების სიას სახელით cars
const cars = [
{ brand: "Toyota", year: 2018 },
{ brand: "BMW", year: 2022 },
{ brand: "Mercedes", year: 2021 },
{ brand: "Ford", year: 2016 }
];

// ვფილტრავთ მხოლოდ ახალ მანქანებს (2020 ან უფრო ახალი)
const newCars = cars.filter(car => car.year >= 2020);

// ვბეჭდავთ ახალ მანქანებს
newCars.forEach(car => {
console.log("მარკა:", car.brand, "| წელი:", car.year);
});
