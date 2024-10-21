import time
import psutil
import multiprocessing

def producer(conn):
    for i in range(100000):  # Enviar 1000 mensajes
        conn.send(f"Mensaje {i}")
    conn.send("FIN")  # Mensaje para indicar el final
    conn.close()  # Cerrar la conexión

def consumer(conn):
    while True:
        message = conn.recv()
        if message == "FIN":
            break
    conn.close()  # Cerrar la conexión

def measure_resources():
    # Obtener el proceso actual
    process = psutil.Process()
    return process.cpu_percent(), process.memory_info().rss

if __name__ == "__main__":
    # Crear un pipe
    parent_conn, child_conn = multiprocessing.Pipe()

    start_time = time.time()

    # Iniciar el proceso productor y consumidor
    producer_process = multiprocessing.Process(target=producer, args=(child_conn,))
    consumer_process = multiprocessing.Process(target=consumer, args=(parent_conn,))

    producer_process.start()
    consumer_process.start()

    # Medir recursos antes y después de la ejecución
    cpu_start, mem_start = measure_resources()

    producer_process.join()
    consumer_process.join()

    cpu_end, mem_end = measure_resources()
    end_time = time.time()  # Se asegura de que esta línea esté aquí

    # Resultados
    print(f"Tiempo de ejecución: {end_time - start_time:.4f} segundos")
    print(f"Uso de CPU: {cpu_end - cpu_start:.2f}%")
    print(f"Uso de memoria: {mem_end - mem_start} bytes")
