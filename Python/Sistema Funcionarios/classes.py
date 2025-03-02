
import pymysql.cursors

codigo_func=0

connection = pymysql.connect(host='localhost',
                                user='root',
                                password='',
                                database='prova03', 
                                charset='utf8mb4', 
                                cursorclass=pymysql.cursors.DictCursor)

class Funcionario:
    global connection
    def __init__(self):
        self.funcionarios = []

    def cadastrar(self):
        print('------------- Cadastrando Funcionario -------------')
        nome = str(input("Nome: "))
        cpf = str(input("CPF: "))
        funcao = str(input("Função: "))
        salario = float(input("Salário: "))
        telefone = str(input("Telefone: "))
        funcionario = {"nome": nome, "cpf": cpf, "funcao": funcao, "salario": salario, "telefone": telefone}
        self.funcionarios.append(funcionario)
        print("Funcionário cadastrado com sucesso!")

        with connection.cursor() as c:
            sql = "INSERT INTO funcionarios (cpf, nome, funcao, salario, telefone) VALUES (%s,%s,%s,%s,%s)"
            c.execute(sql, (cpf, nome, funcao, salario, telefone ))
        connection.commit() 

    def pesquisar(self):
        print('------------- Pesquise um Funcionario -------------')
        cpf = input("Informe o CPF do funcionário: ")
        for funcionario in self.funcionarios:
            if funcionario["cpf"] == cpf:
                print()
                print('--- Funcionario ----')
                print("Nome:", funcionario["nome"])
                print("CPF:", funcionario["cpf"])
                print("Função:", funcionario["funcao"])
                print("Salário:", funcionario["salario"])
                print("Telefone:", funcionario["telefone"])
                return
        print("Funcionário não encontrado.")

    def editar(self):
        cpf = input("Informe o CPF do funcionário: ")
        for funcionario in self.funcionarios:
            if funcionario["cpf"] == cpf:
                funcionario["nome"] = input("Novo nome: ")
                funcionario["funcao"] = input("Nova função: ")
                funcionario["salario"] = float(input("Novo salário: "))
                funcionario["telefone"] = input("Novo telefone: ")
                print("Funcionário editado com sucesso!")
                return
        print("Funcionário não encontrado.")

    def deletar(self):
        cpf = input("Informe o CPF do funcionário: ")
        for funcionario in self.funcionarios:
            if funcionario["cpf"] == cpf:
                self.funcionarios.remove(funcionario)
                print("Funcionário deletado com sucesso!")
                return
        print("Funcionário não encontrado.")


class Funcao:
    global connection

    def __init__(self):
        self.funcoes = []

    def cadastrar(self):
        global codigo_func

        codigo_func+=1
        codigo = str(codigo_func)
        nome = input("Nome: ")
        funcao = {"codigo": codigo, "nome": nome}
        self.funcoes.append(funcao)
        print("Função cadastrada com sucesso!")

        with connection.cursor() as c:
            sql = "INSERT INTO funcionario (cod, nome) VALUES (%s, %s)"
            c.execute(sql, (codigo, nome))
        connection.commit() 

        self.pesquisar(codigo)

    def pesquisar(self, codigo=0):
        if codigo == 0:
            codigo = input("Informe o código da função: ")

        for funcao in self.funcoes:
            if funcao["codigo"] == codigo:
                print()
                print('--- Função ----')
                print("Código:", funcao["codigo"])
                print("Nome:", funcao["nome"])
                return
        print("Função não encontrada.")

    def editar(self):
        codigo = input("Informe o código da função: ")
        for funcao in self.funcoes:
            if funcao["codigo"] == codigo:
                funcao["nome"] = input("Novo nome: ")
                print("Função editada com sucesso!")
                return
        print("Função não encontrada.")

    def deletar(self):
        codigo = input("Informe o código da função: ")
        for funcao in self.funcoes:
            if funcao["codigo"] == codigo:
                self.funcoes.remove(funcao)
                print("Função deletada com sucesso!")
                return
        print("Função não encontrada.")
