import numpy as np
import warnings
import os
os.system('cls')

warnings.filterwarnings("error")
x='x'

#

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

def atualizarValoresLinhaFO(matrizCr, matrizCb, matrizB, matrizR):
    result = matrizCr - matrizCb @ np.linalg.inv(matrizB) @ matrizR
    return result

def definirValoresVariaveisBasicas(matrizB,matrizb):
    result = np.linalg.inv(matrizB)@matrizb
    return result

def calcularCoeficinetesNaoBasicos(matrizB,matrizR):
    result = np.linalg.inv(matrizB)@matrizR
    return result

def calcularResultadoFO(matrizcb, matrizB, matrizb):
    result = matrizcb@np.linalg.inv(matrizB)@matrizb
    return result






##########################################################################


'''
matriz_a= np.array([[3,6,1,0],
            [4,2,0,1],
            [-20,-24,0,0]], dtype='float')
matriz_b= np.array([[60],
            [32]], dtype='float')
matriz_c= np.array([-20,-24,0,0], dtype='float')

matriz_R= np.array([[3,6],
            [4,2]], dtype='float')
matriz_B= np.array([[1,0],
            [0,1]], dtype='float')

matriz_Cr= np.array([[-20,-24]], dtype='float')
matriz_Cb= np.array([[0,0]], dtype='float')

valor_FO = 0

old_matrizCb = matriz_Cb
'''

matriz_a= np.array([[5,20,1,0],
            [10,15,0,1],
            [-45,-80,0,0]], dtype='float')
matriz_b= np.array([[400],
            [450]], dtype='float')
matriz_c= np.array([-45,-80,0,0], dtype='float')

matriz_R= np.array([[5,20],
            [10,15]], dtype='float')
matriz_B= np.array([[1,0],
            [0,1]], dtype='float')


matriz_Cr= np.array([[-45,-80]])
matriz_Cb= np.array([[0,0]])

valor_FO = 0

old_matrizCb = matriz_Cb



##############################################################################################


def divisao(matrizA, matrizB, index_menor_valor):

    try:
        valor_divisao = matrizB[0, 0] / matrizA[0, index_menor_valor]
        index_menorRazao = 0
    except RuntimeWarning:
        valor_divisao = 0
        index_menorRazao = None

    for index in range(calcularLinhas(matrizA)-1):
        try:
            aux_valor_divisao = matrizB[index, 0] / matrizA[index, index_menor_valor]
            if aux_valor_divisao < valor_divisao:
                valor_divisao = aux_valor_divisao
                index_menorRazao = index
        except RuntimeWarning:
            pass
    if index_menorRazao == None:
        print("Não foi possivel encontrar nenhuma variavel para saida (Todas são negativas ou zero).")
        breakpoint()

    index_de_swap = indexDeSwap(matrizA, index_menorRazao)[0]

    return index_de_swap

def indexDeSwap(matriz, index)->int:

    index_swap = None
    #retorna os indexes onde há o valor 1
    index_1 = np.where(matriz[index,:] == 1)

    for i in index_1:
        matriz_temp = matriz_a[:,i]
        if (np.isin(matriz_temp, [0, 1]).all()) == True:
            index_swap = i
            return index_swap

def swapDeColuna(matriz, index1, index2):
    #realiza a troca das colunas
    matriz[:,[index1, index2]] = matriz[:,[index2, index1]]


def verificarIteracao(matriz, matrizB):

    index_menor_valor = matriz[-1, :].argmin()

    index_menor_razao = divisao(matriz, matrizB, index_menor_valor)
    
    swapDeColuna(matriz, index_menor_valor, index_menor_razao)

    separarMatrizes(matriz)
    
    verificarSolucaoOtima()
    
    
def verificarSolucaoOtima():

    valores = (atualizarValoresLinhaFO(matriz_Cr,matriz_Cb, matriz_B, matriz_R))
    
    if np.any(valores < 0)==True:

        rearranjoSimplex()
    else:
        
        finalizarSimplex()

def rearranjoSimplex():

    global matriz_b, valor_FO, old_matrizCb
    #atualizar valores das variaveis basicas

    temp_matriz_b = matriz_b
    matriz_b = definirValoresVariaveisBasicas(matriz_B, matriz_b)
    
    #clacular FO

    valor_FO += calcularResultadoFO(old_matrizCb, matriz_B, temp_matriz_b)[0]

    
    nova_matriz_R = calcularCoeficinetesNaoBasicos(matriz_B, matriz_R)
    #atualizando a linha da FO
    nova_linhaFO = atualizarValoresLinhaFO(matriz_Cr,matriz_Cb, matriz_B, matriz_R)
    j=0
    for i in range(matriz_c.shape[0]):
        if matriz_c[i]!= 0:
                matriz_c[i] = nova_linhaFO[j]
                j+=1

    #aqui
    atualizarMatrizA(nova_matriz_R)

def atualizarMatrizA(matrizR):
    global matriz_B, matriz_R, matriz_Cr, matriz_Cb, matriz_c, old_matrizCb, matriz_a, matriz_b

    aux_matriz_semFO = np.delete(matriz_a, [-1], axis=0)

    print(aux_matriz_semFO)
    j=0
    
    #aqui
    #fazer dois tipos de matrizes diferentes
    for i in range(calcularColunas(aux_matriz_semFO)):
        matriz_temp = matriz_a[:,i]
        if (np.isin(matriz_temp, [0, 1]).all()) == False:
                aux_matriz_semFO[:, i] = matrizR[:, j]
                j+=1


    aux_matriz_comFO = np.vstack((aux_matriz_semFO, matriz_c))

    separarMatrizes(aux_matriz_comFO)
    iniciarSimplex(matriz_a, matriz_b)


def finalizarSimplex():
    print('Resultado: ')
    print(definirValoresVariaveisBasicas(matriz_B, matriz_b))
    print('FO: ')
    print(calcularResultadoFO(matriz_Cb, matriz_B, matriz_b))


def separarMatrizes(matriz):

    global matriz_a, matriz_B, matriz_R, matriz_Cr, matriz_Cb, matriz_c, old_matrizCb

    matriz_c = matriz[-1,:]

    #retirada da linha da FO da matriz A
    aux_matriz_semFO = np.delete(matriz, [-1], axis=0)
    
    #split da matriz A, para dividir em duas matrizes
    matriz_R= np.split(aux_matriz_semFO,2, axis=1)[0]
    matriz_B= np.split(aux_matriz_semFO,2, axis=1)[1]
    
    matrizFO = matriz[-1,:]
    #split na linha da fo, para dividir em duas matrizes
    matriz_Cr= np.split(matrizFO,2)[0]
    matriz_Cb= np.split(matrizFO,2)[1]
    
    old_matrizCb = np.split(matrizFO,2)[1]

    matriz_a = matriz


def iniciarSimplex(matriz, matrizB):
    verificarIteracao(matriz, matrizB)



iniciarSimplex(matriz_a, matriz_b)
