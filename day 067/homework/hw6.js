// ვქმნით ობიექტების სიას სახელით users
const users = [
{ name: "თემური", age: 20 },
{ name: "ნიკა", age: 25 },
{ name: "ანა", age: 22 }
];

// ვბეჭდავთ თითოეული მომხმარებლის სახელს და ასაკს
for (let i = 0; i < users.length; i++) {

console.log("სახელი:", users[i].name, "| ასაკი:", users[i].age);

}
