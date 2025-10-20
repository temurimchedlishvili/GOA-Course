// წამოვიღოთ ყველა ელემენტი კლასით .box
const boxes = document.querySelectorAll('.box');

// ფერების მასივი
const colors = [
'#ef4444', '#f97316', '#facc15', '#22c55e',
'#3b82f6', '#8b5cf6', '#ec4899', '#14b8a6'
];

// for loop -ით თითოეულს მივანიჭოთ განსხვავებული ფერი
for (let i = 0; i < boxes.length; i++) {
boxes[i].style.backgroundColor = colors[i % colors.length];
}
