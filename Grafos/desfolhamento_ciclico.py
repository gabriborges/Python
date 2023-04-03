import networkx as gp
import os
os.system('cls')

def centro_grafo(G):
    # copia do grafo
    grafo = G.copy()
    
    # grau de cada nó
    graus_vertices = dict(grafo.degree())

    #Contadores
    i=0
    j=1
    # quais são as folhas
    
    folhas = [vertice for vertice in grafo.nodes() if graus_vertices[vertice] == 1]

    # remove as folhas até que restem 1 ou 2 vertices
    num_vertices = len(grafo.nodes())
    controlador_iterações = len(grafo.nodes())
    
    print(f'Grafo Inicial com seus vertices e graus: {graus_vertices}')
    print(f'Folhas (Interação {j}): {folhas}')
    
    while num_vertices > 2:

        grafo.remove_nodes_from(folhas)

        graus_vertices = dict(grafo.degree())
        folhas = [vertice for vertice in grafo.nodes() if graus_vertices[vertice] == 1]
        
        num_vertices = len(grafo.nodes())

        if len(folhas)==0:
            print('Folhas vazias, não há nenhuma folha a ser retirada mais.')
            return list(grafo.nodes())
        i+=1
        j+=1
        print(f'Cada vertice com seu grau (Retirada de folha: {i}): {graus_vertices}')
        print(f'Folhas (Interação {j}): {folhas}')
    
    # retorna o centro
    return list(grafo.nodes())

#lista_conexoes = [(1,2),(2,3),(3,4),(4,5),(4,6),(6,7)]
lista_conexoes = [(1,2),(2,3),(1,3),(1,4)]
lista_conexoes = [(1,2),(2,3),(3,4),(1,4),(4,5)]

Grafo = gp.Graph()
Grafo.add_edges_from(lista_conexoes)
Centro = centro_grafo(Grafo)


if len(Centro)==2:
    print ("Centro: {0}, {1}".format(min(Centro),max(Centro)))
else:
    print('Centro: ', Centro)