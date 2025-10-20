// წამოვიღოთ ელემენტი DOM-დან მისი ID-ს მიხედვით
const box = document.getElementById("myBox");

// შევინახეთ ცვლადში და გამოვიტანეთ console-ში
console.log(box);

// დინამიურად შევცვალოთ სტილი JS-დანაც
box.style.border = "2px solid darkblue";
box.style.cursor = "pointer";

// სურვილისამებრ ტექსტიც შევცვალოთ
box.textContent = "ეს ელემენტი წამოვიღე JS-ით 😎";
