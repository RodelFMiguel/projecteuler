def get_sum_of_digits(n):
    sum = 0
    for digit in str(n):
        sum += int(digit)
    return sum

sum_of_digits = get_sum_of_digits(2**1000)
print(f'Sum of 2^1000 is {sum_of_digits}')