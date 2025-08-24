l1 = [1, 2, 3, 6, 9, 12, 15, 18, 20, 26, 27, 35, 19]

def l(list):
    l2 = []
    for i in list:
        if i % 3 != 0:
            l2.append(i)

    return l2

print(l(l1))