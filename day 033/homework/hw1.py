# 1. შექმენით manual split ფუნქცია.
def manual_split(what, split_item):
    x_list = []
    x_str = ""

    for i in what:
        if i == split_item:
            continue
        else:
            x_list.append(i)
            x_str += i

    return f"{x_list}, {x_str}"


print(manual_split("z-d-r-o-g-o-r-x-a-r", "-"))