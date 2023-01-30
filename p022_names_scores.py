import sys

def populate_list(filename):
    names_list = []
    with open(filename) as f:
        for line in f:
            list = [str(elt.strip('"')) for elt in line.split(',')]
            names_list.extend(list)
    return sorted(names_list)

def get_name_score(s):
    return sum((ord(c) - 64) for c in s)

if __name__ == "__main__":
    names_list = populate_list(sys.argv[1])
    
    total = 0
    idx = 1
    for name in names_list:
        name_score = get_name_score(name) * idx
        total += name_score
        print (f'name_score={name_score}; total={total}')
        idx += 1
