def get_fibo_iterations(limit):
    first = 0
    second = 1
    sum = 0
    iterations = 1

    while(1):
        sum = first + second
        first = second
        second = sum
        iterations += 1

        if len(str(sum)) >= limit:
            print(sum)
            return iterations


print(get_fibo_iterations(1000))