car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}

graph = {
        'A': {'B': 2, 'c': 3},
        'B': {'D': 5, 'E': 4}
        }

x = graph['A'].keys()
y = graph['A'].items()
z = graph['A'].values()

for vertex, weight in graph['A'].items():
        print(f'Vertex: {vertex}, Weight: {weight}')


#print(x)
print(y)
#print(z)