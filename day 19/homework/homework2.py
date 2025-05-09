l1 = [1, 2, 3, 4, 5]
l2 = [6, 7, 8, 9, 10]

def l(list1, list2):
    ls1 = sum(list1)
    ls2 = sum(list2)

    if ls1 > ls2:
        return ls1
    else:
        return ls2

print(l(l1, l2))