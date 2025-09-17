def digit_sum(number):
    total = 0
    for digit in str(abs(number)):  # abs რომ უარყოფითიც იმუშაოს
        total += int(digit)
    return total

# მაგალითი
print(digit_sum(1234))  # → 10
print(digit_sum(-567))  # → 18
