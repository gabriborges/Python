import threading
import time

vez = 0 
lock = threading.Lock()


def processoA():
    global vez
    for _ in range(2):
        print("Início do Processo A")
        with lock:
            while vez != 0:
                print("Processo A em Espera Ocupada")
        # região crítica
        for _ in range(3):
            print("Região Crítica de A")
        vez = 1
        # região não crítica
        for _ in range(3):
            print("Região NÃO Crítica de A")
            time.sleep(0.01)


def processoB():
    global vez
    for _ in range(2):
        print("Início do Processo B")
        with lock:
            while vez != 1:
                print("Processo B em Espera Ocupada")
        # região crítica
        for _ in range(3):
            print("Região Crítica de B")
        vez = 0
        # região não crítica
        for _ in range(3):
            print("Região NÃO Crítica de B")


thread1 = threading.Thread(target=processoA)
thread2 = threading.Thread(target=processoB)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")
