# 4. შექმენით ფუნქცია, რომელსაც გადაეცემა list, 
# თუ ამ ლისტში არის ყველა integer და ერთი string 
# ან სხვა ნებისმიერი data type, თქვენ უნდა დააბრუნოით 
# იგივე list განსხვავებული data type-ის გარეშე.

mylist = [1, 3, 5, 7, "string"]

def cl(x):
    new_list = []
    for i in x:
        if type(i) != int:
            continue
        else:
            new_list.append(i)
    return new_list

print(cl(mylist))