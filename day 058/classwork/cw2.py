def check_number(num):
    if num > 0:
        return "დადებითი"
    elif num < 0:
        return "უარყოფითი"
    else:
        return "ნულოვანი"

# მაგალითი
# print(check_number(5))   # დადებითი
# print(check_number(-3))  # უარყოფითი
# print(check_number(0))   # ნულოვანი