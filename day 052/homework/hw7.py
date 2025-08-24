num = int(input("შეიყვანე დეციმალური რიცხვი: "))

binary = ""
n = num
while n > 0:
    binary = str(n % 2) + binary
    n //= 2

print("ბინარული ჩანაწერი არის:", binary)
