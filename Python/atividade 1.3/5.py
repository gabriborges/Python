import os
os.system('cls')

numeros=[]
pares=[]
impares=[]
for i in range(20):
    numeros.append(int(input("Digite um valor:")))
    if numeros[i]%2==0:
        pares.append(numeros[i])
    else:
        impares.append(numeros[i])

print("Lista de inteiros: "+str(numeros))
print("Lista de pares: "+str(pares))
print("Lista de impares: "+str(impares))