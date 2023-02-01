def recurring_cycle_length(n):
    remainders = []
    remainder = 10 % n
    while remainder not in remainders and remainder != 0:
        remainders.append(remainder)
        remainder = (remainder * 10) % n
    print(f'N={n}; remainder={remainder}; remainders={remainders}')
    return len(remainders) if remainder == 0 else len(remainders) - remainders.index(remainder)

def longest_recurring_cycle_length(limit):
    max_length = 0
    max_d = 0
    for d in range(2, limit):
        length = recurring_cycle_length(d)
        if length > max_length:
            max_length = length
            max_d = d
    return max_d

print(longest_recurring_cycle_length(1000))