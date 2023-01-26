import inflect

def number_letter_count(n):
    p = inflect.engine()
    sum = 0
    for i in range(1, n+1):
        number_words = p.number_to_words(i)
        print(f'number_words = {number_words}, ord(i) = {ord(number_words)}')
        letter_count = len(number_words.translate({ord(i): None for i in ' ,-'}))
        print(f'length = {letter_count}')
        sum += letter_count
    return sum

print(f'number_letter_count = {number_letter_count(1000)}')