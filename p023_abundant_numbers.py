def d(n):
    divisors = [1]
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            divisors.extend([i, n // i])
    if int(n ** 0.5) ** 2 == n:
        divisors.remove(int(n ** 0.5))
    return sum(divisors)

def abundant_numbers(limit):
    abundant_numbers = []
    for n in range(12, limit):
        if d(n) > n:
            abundant_numbers.append(n)
    return abundant_numbers

def sum_of_two_abundant_numbers(limit, abundant_numbers):
    abundant_sums = set()
    for i in range(len(abundant_numbers)):
        for j in range(i, len(abundant_numbers)):
            abundant_sum = abundant_numbers[i] + abundant_numbers[j]
            if abundant_sum > limit:
                break
            abundant_sums.add(abundant_sum)
    return abundant_sums

def non_abundant_sums(limit):
    abundant_numbers_list = abundant_numbers(limit)
    abundant_sums = sum_of_two_abundant_numbers(limit, abundant_numbers_list)
    return sum(set(range(1, limit)) - abundant_sums)

print(non_abundant_sums(28123))
