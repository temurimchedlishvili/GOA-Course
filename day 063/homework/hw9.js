// გადააქცევს სტრინგს რიცხვად
let str1 = "42";
let num1 = Number(str1);
console.log(num1); // 42 (number)

// გადააქცევს სტრინგს მთელ რიცხვად
let str2 = "123.45";
let num2 = parseInt(str2);
console.log(num2); // 123 (integer)

// გადააქცევს სტრინგს ათწილად რიცხვად
let str3 = "123.45";
let num3 = parseFloat(str3);
console.log(num3); // 123.45 (float)

// სტრინგის წინ პლიუსის დადებით გადაიქცევა რიცხვად
let str4 = "77";
let num4 = +str4;
console.log(num4); // 77 (number)

// სტრინგის რიცხვი რომ გავამრავლოთ 1-ზე, გადაიქცევა number-ად
let str5 = "50";
let num5 = str5