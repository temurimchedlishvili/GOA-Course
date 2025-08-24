numbers = [] 

for i in range(5):
    num = float(input(f"შეიყვანე {i+1}-ე რიცხვი: "))
    numbers.append(num)

total = sum(numbers)

average = total / len(numbers)

print("რიცხვების ჯამი არის:", total)
print("რიცხვების საშუალო არის:", average)