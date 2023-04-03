import networkx as gp
import os
os.system('cls')


def centro_grafo(G):
    # copia do grafo
    grafo = G.copy()
    
    # grau de cada nó
    graus_vertices = dict(grafo.degree())
    
    # quais são as folhas

    folhas = [vertice for vertice in grafo.nodes() if graus_vertices[vertice] == 1]
    
    # remove as folhas até que restem 1 ou 2 vertices
    num_vertices = len(grafo.nodes())
    controlador_iterações = len(grafo.nodes())
    i=0

    while num_vertices > 2:
        
        print(f'Cada vertice com seu grau (Retirada de folha: {i}): {graus_vertices}')

        grafo.remove_nodes_from(folhas)
        graus_vertices = dict(grafo.degree())
        folhas = [vertice for vertice in grafo.nodes() if graus_vertices[vertice] == 1]
        
        num_vertices = len(grafo.nodes())

        i+=1
        print(f'Folhas (Interação {i}): {folhas}')

        if i> controlador_iterações:
            print("O grafo está causando interações infinitas, o problema pode ser a existencia de ciclo(s).")
            quit()

        
    
    # retorna o centro
    return list(grafo.nodes())

lista_conexoes = [(1,2),(2,3),(3,4),(4,5),(4,6),(6,7)]
#lista_conexoes = [(1,2),(2,3),(1,3),(1,4)]

Grafo = gp.Graph()
Grafo.add_edges_from(lista_conexoes)
Centro = centro_grafo(Grafo)
if len(Centro)==2:
    print ("Centro: {0}, {1}".format(min(Centro),max(Centro)))
else:
    print('Centro: ', Centro[0])