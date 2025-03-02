import os
os.system('cls')

notas=[]
media=0
for i in range(4):
    notas.append(float(input("Digite uma nota:")))
    media+=notas[i]
    
media=media/4
print("Notas: "+str(notas))
print("Media: "+str(media))