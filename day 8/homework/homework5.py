import random

# შემთხვევითი რიცხვების თანმიმდევრობის შექმნა
sequence = [random.randint(1, 9) for _ in range(4)]

print("გამოიცანით 4-ნიშნა რიცხვების თანმიმდევრობა (1-9).")

while True:
    # მომხმარებლის შეყვანის მიღება
    guess = input("შეიყვანეთ 4 რიცხვი (გამოსაყოფად გამოიყენეთ დაშორება): ")
    
    # შეყვანილი სტრიქონის დამუშავება
    guess_list = guess.split()
    
    # თუ მომხმარებელმა არ შეიყვანა სწორ ფორმატში
    if len(guess_list) != 4 or not all(i.isdigit() for i in guess_list):
        print("გთხოვთ, შეიყვანოთ 4 ციფრი დაშორებით!")
        continue
    
    # რიცხვების გადაყვანა int-ებში
    guess_numbers = list(map(int, guess_list))
    
    # თუ მომხმარებელმა გამოიცნო
    if guess_numbers == sequence:
        print("გილოცავთ! თქვენ გამოიცანით სწორი თანმიმდევრობა:", sequence)
        break
    else:
        print("არასწორია! სცადეთ კიდევ ერთხელ.")

