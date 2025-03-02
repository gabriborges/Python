import os
os.system('cls')
from classes import Conta, Pessoa, contaCorrente, contaPoupanca

def main():
    p1 = Pessoa('Gabriel', 123)
    c1 = contaPoupanca(p1,1)

    p2 = Pessoa('Iann', 321)
    c2 = contaCorrente(p2,2)

    '''contaAbstrata = Conta('Mr Abstract',66)
    contaAbstrata.depositar(50)'''

    c1.depositar(100.00)
    c2.depositar(100.00)
    c1.transferir(50.00,c2)
    c2.transferir(25.00,c1)

    c1.informacoesConta()
    c2.informacoesConta()
    
    print(c1.saldo)
    

if __name__ == '__main__':
    main()
