const users = [
{ name: "თემური", age: 20 },
{ name: "ნიკა", age: 25 },
{ name: "ანა", age: 16 }
];

// ვბეჭდავთ მხოლოდ იმ მომხმარებლებს, ვისაც ასაკი 18-ზე მეტი აქვს
for (let i = 0; i < users.length; i++) {
if (users[i].age > 18) {
console.log("სახელი:", users[i].name, "| ასაკი:", users[i].age);
}
}
