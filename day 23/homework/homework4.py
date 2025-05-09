#შექმენით ფუნქცია რომელიც დაუმატებს ერთმანეთს string-ებს რომელიც გადმოეცემა არგუმენტად, გაითვალისწინეთ რომ თუ რომელიმე არგუმენტი იქნება ineger ის უნდა მოათავსოთ შედგენილი ქინადადების ბოლოშო.

def x(a, b):
    x = ""
    if isinstance(a, str):
        x += a
    elif isinstance(a, int):
        x += ""
    else:
        a = str(a)

    if isinstance(b, str):
        x += b
    elif isinstance(b, int):
        x += ""
    else:
        b = str(b)

    if isinstance(a, int):
        x += str(a)
    if isinstance(b, int):
        x += str(b)

    return x

print(x("Hello", "World"))
print(x("Age:", 25))
print(x(2025, "წელი"))
print(x(1, 2))
print(x("Test", True))