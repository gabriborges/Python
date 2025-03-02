import os
os.system('cls')
from classes import Funcao, Funcionario

def main():
    
    
    def menu_funcoes():
        funcoes = Funcao()

        opcao = ""
        while opcao != "5":
            print("\nMenu de Funções")
            print("1. Cadastrar")
            print("2. Pesquisar")
            print("3. Editar")
            print("4. Deletar")
            print("5. Voltar")
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                funcoes.cadastrar()
            elif opcao == "2":
                funcoes.pesquisar()
            elif opcao == "3":
                funcoes.editar()
            elif opcao == "4":
                funcoes.deletar()
            elif opcao == "5":
                print("Voltando...")
            else:
                print("Opção inválida")


    def menu_funcionarios():
        funcoes = Funcao()

        opcao = ""
        while opcao != "5":
            print("\nMenu de Funções")
            print("1. Cadastrar")
            print("2. Pesquisar")
            print("3. Editar")
            print("4. Deletar")
            print("5. Voltar")
            opcao = input("\nEscolha uma opção: ")

            if opcao == "1":
                funcoes.cadastrar()
            elif opcao == "2":
                funcoes.pesquisar()
            elif opcao == "3":
                funcoes.editar()
            elif opcao == "4":
                funcoes.deletar()
            elif opcao == "5":
                print("Voltando...")
            else:
                print("Opção inválida")

    def menu():          
            opcao = ""
            while opcao != "3":
                print("\nMenu Principal")
                print("1. Manter Funções")
                print("2. Manter Funcionários")
                print("3. Sair")
                opcao = input("\nEscolha uma opção: ")

                if opcao == "1":
                    menu_funcoes()
                elif opcao == "2":
                    menu_funcionarios()
                elif opcao == "3":
                    print("Saindo...")
                else:
                    print("Opção inválida")
                    
    menu()
if __name__ == '__main__':
    main()