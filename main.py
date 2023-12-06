if __name__ == '__main__':
    from utils import read_json, key_converter
    from traveling_salesman import traveling_salesman
    import networkx as nx
    import matplotlib.pyplot as plt


    path = 'graph1.json'
    graph = read_json(path)
    graph = key_converter(graph)

    vertices = list(graph.keys())

    smallest_route, total_distance = traveling_salesman(graph)
    print("Menor caminho:", smallest_route)
    print("Distância percorrida:", total_distance)

    G = nx.Graph()

    G.add_nodes_from(vertices)
    position = nx.spring_layout(G)  # Posicionamento dos vértices

    edges = []
    edges_labels = {}

    for external_key, values in graph.items():
        for internal_key, distance in values.items():
            if (external_key, internal_key) in edges or (internal_key, external_key) in edges:
                continue
            edges.append((external_key, internal_key))
            edges_labels[(external_key, internal_key)] = distance
    print(edges)
    
    best_path_edges = []
    for i in range(len(smallest_route) - 1):
        if (smallest_route[i], smallest_route[i + 1]) in best_path_edges or (smallest_route[i + 1], smallest_route[i]) in best_path_edges:
            continue
        best_path_edges.append((smallest_route[i], smallest_route[i + 1]))

        # Quando estiver no último elemento
        if i + 1 == len(smallest_route) - 1:
            best_path_edges.append((smallest_route[-1], smallest_route[0]))
    print(best_path_edges)
    
    G.add_edges_from(edges)

    nx.draw(G, position, with_labels=True, node_color='lightblue', font_weight='bold')

    nx.draw_networkx_edges(G, position, edgelist=best_path_edges, edge_color='red', width=3)
    
    nx.draw_networkx_edge_labels(G, position, edge_labels=edges_labels)

    plt.title('Grafo')
    plt.show()

