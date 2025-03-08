num = int(input("chaweret ricxvi 50-is chatvlit: "))
while num > 50 or num <1:
    print("tqveni ricxvi agemateba 50-s sheiyvanet ricxvi axlidan: ")
    num = int(input("chaweret ricxvi 50-is chatvlit: "))
for i in range(num,101):
    if i % num == 0:
        print(i)    