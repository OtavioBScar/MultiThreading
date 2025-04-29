
# 💻 Programação com Threads

A **programação com threads** permite que um programa realize várias tarefas simultaneamente, o que é especialmente útil quando lidamos com tarefas paralelizáveis ou que envolvem espera (como acesso a disco ou rede). Isso é diferente do uso de **processos**, que são mais pesados em termos de recursos e isolados entre si.

---

## 🧠 Vantagens de Threads sobre Processos

- **Compartilhamento de memória:** Threads compartilham o mesmo espaço de memória, o que facilita a comunicação entre elas.
- **Leveza:** Criar uma thread consome menos recursos do que criar um processo.
- **Desempenho em I/O:** Threads são muito eficazes em aplicações que fazem operações de I/O (leitura de arquivos, rede etc).
- **Menor overhead:** Menos sobrecarga do sistema operacional.

---

## ✅ Resultado Esperado

- A **execução sequencial** leva ~6 segundos (2s por tarefa, uma após a outra).
- A **execução com threads** leva ~2 segundos (as tarefas ocorrem em paralelo).

---

## 📚 Conclusão

Esse exemplo simples mostra como as threads permitem que múltiplas tarefas sejam feitas **simultaneamente**, reduzindo o tempo total de execução. Isso é extremamente útil para melhorar o desempenho de aplicações com tarefas paralelizáveis.
