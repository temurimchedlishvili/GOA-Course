# 1. "გადათარგმნეთ" ფსევდო კოდი Python-ზე.

user = {
    "login": "Temuri",
    "password": "Temuri2005"
}

start = True
while start == True:
    login = input("enter login: ") # შეიყვანეთ მომხმარებელი
    password = input("enter password: ") # შეიყვანეთ პაროლი

    if login != user["login"] and password != user["password"]:
        print("თქვენი ავტორიზაციის ინფორმაცია არასწორია სცადეთ ახლიდან!")
    else:
        if login == user["login"] and password == user["password"]:
            print("თქვენ ავტორიზაცია წარმატებით გაიარეთ!")
            break