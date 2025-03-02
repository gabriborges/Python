from queue import PriorityQueue
import networkx as nx
import matplotlib.pyplot as plt


def prim(grafo):
    visitados = set()
    fila = PriorityQueue()
    vertice_inicial = list(grafo.keys())[0]
    visitados.add(vertice_inicial)

    for vertice, peso, in grafo[vertice_inicial].items():
        fila.put((peso, vertice_inicial, vertice))
    
    mst = []
    while not fila.empty():
        peso, vertice_origem, proximo_vertice = fila.get()
        if proximo_vertice not in visitados:
            visitados.add(proximo_vertice)
            mst.append((vertice_origem, proximo_vertice, peso))
            for vertice, peso in grafo[proximo_vertice].items():
                if vertice not in visitados:
                    fila.put((peso, proximo_vertice, vertice_origem))
    
    return mst

grafo = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3},
    'C': {'B': 3},
    'D': {'A': 1}
}

grafo2 = {
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

#mst_grafo = prim(grafo)
mst_grafo2 = prim(grafo2)
#print(mst_grafo)
print(mst_grafo2)

def vizualizarGrafo(Grafo):
    G = nx.Graph()

    for aresta in Grafo:
        no1, no2, peso = aresta
        G.add_edge(no1, no2, weight=peso)
    
    posicionamento = nx.spring_layout(G)
    nx.draw(G, posicionamento, with_labels=True, node_size=500, node_color='lightblue', font_size=12, font_weight='bold', edge_color='gray')

    rotulo_aresta = nx.get_edge_attributes(G, 'weight')
    nx.draw_networkx_edge_labels(G, posicionamento, edge_labels=rotulo_aresta)

    plt.axis('off')
    plt.show()

#vizualizarGrafo(mst_grafo)
vizualizarGrafo(mst_grafo2)