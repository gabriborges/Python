from Grafo import GrafoListaAdj

G = GrafoListaAdj()

G.DefinirN(4)

e = G.AdicionarAresta(1,2)
e.custo = 3

e = G.AdicionarAresta(2,3)
e.custo = 1

e = G.AdicionarAresta(1,3)
e.custo = 2

e = G.AdicionarAresta(1,4)
e.custo = 4

for v in G.V():
    for no in G.N(v, IterarSobreNo=True):
        u = no.Viz
        print((v,u, no.e.custo))

