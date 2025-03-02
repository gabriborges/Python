agenda = {}

contato = { "Cpf": [], "Nome": [], "Idade": [], "Telefone": []}


def criarContato():
  global contato_alvo
  print("\n----Adicione um novo contato----\n")
  cpf = int(input("Chave cpf: "))
  nome = str(input("Nome do titular: "))
  idade = int(input("Idade: "))
  telefone = int(input("Telefone: "))


  contato["Cpf"].append(cpf)
  contato["Nome"].append(nome)
  contato["Idade"].append(idade)
  contato["Telefone"].append(telefone)

  agenda.update(contato)


def menu():
  criarContato()
  op_menu = str(input("\n\ndigite 's' se deseja sair\n"))
  if op_menu == 's':
    pass
  else:
    menu()


def mostrarAgenda():
  for i in range(len(agenda["Cpf"])):
    print(str(agenda["Nome"][i])+"-"+str(agenda["Idade"][i])+"-"+str(agenda["Telefone"][i]))


print("\n--------- Agenda ---------\n")

menu()
print("\nContatos: \n")
mostrarAgenda()