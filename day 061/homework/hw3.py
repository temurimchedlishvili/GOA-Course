import random

# კომპიუტერი ირჩევს შემთხვევით რიცხვს 1-დან 10-მდე
secret_number = random.randint(1, 10)
hearts = 5  # მცდელობების რაოდენობა

print("გამოიცანი რიცხვი 1-დან 10-მდე! გაქვს", hearts, "ცდა.")

while hearts > 0:
    guess = int(input("შეიყვანე რიცხვი: "))

    if guess == secret_number:
        print("🎉 სწორია! გილოცავ!")
        break
    else:
        hearts -= 1
        if hearts > 0:
            print("❌ არასწორია! დაგრჩა", hearts, "ცდა.")
        else:
            print("თამაში დამთავრდა 😢. სწორი რიცხვი იყო:", secret_number)
