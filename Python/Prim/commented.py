from queue import PriorityQueue

def prim(graph):
    visited = set()  # Set to keep track of visited vertices
    pq = PriorityQueue()  # Priority queue to store edges with their weights
    start_vertex = list(graph.keys())[0]  # Selecting the first vertex as the starting point
    visited.add(start_vertex)  # Mark the start_vertex as visited

    # Adding edges from the start_vertex to the priority queue
    for vertex, weight in graph[start_vertex].items():
        pq.put((weight, start_vertex, vertex))

    mst = []  # List to store the minimum spanning tree edges
    while not pq.empty():  # Continue until the priority queue is empty
        weight, frm, to = pq.get()  # Get the edge with the minimum weight from the priority queue

        if to not in visited:  # If the destination vertex is not visited
            visited.add(to)  # Mark the destination vertex as visited
            mst.append((frm, to, weight))  # Add the edge to the minimum spanning tree list

            # Add edges from the newly visited vertex to the priority queue
            for vertex, weight in graph[to].items():
                if vertex not in visited:  # Add only the unvisited vertices to the priority queue
                    pq.put((weight, to, vertex))

    return mst

old_graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3},
    'C': {'B': 3},
    'D': {'A': 1}
}

graph = prim(old_graph)  # Compute the minimum spanning tree using Prim's algorithm
print(graph)  # Print the minimum spanning tree



#-----------------------------------------


graph = {
    'A': {'B': 2, 'D': 1},
    'B': {'A': 2, 'C': 3},
    'C': {'B': 3},
    'D': {'A': 1}
}