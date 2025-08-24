import random

secret = random.randint(1, 100)

print("გამოიცანი რიცხვი 1-დან 100-მდე 🎯")

while True:
    guess = int(input("შეიყვანე შენი ვარაუდი: "))
    
    if guess < secret:
        print("🔼 მეტია")
    elif guess > secret:
        print("🔽 ნაკლებია")
    else:
        print("🎉 სწორია! გამოიცანი რიცხვი:", secret)
        break
