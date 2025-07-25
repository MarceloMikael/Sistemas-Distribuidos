import threading
import time
import random
from queue import Queue

TOTAL_PROCESSOS = 3
fila_mensagens = [Queue() for _ in range(TOTAL_PROCESSOS)]
relogio_vetorial = [[0]*TOTAL_PROCESSOS for _ in range(TOTAL_PROCESSOS)]

def processo(id_processo: int):
    for _ in range(5):
        time.sleep(random.uniform(0.5, 1.5))
        
        relogio_vetorial[id_processo][id_processo] += 1
        print(f"Processo {id_processo}: Evento local | Vetor = {relogio_vetorial[id_processo]}")
        
        destinatario = random.choice([p for p in range(TOTAL_PROCESSOS) if p != id_processo])
        mensagem = (id_processo, list(relogio_vetorial[id_processo]))
        fila_mensagens[destinatario].put(mensagem)
        print(f"Processo {id_processo}: Mensagem enviada para P{destinatario} | Vetor = {relogio_vetorial[id_processo]}")

        while not fila_mensagens[id_processo].empty():
            remetente, vetor_recebido = fila_mensagens[id_processo].get()
            for j in range(TOTAL_PROCESSOS):
                relogio_vetorial[id_processo][j] = max(relogio_vetorial[id_processo][j], vetor_recebido[j])
            relogio_vetorial[id_processo][id_processo] += 1
            print(f"Processo {id_processo}: Mensagem recebida de P{remetente} | Vetor = {relogio_vetorial[id_processo]}")

threads = [threading.Thread(target=processo, args=(i,)) for i in range(TOTAL_PROCESSOS)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()