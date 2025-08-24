# 4. შექმენი სია numbers = [3, 7, 2, 9, 4, 1]. 
# გამოიყენე for ციკლი, რათა იპოვო ამ 
# სიაში მაქსიმალური რიცხვი (არ გამოიყენო max() ფუნქცია).

numbers = [3, 7, 2, 9, 4, 1] 

mx = numbers[0]

for i in range(1, len(numbers)):
    if numbers[i] > mx:
        mx = numbers[i]
print(mx) 