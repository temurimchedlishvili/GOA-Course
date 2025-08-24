#შექმენით ფუნქცია სადაც მომხარებელი გასაცემს ასევე ორ არგუმენტს, თქვენი დავალებაა რომ უფრო დიდი რიცხვი გაყოთ უფრო პატარაზე (ასევე არ იცით რა მონაცმეთა ტიპია), თუ გამყოფი აღმოჩნდება 0 გამოიტანეთ ZeroDivissionError

def x(one, two):
    one = float(one)
    two = float(two)

    if one == 0 or two == 0:
        return "ZeroDivissionError"
    elif one < two:
        return two / one
    elif one > two:
        return one / two

print(x(10, 5))
print(x("3.0", 6))
print(x(True, "10"))
print(x(0, 5))
print(x(5, 0))