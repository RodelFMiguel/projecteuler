from array import *
import sys

# ARR = [
#     [75],
#     [95,64],
#     [17,47,82],
#     [18,35,87,10],
#     [20,4,82,47,65],
#     [19,1,23,75,3,34],
#     [88,2,77,73,7,63,67],
#     [99,65,4,28,6,16,70,92],
#     [41,41,26,56,83,40,80,70,33],
#     [41,48,72,33,47,32,37,16,94,29],
#     [53,71,44,65,25,43,91,52,97,51,14],
#     [70,11,33,28,77,73,17,78,39,68,17,57],
#     [91,71,52,38,17,14,91,43,58,50,27,29,48],
#     [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
#     [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
# ]

def populate_triangle(filename, ARR):
    with open(filename) as f:
        for line in f:
            inner_list = [int(elt.strip()) for elt in line.split(' ')]
            ARR.append(inner_list)

if __name__ == "__main__":

    i_idx = j_idx = 0
    graph = {}
    global routes
    global max_sum
    global route_sums

    routes = max_sum = 0
    route_sums = []
    ARR = []

    # Populate the graph
    populate_triangle(sys.argv[1], ARR)
    for i in ARR:
        for j in i:
            if i_idx < len(ARR)-1:
                graph[(i_idx, j_idx)] = [
                    (i_idx+1, j_idx),
                    (i_idx+1, j_idx+1)    
                ]
            else:
                graph[(i_idx, j_idx)] = []
            j_idx += 1
        j_idx = 0
        i_idx += 1

    print(graph)
    for i in range(len(ARR)-2, -1, -1):
        for j in range(len(ARR[i])):
            node = graph[(i,j)]
            print(f'i={i}; j={j}; node={node}; ARR[0]={ARR[node[0][0]][node[0][1]]} ARR[1]={ARR[node[1][0]][node[1][1]]}')
            if ARR[node[0][0]][node[0][1]] > ARR[node[1][0]][node[1][1]]:
                ARR[i][j] += ARR[node[0][0]][node[0][1]]
            else:
                ARR[i][j] += ARR[node[1][0]][node[1][1]]

    print(f'max sum = {ARR[0][0]}')


