import threading
import time

CA = False
CB = False

def processo_A():
    global CA, CB
    while True:
        CA = True
        while CB:
            pass
        regiao_critica_A()
        CA = False
        processamento_A()

def processo_B():
    global CA, CB
    while True:
        CB = True
        while CA:
            pass 
        regiao_critica_B()
        CB = False
        processamento_B()

def regiao_critica_A():
    print("Entrou na Região Crítica A")
    time.sleep(1)
    print("Saiu da Região Crítica A")

def processamento_A():
    print("Processamento A fora da Região Crítica")
    time.sleep(1)

def regiao_critica_B():
    print("Entrou na Região Crítica B")
    time.sleep(1)
    print("Saiu da Região Crítica B")

def processamento_B():
    print("Processamento B fora da Região Crítica")
    time.sleep(1)


thread1 = threading.Thread(target=processo_A)
thread2 = threading.Thread(target=processo_B)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")
