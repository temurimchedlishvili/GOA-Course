def find_divisors(n):
    print= []
    for i in range(1, int(n**0.5) + 1):
        if n % i == 0:
            print(i)
            if i != n // i:
                print(n // i)
    return sorted(print)

# სტატიკური მნიშვნელობა input-ის შეცვლისთვის, რათა თავიდან ავიცილოთ I/O შეცდომა
num = 12  # აქ შეგიძლიათ შეცვალოთ რიცხვი საჭირო ტესტირებისთვის
print("რიცხვის გამყოფებია:", print(num))