function purchaseMessage(item, price, quantity) {
  return `You bought ${quantity} ${item}${quantity > 1 ? 's' : ''} for a total of ${price * quantity} GEL.`;
}

// მაგალითი გამოყენების
console.log(purchaseMessage("apple", 2, 5));
