def divisors(n):
    result = []
    for i in range(1, n + 1):
        if n % i == 0:
            result.append(i)
    return result

num = int(input("შეიყვანე რიცხვი: "))
print(f"{num}-ის გამყოფები არიან:", divisors(num))
