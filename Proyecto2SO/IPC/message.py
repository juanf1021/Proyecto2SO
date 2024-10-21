import time
import psutil
import multiprocessing
import os  # Asegúrate de importar os

def producer(queue):
    for i in range(1000000):  # Enviar 1000 mensajes
        queue.put(f"Mensaje {i}")
    queue.put("FIN")  # Mensaje para indicar el final

def consumer(queue):
    while True:
        message = queue.get()
        if message == "FIN":
            break

def measure_resources():
    # Obtener el proceso actual
    process = psutil.Process(os.getpid())
    return process.cpu_percent(), process.memory_info().rss

if __name__ == "__main__":
    queue = multiprocessing.Queue()

    start_time = time.time()

    # Iniciar el proceso productor y consumidor
    producer_process = multiprocessing.Process(target=producer, args=(queue,))
    consumer_process = multiprocessing.Process(target=consumer, args=(queue,))

    producer_process.start()
    consumer_process.start()

    # Medir recursos antes y después de la ejecución
    cpu_start, mem_start = measure_resources()

    producer_process.join()
    consumer_process.join()

    cpu_end, mem_end = measure_resources()
    end_time = time.time()

    # Resultados
    print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
    print(f"Uso de CPU: {cpu_end - cpu_start:.2f}%")
    print(f"Uso de memoria: {mem_end - mem_start} bytes")
