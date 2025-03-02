import os
os.system('cls')
from classes import Conta, Pessoa

p1 = Pessoa('Gabriel', 123)
c1 = Conta(p1,1)

p2 = Pessoa('Iann', 321)
c2 = Conta(p2,2)

c1.depositar(300.00)
c1.transferir(50.00,c2)

c1.criarChavePix(9999999999)
c1.criarChavePix('carvalhobrgs@gmail.com')

c1.chaves


c1.informacoesConta()
c2.informacoesConta()
