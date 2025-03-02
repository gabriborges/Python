
# ​Autoria:
#     Fabiano S. Oliveira
#     Paulo E. D. Pinto
#
# ​A correção e a análise de complexidade deste programa
# encontram-se no livro
#
# Teoria Computacional de Grafos, Elsevier, 2018
# ​    ​Jayme L. Szwarcfiter

#Algoritmo 2.1: Determinação do centro de uma árvore

from Grafo import GrafoListaAdj



E = [(1,2),(2,3),(3,4),(4,5),(4,6),(6,7)]


T = GrafoListaAdj(orientado=False)
T.DefinirN(len(E)+1,VizinhancaDuplamenteLigada=True)
for (u,v) in E:
	T.AdicionarAresta(u,v)
			

#Dados: árvore T
def CentroArvore(T):
	if T.n == 1:
		return [1]
	d = [0]*(T.n+1)
	n = T.n
	for (u,v) in T.E():
		d[u]=d[u]+1;d[v]=d[v]+1
	F = [ v for v in T.V() if d[v]==1 ]

	while n > 2:
		Flin = []
		for f in F:
			v_no = next(T.N(f,IterarSobreNo=True)) #por ser folha, tem apenas um vizinho		
			v = v_no.Viz
			d[v]=d[v]-1; n=n-1; T.RemoverAresta(v_no.e) 
			if d[v] == 1:
				Flin.append(v)
		F = Flin

	return F


C = CentroArvore(T)
if len(C)==2:
	print ("{0}, {1}".format(min(C),max(C)))
else:
	print(C[0])

