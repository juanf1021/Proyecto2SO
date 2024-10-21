class Process:

    def __init__(self, id, arrival_time, burst_time):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.remaining_time = burst_time
        self.waiting_time = 0
        self.turnaround_time = 0


def round_robin(processes, quantum):
    current_time = 0
    queue = processes[:]

    while queue:
        process = queue.pop(0)

        if process.remaining_time > quantum:
            current_time += quantum
            process.remaining_time -= quantum
            queue.append(process)
        else:
            current_time += process.remaining_time
            process.turnaround_time = current_time - process.arrival_time
            process.waiting_time = process.turnaround_time - process.burst_time

    print("ID\tArrival\tBurst\tWaiting\tTurnaround")
    for process in processes:
        print(
            f"{process.id}\t{process.arrival_time}\t{process.burst_time}\t{process.waiting_time}\t{process.turnaround_time}"
        )


if __name__ == "__main__":
    processes = [Process(1, 0, 5), Process(2, 1, 3), Process(3, 2, 8)]
    quantum = 2
    round_robin(processes, quantum)
