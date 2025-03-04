# მომხმარებლისგან რიცხვის მიღება
number = int(input("შეიყვანეთ რიცხვი: "))

# გამყოფების პოვნა
divisors = []
for i in range(1, number + 1):
    if number % i == 0:
        divisors.append(i)

# გამყოფების ჩვენება
print(f"{number} რიცხვის გამყოფები: {divisors}")
