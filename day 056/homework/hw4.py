def even_odd_sort(lst):
    evens = [x for x in lst if x % 2 == 0]
    odds = [x for x in lst if x % 2 != 0]
    return evens + odds

# მაგალითი
numbers = [1, 2, 3, 4, 5, 6]
print(even_odd_sort(numbers))  # → [2, 4, 6, 1, 3, 5]
