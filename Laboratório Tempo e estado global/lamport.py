import threading
import time
import random
from queue import Queue

TOTAL_PROCESSOS = 3
fila_mensagens = [Queue() for _ in range(TOTAL_PROCESSOS)]
relogio_logico = [0 for _ in range(TOTAL_PROCESSOS)]

def processo(id_processo: int):
    global relogio_logico
    for _ in range(5):
        time.sleep(random.uniform(0.5, 1.5))

        relogio_logico[id_processo] += 1
        print(f"Processo {id_processo}: Evento local | Relógio = {relogio_logico[id_processo]}")

        destinatario = random.choice([p for p in range(TOTAL_PROCESSOS) if p != id_processo])
        marca_tempo = relogio_logico[id_processo]
        fila_mensagens[destinatario].put((id_processo, marca_tempo))
        print(f"Processo {id_processo}: Mensagem enviada para P{destinatario} | Relógio = {marca_tempo}")

        while not fila_mensagens[id_processo].empty():
            remetente, tempo_recebido = fila_mensagens[id_processo].get()
            relogio_logico[id_processo] = max(relogio_logico[id_processo], tempo_recebido) + 1
            print(f"Processo {id_processo}: Mensagem recebida de P{remetente} (Tempo={tempo_recebido}) | Novo relógio = {relogio_logico[id_processo]}")

threads = [threading.Thread(target=processo, args=(i,)) for i in range(TOTAL_PROCESSOS)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()