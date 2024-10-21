import threading
import time
import random

class ReadWriteLock:
    def __init__(self):
        self.read_lock = threading.Semaphore(1)
        self.write_lock = threading.Semaphore(1)
        self.reader_count = 0

    def reader_acquire(self):
        self.read_lock.acquire()
        self.reader_count += 1
        if self.reader_count == 1:
            self.write_lock.acquire()
        self.read_lock.release()

    def reader_release(self):
        self.read_lock.acquire()
        self.reader_count -= 1
        if self.reader_count == 0:
            self.write_lock.release()
        self.read_lock.release()

    def writer_acquire(self):
        self.write_lock.acquire()

    def writer_release(self):
        self.write_lock.release()

def reader(lock, reader_id):
    while True:
        lock.reader_acquire()
        print(f"Reader {reader_id} is reading.")
        time.sleep(random.uniform(0.1, 0.5))  # Simulate reading
        print(f"Reader {reader_id} has finished reading.")
        lock.reader_release()
        time.sleep(random.uniform(0.1, 0.5))  # Wait before next read

def writer(lock, writer_id):
    while True:
        lock.writer_acquire()
        print(f"Writer {writer_id} is writing.")
        time.sleep(random.uniform(0.2, 0.7))  # Simulate writing
        print(f"Writer {writer_id} has finished writing.")
        lock.writer_release()
        time.sleep(random.uniform(0.1, 0.5))  # Wait before next write

# Initialize locks and create threads
lock = ReadWriteLock()
readers = [threading.Thread(target=reader, args=(lock, i)) for i in range(5)]
writers = [threading.Thread(target=writer, args=(lock, i)) for i in range(2)]

for r in readers:
    r.start()
for w in writers:
    w.start()
