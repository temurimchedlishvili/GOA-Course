# მომხმარებელს შეაქვს სტრინგი
user_input = input("shemoiyvanet stringi: ")

# ცარიელი სტრიქონი, სადაც შევინახავთ ამოტრიალებულ სტრინგს
reversed_string = ""

# for ციკლი, რომელიც გადის სტრინგის სიმბოლოებზე უკუღმა
for char in user_input:
    reversed_string = char + reversed_string

# შედეგის გამოყვანა
print("shemotrialebuli stringi:", reversed_string)