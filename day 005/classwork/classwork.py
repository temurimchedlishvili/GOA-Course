for i in range(2,25):
    if i%2 ==1:
        print(i)

#classwork 2

user_name = str(input("enter name"))
for i in user_name:
    print(i)


#classwork 3

correct_password = "your_password_here"

# მომხმარებლისგან პაროლის მიღება
user_password = input("gtxovt shemoitanot paroli")

# პაროლის შედარება
while user_password != correct_password:
    print("paroli arasworia")
    user_password = input("gtxovt sheitanot paroli ")

print("tqveni paroli sworia!")