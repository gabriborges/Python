''' Considere um sistema onde os dados são armazenados em dicionários. 
Nesse sistema existe um dicionario principal e o dicionário de backup.
Cada vez que o dicionário principal atinge tamanho 5, ele imprime os dados 
na tela e apaga o seu conteúdo. Crie um programa que insira dados em um dicionário, 
realizando o backup a cada dado e excluindo os dados do dicionário principal quando 
ele atingir tamanho 5. '''

import os
os.system('cls')

Principal={}
Backup={}

principal = { "Cpf": [], "Nome": [], "Idade": []}
backup = { "Cpf": [], "Nome": [], "Idade": []}

contador_backup=0

def criarContato():

    global contador_backup
    print("\n----Cadastro----\n")
    cpf = int(input("Cpf: "))
    nome = str(input("Nome: "))
    idade = int(input("Idade: "))

    principal["Cpf"].append(cpf)
    principal["Idade"].append(idade)
    principal["Nome"].append(nome)

    Principal.update(principal)
    contador_backup+=1
    if contador_backup==5:
        realizarBackup()
        contador_backup=0

def menu():
  criarContato()
  op_menu = str(input("\n\ndigite 's' se deseja sair\n"))
  if op_menu == 's':
    pass
  else:
    menu()

def realizarBackup():
        if len(Principal["Cpf"])==5:
            i=0
            while i<len(Principal["Cpf"]):
                temp_cpf=Principal["Cpf"][i]
                temp_nome=Principal["Nome"][i]
                temp_idade=Principal["Idade"][i]
                backup["Cpf"].append(temp_cpf)
                backup["Nome"].append(temp_nome)
                backup["Idade"].append(temp_idade)

                Backup.update(backup)
                Principal["Cpf"].pop(i)
                Principal["Nome"].pop(i)
                Principal["Idade"].pop(i)
            print('\nBackup realizado, o dicionario principal possui ',len(Principal["Cpf"]),' contatos. O dicionario de backup possui ', len(Backup["Cpf"]),' contatos.')

        else:
            print('O backup não pode ser realizado!')

def mostrarPrincipal():
  print("\nDicionario Principal: \n")
  for i in range(len(Principal["Cpf"])):
    print(str(Principal["Nome"][i])+"-"+str(Principal["Idade"][i]))

def mostrarBackup():
  if Backup:
    print("\nDicionario Backup: \n")
    for i in range(len(Backup["Cpf"])):
        print(str(Backup["Nome"][i])+"-"+str(Backup["Idade"][i]))
  else:
    print("O dicionario de backup está vazio.")
    

menu()

print("\n------- Dicionarios -------")
mostrarPrincipal()
mostrarBackup()