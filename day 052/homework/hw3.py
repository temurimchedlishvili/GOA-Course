def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

num = int(input("შეიყვანე რიცხვი: "))

print(f"{num}! =", factorial(num))