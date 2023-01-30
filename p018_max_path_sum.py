from array import *

ARR = [
    [75],
    [95,64],
    [17,47,82],
    [18,35,87,10],
    [20,4,82,47,65],
    [19,1,23,75,3,34],
    [88,2,77,73,7,63,67],
    [99,65,4,28,6,16,70,92],
    [41,41,26,56,83,40,80,70,33],
    [41,48,72,33,47,32,37,16,94,29],
    [53,71,44,65,25,43,91,52,97,51,14],
    [70,11,33,28,77,73,17,78,39,68,17,57],
    [91,71,52,38,17,14,91,43,58,50,27,29,48],
    [63,66,4,68,89,53,67,30,73,16,69,87,40,31],
    [4,62,98,27,23,9,70,98,73,93,38,53,60,4,23]
]

def get_route_sum(node, graph, route_sum):
    global routes, max_sum, route_sums
    if not graph[node]: # end of the tree, i.e. dead-end of the graph
        routes += 1
        route_sum += ARR[node[0]][node[1]]
        print(f'route_sum={route_sum}; max_sum={max_sum}; node={node}')
        max_sum = max(route_sum, max_sum)
        route_sums.append(route_sum)
        return

    # Traverse to each adjacent node of a node
    # Note: this only works because we know the nature of the graph has no routes in circles
    for child in graph[node]:
        get_route_sum(child, graph, route_sum + ARR[node[0]][node[1]])  # Call the function recursively

if __name__ == "__main__":

    i_idx = j_idx = 0
    graph = {}
    global routes
    global max_sum
    global route_sums

    routes = max_sum = 0
    route_sums = []

    # Populate the graph
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
    node = (0,0)  # Starting node
    route_sum = 0
    get_route_sum(node, graph, route_sum)  # Traverse to each node of a graph
    print(f"Following is the Depth-first search size: {routes}; {max_sum}")
