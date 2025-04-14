from threading import Thread
import time

# Definindo as funções que serão executadas pelas threads
def tarefa1():
    for i in range(5):
        print("Tarefa 1 está executando...")
        time.sleep(1)

def tarefa2():
    for i in range(5):
        print("Tarefa 2 está executando...")
        time.sleep(1)

# Criando as threads
thread1 = Thread(target=tarefa1)
thread2 = Thread(target=tarefa2)

# Iniciando as threads
thread1.start()
thread2.start()

# Esperando as threads terminarem
thread1.join()
thread2.join()

print("Execução concluída!")
