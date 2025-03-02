from Grafo import GrafoListaAdj

def LerGrafosTeste():
    # Itera sobre 4 diferentes grafos
    for num in range(1,5):
        
        # Define as arestas de cada grafo
        if num == 1:
            E = [(1,2),(2,3),(3,4),(3,5),(2,6),(6,7),(7,8),(7,9),(6,10),(10,11),(10,12),(10,13)]
        elif num == 2:
            E = [(1,5),(5,6),(2,6),(6,7),(3,7),(7,4)]
        elif num == 3:
            E = [(1,2),(2,3),(3,4),(4,5)]
        else:
            E = [(1,2),(2,3),(3,4),(3,5),(3,6),(2,9),(9,10),(2,7),(7,8),(8,11),(8,12),(8,13)]
        
        # Cria um grafo não-orientado com lista de adjacências, e define o tamanho do grafo
        T = GrafoListaAdj(orientado=False)
        T.DefinirN(len(E)+1,VizinhancaDuplamenteLigada=True)
        
        # Adiciona cada aresta ao grafo
        for (u,v) in E:
            T.AdicionarAresta(u,v)
        
        # Retorna o grafo criado
        yield (T)


def CentroArvore(T):
    # Se o grafo tem apenas um nó, retorna ele mesmo como o centro
    if T.n == 1:
        return [1]

    # Inicializa o vetor de graus de cada nó
    d = [0]*(T.n+1)

    # Calcula o grau de cada nó
    for (u,v) in T.E():
        d[u]=d[u]+1;d[v]=d[v]+1

    # Identifica os nós folha
    F = [ v for v in T.V() if d[v]==1 ]

    # Repete até que haja apenas dois nós restantes
    n = T.n
    while n > 2:
        
        # Inicializa a lista de folhas para a próxima iteração
        Flin = []
        
        # Remove as folhas e atualiza os graus dos nós adjacentes
        for f in F:
            v_no = next(T.N(f,IterarSobreNo=True)) # por ser folha, tem apenas um vizinho		
            v = v_no.Viz
            d[v]=d[v]-1; n=n-1; T.RemoverAresta(v_no.e) 
            if d[v] == 1:
                Flin.append(v)
        
        # Define as novas folhas
        F = Flin

    # Retorna o(s) nó(s) central(is)
    return F

for T in LerGrafosTeste():
	C = CentroArvore(T)
	if len(C)==2:
		print ("{0}, {1}".format(min(C),max(C)))
	else:
		print(C[0])