
class Conta:
  def __init__(self, pessoa, conta):
    self._titular = pessoa._nome
    self._cpf = pessoa._cpf
    self._conta = conta
    self._saldo = 0
    self._chavesPix = []
    pessoa.associarConta(self._conta)
    print('Sua conta foi criada',self._titular)

  def mostrarSaldo(self):
    print("Saldo da conta ", self._conta, " : ", self._saldo)

  def transferir(self, valor, conta_alvo):
    taxa = 1.005
    if self._saldo >= (valor*taxa):
      conta_alvo._saldo += valor
      self._saldo -= (valor*taxa)
      print('R$', valor, " foram tranferidos para a conta ",
            conta_alvo._conta,'- Taxa: R$',((valor*taxa)-valor))
    else:
      print("Saldo Insuficiente")

  def informacoesConta(self):
    print('Conta:',self._conta,', Titular:',self._titular,', Saldo: ',self._saldo)

  def depositar(self, valor):
    self._saldo+= valor
    print(valor,'reais foram depositados na conta',self._conta)

  def criarChavePix(self, chave):
    self._chavesPix.append(Pix(chave))
    print('Uma nova chave pix foi criada: ', chave)
  
  @property
  def chaves(self):
    print('\nSuas chaves pix: ')
    for chaves in self._chavesPix:
      print(chaves._chave)
    print()

  @property
  def titular(self):
    print(self._titular)
  @titular.setter
  def titular(self, titular):
    self._titular=titular

  @property
  def conta(self):
    return self._conta
  @conta.setter
  def conta(self, conta):
    print("O número da conta não pode ser alterado.")

  @property
  def saldo(self):
    return self._saldo
  @saldo.setter
  def saldo(self,saldo):
    print("Você precisa realizar um deposito para adicionar dinheiro a sua conta.")
    
class contaCorrente(Conta):

  def transferir(self, valor, conta_alvo):
    taxa = 1.025
    if self._saldo >= (valor*taxa):
      conta_alvo._saldo += valor
      self._saldo -= (valor*taxa)
      print('R$', valor, " foram tranferidos para a conta ",
            conta_alvo._conta,'- Taxa: R$',((valor*taxa)-valor))
    else:
      print("Saldo Insuficiente")

class contaPoupanca(Conta):
  
  def transferir(self, valor, conta_alvo):
    taxa = 1.005125
    if self._saldo >= (valor*taxa):
      conta_alvo._saldo += valor
      self._saldo -= (valor*taxa)
      print('R$', valor, " foram tranferidos para a conta ",
            conta_alvo._conta,'- Taxa: R$',((valor*taxa)-valor))
    else:
      print("Saldo Insuficiente")

class Pessoa:
  def __init__(self, nome, cpf):
    self._nome = nome
    self._cpf = cpf

  def associarConta(self, conta):
    self._conta = conta
  
  @property
  def pessoa(self):
    return self._conta

class Pix:
  def __init__(self, chave):
    self._chave = chave
