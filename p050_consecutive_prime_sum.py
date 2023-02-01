import math

def is_prime(x):
    if x == 2:
        return True

    if x % 2 == 0:
        return False

    i = 3
    while i <= int(math.sqrt(x)):
        if x % i == 0:
            return False
        i += 2

    return True

def consecutive_primes(limit):
    primes = []
    for i in range(2, limit):
        if is_prime(i) == True:
            primes.append(i)
    return primes

def get_max_prime(limit):
    total = 0
    max_prime = 0
    max_range = 0

    prime_list = consecutive_primes(limit)

    for x in range(len(prime_list)):
        total = 0
        for y in range(x, len(prime_list)):
            total += prime_list[y]
            if total > limit:
                break
            if max_range < y-x and is_prime(total):
                max_prime = max(max_prime, total)
                max_range = y-x
                print(f'{max_prime}; {max_range}')
    
    return max_prime, max_range

print(get_max_prime(1000))