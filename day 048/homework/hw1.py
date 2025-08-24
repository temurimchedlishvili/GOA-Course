numbers = [1, 2, 3, 2, 4, 5, 6, 1, 7, 3, 8, 9, 5]

duplicates = []

for num in numbers:
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

print("გამეორებული რიცხვები:", duplicates)
