// ობიექტის შექმნა
const messageBuilder = {
text: "",

add(word) {
    this.text += word + " ";
    return this;
},

upper() {
    this.text = this.text.toUpperCase();
    return this;
},

print() {
    console.log(this.text.trim());
    return this;
}
};

// გამოყენების მაგალითი:
messageBuilder
.add("hello")
.add("world")
.upper()
.print(); // გამოიტანს: HELLO WORLD
