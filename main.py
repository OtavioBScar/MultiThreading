import threading
import time
import os

# Criação de arquivos grandes para teste
def criar_arquivos():
    os.makedirs("arquivos", exist_ok=True)
    conteudo = "Clauss me da 10!\n" * 100000
    for i in range(10):
        with open(f"arquivos/arquivo_{i}.txt", "w", encoding="utf-8") as f:
            f.write(conteudo)

        # f = open(f"arquivos/arquivo_{i}.txt", "w", encoding="utf-8")
        # f.write(conteudo)

        # f.close()

# Função que simula uma tarefa de I/O: leitura de um arquivo
def ler_arquivo(nome_arquivo):
    with open(nome_arquivo, "r", encoding="utf-8") as f:
        conteudo = f.read()
    print(f"{nome_arquivo} lido ({len(conteudo)} caracteres)")

def execucao_sequencial():
    inicio = time.time()
    for i in range(10):
        ler_arquivo(f"arquivos/arquivo_{i}.txt")
    fim = time.time()
    print(f"Tempo total (Sem): {fim - inicio:.2f} segundos\n")

def execucao_com_threads():
    inicio = time.time()
    threads = []
    for i in range(10):
        t = threading.Thread(target=ler_arquivo, args=(f"arquivos/arquivo_{i}.txt",))
        threads.append(t)
        t.start()
    for t in threads:
        t.join()
    fim = time.time()
    print(f"Tempo total (com threads): {fim - inicio:.2f} segundos\n")

# Preparação
criar_arquivos()

# Execução
execucao_sequencial()
execucao_com_threads()
