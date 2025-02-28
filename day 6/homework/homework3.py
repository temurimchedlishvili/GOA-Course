attempts = 0  # მცდელობების მთვლელი
while attempts < 3:
    num = int(input("please input a number: "))  # მომხმარებელი შეიყვანს რიცხვს

    if num != 1:  # თუ შეყვანილი რიცხვი 1 არ არის, გადავიდეთ მთავარი ლოგიკის შესრულებაზე
        count = 0
        for i in range(2, num):
            if num % i == 0 and count == 0:
                print("Your number is not a prime")
                count += 1
        if count == 0:
            print("Your number is a prime")
        break  # სწორი რიცხვის შეყვანის შემდეგ ვწყვეტთ ციკლს
    else:
        print("try another number")  # თუ მომხმარებელმა შეიყვანა 1, სთხოვს ხელახლა შეყვანას
        attempts += 1  # მცდელობების რაოდენობის გაზრდა

if attempts == 3:
    print("Too many incorrect attempts. Exiting...")