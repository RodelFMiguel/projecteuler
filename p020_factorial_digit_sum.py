from math import factorial

def getSumOfDigits(number):
    sum = 0
    while number > 0:
        sum += number % 10
        number //= 10

    return sum

print(getSumOfDigits(int(factorial(100))))