
class Grafo:
    def __init__(self, num_vertices):
        self.num_vertices = num_vertices
        self.lista_adj = [[] for _ in range(num_vertices)]
        self.pesos = {}

    def adicionar_aresta(self, origem, destino, peso):
        self.lista_adj[origem].append(destino)
        print(f'Vertice {origem} ligado ao {destino}')
        self.lista_adj[destino].append(origem)
        print(f'Vertice {destino} ligado ao {origem}')
        self.pesos[(origem, destino)] = peso
        self.pesos[(destino, origem)] = peso

g = Grafo(5)
g.adicionar_aresta(0, 1, 1)
g.adicionar_aresta(1, 2)
g.adicionar_aresta(2, 3)
g.adicionar_aresta(3, 4)
g.adicionar_aresta(4, 0)