import numpy as np
import os
os.system('cls')

x='x'

#########################################################################

def calcularLinhas(matriz)->int:
        dimensoes=matriz.shape
        return dimensoes[0]

def calcularColunas(matriz)->int:
        dimensoes=matriz.shape
        return dimensoes[1]

def mostrarMatriz(matriz):
    linhas = calcularLinhas(matriz)
    colunas = calcularColunas(matriz)

    mostrarVariaveis(matriz)
    for linha in range(linhas):
        for coluna in range(colunas):
            print(f'{matriz[linha][coluna]}  ',end='')
        print()
    print()

def povoarMatriz_A(matriz):
    linhas = calcularLinhas(matriz)
    colunas = calcularColunas(matriz)

    i,j=0,0
    while i<linhas:
        for linha in range(linhas):
            for coluna in range(colunas):
                aux=float(input(f'Valor de {x+str(i+1)} na linha {j+1}: '))
                matriz[linha][coluna]=aux
                i+=1
            j+=1
            i=0
        break
    print()

def mostrarVariaveis(matriz):
    print()

    colunas = calcularColunas(matriz)
    i=0
    while i<colunas:
        print(f' {x+str(i+1)}  ',end='')   
        i+=1
    print()

def atualizarValoresFO(matrizCr, matrizCb, matrizB, matrizR):
    result = matrizCr-matrizCb*np.linalg.inv(matrizB)*matrizR
    return result

def definirValoresVariaveisBasicas(matrizB,matrizb):
    result = np.linalg.inv(matrizB)*matrizb

def calcularCoeficinetesNaoBasicos(matrizB,matrizR):
    result = np.linalg.inv(matrizB)*matrizR

def calcularResultadoFO(matrizcb, matrizB, matrizb):
    result = matrizcb*np.linalg.inv(matrizB)*matrizb

def Simplex():
    pass




##########################################################################



matriz_a= np.array([[5,20,1,0],
            [10,15,0,1],
            [-45,-80,0,0]])
matriz_b= np.array([[400],
            [450]])
matriz_c= np.array([-45,-80,0,0])

matriz_R= np.array([[3,6],
            [4,2]])
matriz_B= np.array([[1,0],
            [0,1]])
matriz_Cr= np.array([[-20,-24]])
matriz_Cb= np.array([[0,0]])

##############################################################################################


def divisão(matriza, matrizb, coluna):
    lista = []
    
    num=0
    for n in coluna:
        try:
            lista.append(matrizb[num][0]/n)
            num+=1
        except ZeroDivisionError:
            #se existir uma divisão por 0, então colocaremos no lugar o -1, visto que os dois seriam igualmente não considerados.
            lista.append(-1)
            num+=1
    k=0
    menor=lista[0]
    while k < len(lista):
        if lista[k]<0:
            k+=1
        else:
            menor=lista[k]
            break
    #print (menor)

    indice_menor=0
    for n in range(len(lista)):
        if lista[n]<=menor:
            if lista[n]<0:
                pass
            else:
                menor=lista[n]
            indice_menor=n
    #print(indice_menor)
    return indice_menor


def swapColuna(matriza, indice_menor, tamanho):
    coluna_nao_basica = matriza[:tamanho,indice_menor]

    indice_coluna_a_sair = divisão(matriza, matriz_b, coluna_nao_basica)

    print(indice_coluna_a_sair)

    temp = indice_coluna_a_sair
    temp_matriz_a = matriza
    coluna_a_sair=[]
    indice_determinante_alvo=0

    n=0
    while n < calcularColunas(matriza):
        
        if (matriza[indice_coluna_a_sair][n] == 1) and (matriza[indice_coluna_a_sair+1][n] == 0) and (matriza[-1][n] == 0):
            indice_determinante_alvo=n
            for t in range(calcularLinhas(matriza)):
                coluna_a_sair.append(matriz_a[t][n]) 
        
            for k in coluna_nao_basica:     
                        temp_matriz_a[temp][n] = k
                        temp+=1
      
        n+=1

    temp_matriz_a[-1][indice_determinante_alvo] = matriza[-1][indice_menor]
    
    n=0
    while n < calcularColunas(matriza)-1:
        for g in coluna_a_sair:
            temp_matriz_a[n][indice_menor] = g
            n+=1
    
    print(coluna_a_sair)
    print(temp_matriz_a)

def definirMenorNaFO(matriza):
    linha = calcularLinhas(matriza)-1
    menor = matriz_a[linha][0]
    indice_menor = 0
    for n in range(linha):
        if matriza[linha][n]<=menor:
            menor = matriza[linha][n]
            indice_menor = n

    swapColuna(matriza, indice_menor, linha)

definirMenorNaFO(matriz_a)
