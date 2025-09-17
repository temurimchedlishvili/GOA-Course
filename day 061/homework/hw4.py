import random

# შესაძლო არჩევანები
choices = ["ქვა", "ქაღალდი", "მაკრატელი"]

# კომპიუტერი შემთხვევით ირჩევს ერთს
computer = random.choice(choices)

# მომხმარებლის არჩევანი
player = input("აირჩიე: ქვა, ქაღალდი, მაკრატელი → ")

print("კომპიუტერი:", computer)
print("მომხმარებელი:", player)

# შედეგის დადგენა
if player == computer:
    print("ფრე 🤝")
elif (player == "ქვა" and computer == "მაკრატელი") or \
    (player == "ქაღალდი" and computer == "ქვა") or \
    (player == "მაკრატელი" and computer == "ქაღალდი"):
    print("გაიმარჯვე 🎉")
else:
    print("კომპიუტერმა მოიგო 😢")
