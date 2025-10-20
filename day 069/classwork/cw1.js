const user = {
  name: "Temuri",
  greet: function() {
    console.log(`გამარჯობა, ${this.name}!`);
  }
};

user.greet(); // გამოტანს: "გამარჯობა, Temuri!"
