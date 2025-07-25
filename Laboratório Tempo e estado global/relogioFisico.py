import threading
import time
import random
from queue import Queue

TOTAL_PROCESSOS = 3
fila_mensagens = [Queue() for _ in range(TOTAL_PROCESSOS)]

def tempo_atual_ms():
    return int(time.time() * 1000)

def processo(id_processo: int):
    for _ in range(5):
        time.sleep(random.uniform(0.5, 1.5))
    
        destinatario = random.choice([p for p in range(TOTAL_PROCESSOS) if p != id_processo])
        marca_tempo = tempo_atual_ms()
        mensagem = (id_processo, marca_tempo)
        fila_mensagens[destinatario].put(mensagem)
        print(f"Processo {id_processo}: Mensagem enviada para P{destinatario} no tempo {marca_tempo}ms")

        while not fila_mensagens[id_processo].empty():
            remetente, tempo_recebido = fila_mensagens[id_processo].get()
            print(f"Processo {id_processo}: Mensagem recebida de P{remetente} com marca de tempo {tempo_recebido}ms")

threads = [threading.Thread(target=processo, args=(i,)) for i in range(TOTAL_PROCESSOS)]
for thread in threads:
    thread.start()
for thread in threads:
    thread.join()