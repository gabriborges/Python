from operator import length_hint
import os
os.system('cls')

contador=0
lista=['a','b','c','d','e','f','g','h','i','j']
for i in range(10):
    if lista[i]=='a' or lista[i]=='e' or lista[i]=='i' or lista[i]=='o' or lista[i]=='u':
        pass
    else:
        print(lista[i])
        contador+=1
print("Quantidade de consoantes: "+str(contador))
