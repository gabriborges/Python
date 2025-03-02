import os
os.system('cls')

nota=media=contador=0
medias=[]
for i in range(10):
    for j in range(4):
        nota=(float(input(("Digite as notas do aluno ")+str(i+1)+" : ")))
        media+=nota
        if j==3:
            media=media/4
            if media>=7:
                contador+=1
            medias.append(media)
            media=0
print("Medias: "+str(medias))
print("Quantidade de alunos com media maior ou igual a 7: "+str(contador))