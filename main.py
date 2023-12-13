if __name__ == '__main__':
    from utils import read_json, key_converter
    from traveling_salesman import traveling_salesman
    from draw_interface import draw_interface

    path = 'graph1.json'
    graph = read_json(path)
    graph = key_converter(graph)

    vertices = list(graph.keys())

    smallest_route, total_distance = traveling_salesman(graph)
    print("Menor caminho:", smallest_route)
    print("Distância percorrida:", total_distance)

    draw_interface(vertices, graph, smallest_route)
