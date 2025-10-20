// ობიექტის შექმნა
const counter = {
count: 0,

increment() {
    this.count++;
    return this; // აბრუნებს თვითონ ობიექტს (ჩეინინგისთვის)
},

decrement() {
    this.count--;
    return this;
},

show() {
    console.log(this.count);
    return this;
}
};

// გამოყენების მაგალითი:
counter.increment().increment().show().decrement().show();
