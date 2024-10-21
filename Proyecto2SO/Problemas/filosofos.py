import threading
import time
import random

class Philosopher(threading.Thread):
    def __init__(self, id, left_fork, right_fork):
        threading.Thread.__init__(self)
        self.id = id
        self.left_fork = left_fork
        self.right_fork = right_fork

    def run(self):
        while True:
            self.think()
            self.eat()

    def think(self):
        print(f"Filósofo {self.id} está pensando.")
        time.sleep(random.uniform(0.1, 0.5))  # Simula pensar

    def eat(self):
        with self.left_fork:  # Adquiere el tenedor izquierdo
            with self.right_fork:  # Adquiere el tenedor derecho
                print(f"Filósofo {self.id} está comiendo.")
                time.sleep(random.uniform(0.1, 0.5))  # Simula comer

# Inicializar los tenedores como mutex
num_philosophers = 5
forks = [threading.Lock() for _ in range(num_philosophers)]

# Crear filósofos
philosophers = [Philosopher(i, forks[i], forks[(i + 1) % num_philosophers]) for i in range(num_philosophers)]

# Iniciar los hilos de los filósofos
for philosopher in philosophers:
    philosopher.start()
