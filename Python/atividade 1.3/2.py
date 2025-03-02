import os
os.system('cls')

lista=[]
for i in range(10):
    lista.append(float(input("Digite um valor:")))
print(lista[::-1])