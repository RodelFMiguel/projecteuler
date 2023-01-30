from itertools import permutations

a = '0123456789'
p = permutations(a)

idx = 1
for j in list(p):
    if idx == 1000000:
        print(j)
    idx += 1