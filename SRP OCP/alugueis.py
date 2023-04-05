from abc import ABC, abstractmethod
import datetime

class Imovel(ABC):
    def __init__(self, endereco, preco):
        self.endereco = endereco
        self.preco = preco

    @abstractmethod
    def tipo_imovel(self):
        pass

class Casa(Imovel):
    def tipo_imovel(self):
        return "Casa"

class Quarto(Imovel):
    def tipo_imovel(self):
        return "Quarto"

class Escritorio(Imovel):
    def tipo_imovel(self):
        return "Escritório"

class Pessoa(ABC):
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    @abstractmethod
    def tipo_pessoa(self):
        pass

class PessoaFisica(Pessoa):
    def tipo_pessoa(self):
        return "Pessoa Física"

class PessoaJuridica(Pessoa):
    def tipo_pessoa(self):
        return "Pessoa Jurídica"

class Aluguel:
    def __init__(self, pessoa, imovel, preco):
        self.pessoa = pessoa
        self.imovel = imovel
        self.preco = preco
        self.pagamentos = []

    def calcular_preco_com_desconto(self, desconto):
        preco_com_desconto = self.preco - (self.preco * desconto / 100)
        self.pagamentos.append((preco_com_desconto, datetime.datetime.now()))
        return preco_com_desconto

    def adicionar_pagamento(self, valor):
        self.pagamentos.append((valor, datetime.datetime.now()))

    def gerar_log(self):
        print(f"Log de pagamentos do aluguel do(a) {self.imovel.tipo_imovel()} localizado(a) em {self.imovel.endereco}:")
        for pagamento in self.pagamentos:
            print(f"Data: {pagamento[1]} - Valor pago: R${pagamento[0]:.2f}")

# Exemplo de uso:
casa = Casa("Casa 1", 1000)
quarto = Quarto("Quarto 1", 500)
escritorio = Escritorio("Escritorio 1", 2000)

pessoa_fisica = PessoaFisica("Gabriel", "gabriel@gmail.com")
pessoa_juridica = PessoaJuridica("Empresa 1", "empresa1@gmail.com")

aluguel_casa = Aluguel(pessoa_fisica, casa, 1000)
aluguel_quarto = Aluguel(pessoa_juridica, quarto, 500)
aluguel_escritorio = Aluguel(pessoa_fisica, escritorio, 2000)

preco_com_desconto = aluguel_casa.calcular_preco_com_desconto(10)
print(f"Preço com desconto: R${preco_com_desconto:.2f}")

preco_com_desconto = aluguel_escritorio.calcular_preco_com_desconto(15)
print(f"Preço com desconto: R${preco_com_desconto:.2f}")

aluguel_casa.adicionar_pagamento(950)
aluguel_casa.adicionar_pagamento(1000)
aluguel_casa.gerar_log()

aluguel_escritorio.adicionar_pagamento(1700)
aluguel_escritorio.adicionar_pagamento(1800)
aluguel_escritorio.gerar_log()
