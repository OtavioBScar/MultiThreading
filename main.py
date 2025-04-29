import threading
import time

def tarefa(nome, tempo):
    print(f"{nome} iniciou e vai esperar {tempo} segundos")
    time.sleep(tempo)
    print(f"{nome} terminou")

# Execução sequencial (sem threads)
def execucao_sequencial():
    inicio = time.time()
    tarefa("Tarefa 1", 2)
    tarefa("Tarefa 2", 2)
    tarefa("Tarefa 3", 2)
    fim = time.time()
    print(f"Tempo total (sequencial): {fim - inicio:.2f} segundos\n")

# Execução com threads
def execucao_com_threads():
    inicio = time.time()
    threads = []
    for i in range(3):
        t = threading.Thread(target=tarefa, args=(f"Tarefa {i+1}", 2))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    fim = time.time()
    print(f"Tempo total (com threads): {fim - inicio:.2f} segundos\n")

# Rodar os dois métodos
execucao_sequencial()
execucao_com_threads()
