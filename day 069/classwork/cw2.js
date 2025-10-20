const car = {
  brand: "BMW",
  speed: 0,

  drive: function() {
    this.speed += 50;
    console.log(`Car is driving at ${this.speed} km/h`);
  },

  stop: function() {
    this.speed = 0;
    console.log("Car stopped");
  }
};

car.drive(); // ➜ Car is driving at 50 km/h  
car.drive(); // ➜ Car is driving at 100 km/h  
car.stop();  // ➜ Car stopped
