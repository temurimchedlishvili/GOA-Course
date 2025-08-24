l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def l(list):
    l2 = []

    for i in list:
        l2.append(i*2)

    return l2

print(l(l1))
