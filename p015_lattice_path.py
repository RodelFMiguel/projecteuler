import math

def lattice_path(n):
    n_fact = math.factorial(n)
    return math.factorial(2*n) / n_fact / n_fact

no_of_paths = lattice_path(20)
print(f'No of paths is {no_of_paths}')