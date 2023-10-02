import threading
import time

travaA = False
travaB = False

def processoA():
    global travaA
    for _ in range(2):
        print("Início do Processo A")
        travaA = True
        while travaB:
            print("Processo A em Espera")
        # região crítica
        for _ in range(3):
            print("Região Crítica de A")
        travaA = False
        # região não crítica
        for _ in range(3):
            print("Região NÃO Crítica de A")
            time.sleep(1)

def processoB():
    global travaB
    for _ in range(2):
        print("Início do Processo B")
        travaB = True
        while travaA:
            print("Processo B em Espera")
        # região crítica
        for _ in range(3):
            print("Região Crítica de B")
        travaB = False
        # região não crítica
        for _ in range(3):
            print("Região NÃO Crítica de B")
            time.sleep(1)

thread1 = threading.Thread(target=processoA)
thread2 = threading.Thread(target=processoB)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")
