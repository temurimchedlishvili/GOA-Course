const items = document.querySelectorAll(".item"); // ყველა პარაგრაფს ვიღებთ class-ით

items.forEach(p => {
  p.style.color = "green";        // ტექსტის ფერი
  p.style.fontSize = "20px";      // ტექსტის ზომა
  p.style.fontWeight = "bold";    // ტექსტის bold
  p.style.marginBottom = "10px";  // ქვედა გამოტოვება
});
