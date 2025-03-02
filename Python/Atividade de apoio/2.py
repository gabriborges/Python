import os
os.system('cls')

pessoas = {}
menores = {}

pessoa = { "Cpf": [], "Nome": [], "Idade": []}
menor = { "Cpf": [], "Nome": [], "Idade": []}

def criarContato():
  print("\n----Cadastro----\n")
  cpf = int(input("Cpf: "))
  nome = str(input("Nome: "))
  idade = int(input("Idade: "))

  pessoa["Cpf"].append(cpf)
  pessoa["Nome"].append(nome)
  pessoa["Idade"].append(idade)

  pessoas.update(pessoa)


def menu():
  criarContato()
  op_menu = str(input("\n\ndigite 's' se deseja sair\n"))
  if op_menu == 's':
    pass
  else:
    menu()

def removerMenores():
  if len(pessoas)==0:
    pass
  else:
    i=0
    while i < len(pessoas["Cpf"]):
        if pessoas["Idade"][i]<18:
          temp_cpf=pessoas["Cpf"][i]
          temp_nome=pessoas["Nome"][i]
          temp_idade=pessoas["Idade"][i]
          menor["Cpf"].append(temp_cpf)
          menor["Nome"].append(temp_nome)
          menor["Idade"].append(temp_idade)
          
          menores.update(menor)

          pessoas["Cpf"].pop(i)
          pessoas["Nome"].pop(i)
          pessoas["Idade"].pop(i)
          i-=1
        i+=1

def mostrarPessoas():
  print("\nPessoas: \n")
  for i in range(len(pessoas["Cpf"])):
    print(str(pessoas["Nome"][i])+"-"+str(pessoas["Idade"][i]))

def mostrarMenores():
  print("\nMenores de Idade: \n")
  if len(menores)==0:
    pass
  else:
    for i in range(len(menores["Cpf"])):
      print(str(menores["Nome"][i])+"-"+str(menores["Idade"][i]))


menu()

removerMenores()

print("\n------- Pessoas Castradas -------")
mostrarPessoas()
mostrarMenores()
