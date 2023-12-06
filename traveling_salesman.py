import itertools


def calculate_distance(route, graph):
    distance = 0
    for i in range(len(route) - 1):
        # Verifica se o vertice atual tem ligação com o próximo
        if route[i + 1] not in graph[route[i]]:
            return float('inf')
        distance += graph[route[i]][route[i + 1]]

    # Verifica se o último elemento tem ligação com o primeiro
    if route[0] not in graph[route[-1]]:
        return float('inf')
    distance += graph[route[-1]][route[0]]
    return distance

def traveling_salesman(graph):
    vertices = list(graph.keys())
    smallest_distance = float('inf')
    smallest_route = []

    for permutation in itertools.permutations(vertices):
        if permutation[0] != 1:
            continue
        # print(permutation )
        distance = calculate_distance(permutation, graph)
        if distance < smallest_distance:
            smallest_distance = distance
            smallest_route = list(permutation)

    return smallest_route, smallest_distance