// წამოვიღოთ ყველა ელემენტი რომლებიც კლასით არიან "box"
const boxes = document.querySelectorAll(".box");

// გამოვიტანოთ console-ში
console.log(boxes);

// ყველა ელემენტზე ციკლით გავიაროთ და დავამატოთ სტილი JS-დან
boxes.forEach((box, index) => {
  box.style.border = "2px solid darkblue";
  box.style.fontWeight = "bold";
  box.style.cursor = "pointer";
  box.textContent = `Box ${index + 1}`;
});
