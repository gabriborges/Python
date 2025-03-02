import os
os.system('cls')

contas = []

op_contas=1

def nova_conta():
    global op_contas
    global conta_alvo
    print("\n----Crie uma nova conta----\n")
    numero = op_contas
    conta_alvo=numero
    titular = str(input("Nome do titular: "))
    saldo = 0.0
    conta = {"Numero": numero, "Titular": titular, "Saldo": saldo}
    contas.append(conta)
    mostrar_conta()
    op_contas+=1

def remover_conta():
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            del(contas[i])
            mostrar_todas()
            break        
    menu_principal()
  
def realizar_tranferencia():
    conta_dest=int(input("\nConta destinaria da transferencia: "))
    valor=float(input("\nValor a ser tranferido: "))
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            if contas[i]["Saldo"]>=valor:
                for j in range(len(contas)):
                    if contas[j]["Numero"]==conta_dest:
                        contas[j]["Saldo"]+=valor
                        contas[i]["Saldo"]-=valor
                        print("\nR$"+str(valor)+" acabam de ser tranferisos para a conta "+str(conta_dest)+"\n")
            else:
                print("Saldo indisponivel")
    menu_principal()          

def exibir_saldo():
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            print("Seu saldo é R$"+str(contas[i]["Saldo"]))
    menu_principal()       

def depositar():
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            deposito=float(input("Valor a ser depositado: "))
            contas[i]["Saldo"]+=deposito
            print("Deposito realizado com sucesso.")
            mostrar_conta()
    menu_principal()
    
def encontrar_conta():
    global conta_alvo
    conta_alvo=int(input("\nDigite o número da conta: "))
    conta_encontrada=False
    if len(contas)==0:
        print("Nenhuma conta está cadastrada.")
        menu_principal()
    else:
        for i in range(len(contas)):
            if contas[i]["Numero"]==conta_alvo:
                conta_encontrada=True
                op_encontrar = int(input("\n1- Remover Conta \n2- Realizar transferência\n3- Exibir saldo\n4- Depositar Valor\n5- Voltar para o menu inicial\n "))
                if op_encontrar == 1:
                    remover_conta()
                elif op_encontrar==2:
                    realizar_tranferencia()
                elif op_encontrar==3:
                    exibir_saldo()
                elif op_encontrar==4:
                    depositar()
                elif op_encontrar==5:
                    menu_principal()
                else:
                    print("\nOpção inválida, tente outra.")
                    encontrar_conta()
    if conta_encontrada==False: print("\nConta não encontrada.")
    menu_principal()

def mostrar_conta():
    for i in range(len(contas)):
        if contas[i]["Numero"]==conta_alvo:
            print("\nInformações da conta: ")
            print("\nNumero: "+str(contas[i]["Numero"])+"\nTitular: "+str(contas[i]["Titular"])+"\nSaldo: R$"+str(contas[i]["Saldo"])+"\n")

def mostrar_todas():
    for i in range(len(contas)):
            print("\nInformações da conta: \n")
            print("\nNumero: "+str(contas[i]["Numero"])+"\nTitular: "+str(contas[i]["Titular"])+"\nSaldo: R$"+str(contas[i]["Saldo"])+"\n")

def menu_principal():
    op_menu_principal = int(input("-------------------------\n 1- Cadastrar Nova Conta \n 2- Encontrar uma conta  \n-------------------------\n"))
    if op_menu_principal == 1:
        nova_conta()
        menu_principal()
    elif op_menu_principal==2:
        encontrar_conta()
    else:
        print("\nOpção inválida.\n")
        menu_principal()

menu_principal()