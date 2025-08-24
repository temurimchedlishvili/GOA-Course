l1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, -6, -10, -7, -8, -5]

def l(list):
    l2 = []
    l3 = []

    for i in list:
        if i > 0:
            l2.append(i)
        elif i < 0:
            l3.append(i)

    li2 = sum(l2)
    li3 = sum(l3)

    return li2, li3

print(l(l1))