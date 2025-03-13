# მომხმარებელი შეყავს რიცხვი
num = int(input("shemoiyvanet ricxvi: "))

print(f"{num}-is gamyofebi:")

# for ციკლი 1-დან შეყვანილ რიცხვამდე
for i in range(1, num + 1):
    if num % i == 0:  # თუ num უნაშთოდ იყოფა i-ზე
        print(i)