def unique_numbers(lst):
    result = []
    for num in lst:
        if lst.count(num) == 1:   # თუ რიცხვი მხოლოდ ერთხელაა სიაში
            result.append(num)
    return result