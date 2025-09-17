# ფუნქცია, რომელიც ამოწმებს ლუწია თუ კენტი
def is_even(number):
    return number % 2 == 0

# მომხმარებელი შეიყვანს 3 რიცხვს
for i in range(3):
    num = int(input(f"შეიყვანე რიცხვი {i+1}: "))
    
    if is_even(num):
        print(f"Number {num} is even")
    else:
        print(f"Number {num} is odd")
