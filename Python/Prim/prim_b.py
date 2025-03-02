from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph):
    visited = set()
    pq = PriorityQueue()
    start_vertex = list(graph.keys())[0]
    visited.add(start_vertex)

    for vertex, weight in graph[start_vertex].items():
        pq.put((weight, start_vertex, vertex))

    mst = []
    while not pq.empty():
        weight, frm, to = pq.get() #minimum edge base on the weight
        if to not in visited:
            visited.add(to)
            mst.append((frm, to, weight))
            for vertex, weight in graph[to].items():
                if vertex not in visited:
                    pq.put((weight, to, vertex))

    return mst

old_graph = {
    'A': {'B': 4, 'H': 8},
    'B': {'A': 4, 'C': 8, 'H': 11},
    'C': {'B': 8, 'D': 7, 'F': 4, 'I': 2},
    'D': {'C': 7, 'E': 9, 'F': 14},
    'E': {'D': 9, 'F': 10},
    'F': {'C': 4, 'D': 14, 'E': 10, 'G': 2},
    'G': {'F': 2, 'H': 1, 'I': 6},
    'H': {'A': 8, 'B': 11, 'G': 1, 'I': 7},
    'I': {'C': 2, 'G': 6, 'H': 7}
}

graph = prim(old_graph)
print(graph)


# Create an empty graph

# Add edges with weights
def vizualizarGrafo():
    G = nx.Graph()

    for edge in graph:
        node1, node2, weight = edge
        G.add_edge(node1, node2, weight=weight)

    # Draw the graph
    pos = nx.spring_layout(G)  # Positions nodes using the Fruchterman-Reingold force-directed algorithm
    nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')

    # Draw edge weights
    edge_labels = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    # Show the graph
    plt.axis('off')
    plt.show()

vizualizarGrafo()

# #---------------------------------------------



# # Create an empty graph
# G = nx.Graph()

# # Add nodes
# G.add_nodes_from(graph.keys())

# # Add edges
# for node, edges in graph.items():
#     for neighbor, weight in edges.items():
#         G.add_edge(node, neighbor, weight=weight)

# # Draw the graph
# pos = nx.spring_layout(G)  # Positions nodes using the Fruchterman-Reingold force-directed algorithm
# nx.draw(G, pos, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')

# # Draw edge weights
# edge_labels = nx.get_edge_attributes(G, 'weight')
# nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

# # Show the graph
# plt.axis('off')
# plt.show()
