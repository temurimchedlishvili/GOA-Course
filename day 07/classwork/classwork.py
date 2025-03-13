# classwork 1
text = input("შეიყვანეთ ტექსტი: ")
number = int(input("შეიყვანეთ რიცხვი: "))

if 0 <= number < len(text):
    print("number len(text):")
else:
    print("შეყვანილი რიცხვი არასწორია!")

# classwork 2
for i in range(100, 0, -1):
    print(i)

#classwork 3
# შექმნათ ციკლი 1-100-მდე რიცხვებისთვის
for i in range(1, 101):
    if i % 2 != 0:  # თუ რიცხვი კენტია
        print(i)

# classwork 4
# ციკლი 250-დან 500-მდე რიცხვებისთვის
for i in range(250, 501, 10):
    print(i)

# classwork 6
# მომხმარებლისგან რიცხვის შეყვანა
number = int(input("შეიყვანეთ რიცხვი: "))

# შემოწმება თუ რიცხვი ლუწია თუ კენტია
if number % 2 == 0:
    for _ in range(10):
        print("yes")
else:
    print("no")
    