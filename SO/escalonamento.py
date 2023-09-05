import threading
import time

counter = 1

def task1():
    global counter
    print("Início da Tarefa 1")
    while counter!= 0:
        for _ in range(5):
            print("Tarefa 1 executando")
            counter = 1 
            time.sleep(1.8)
        
    print("Fim da Tarefa 1")

def task2():
    global counter
    print("Início da Tarefa 2")
    while counter!= 1:
        for _ in range(5):
            print("Tarefa 2 executando")
            counter = 0  
            time.sleep(1.8)
    print("Fim da Tarefa 2")

thread1 = threading.Thread(target=task1)
thread2 = threading.Thread(target=task2)

thread1.start()
thread2.start()

thread1.join()
thread2.join()

print("Ambas as tarefas foram concluídas")

