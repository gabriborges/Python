import heapq
import networkx as nx
import matplotlib.pyplot as plt

def prim(graph, start):
    visited = set()
    min_heap = [(0, start)]
    mst_cost = 0
    mst_edges = []

    while min_heap:
        cost, node = heapq.heappop(min_heap)

        if node not in visited:
            visited.add(node)
            mst_cost += cost

            for neighbor, neighbor_cost in graph[node]:
                if neighbor not in visited:
                    heapq.heappush(min_heap, (neighbor_cost, neighbor))
                    mst_edges.append((node, neighbor))

    return mst_cost, mst_edges



graph = {
    'A': [('B', 4), ('H', 8)],
    'B': [('A', 4), ('C', 8), ('H', 11)],
    'C': [('B', 8), ('D', 7), ('F', 4), ('I', 2)],
    'D': [('C', 7), ('E', 9), ('F', 14)],
    'E': [('D', 9), ('F', 10)],
    'F': [('C', 4), ('D', 14), ('E', 10), ('G', 2)],
    'G': [('F', 2), ('H', 1), ('I', 6)],
    'H': [('A', 8), ('B', 11), ('G', 1), ('I', 7)],
    'I': [('C', 2), ('G', 6), ('H', 7)]
}

start_node = 'A'

mst_cost, mst_edges = prim(graph, start_node)

print("-- Minimum Spanning Tree --")
print("Total Cost:", mst_cost)
print("Edges:")
for edge in mst_edges:
    print(edge)

