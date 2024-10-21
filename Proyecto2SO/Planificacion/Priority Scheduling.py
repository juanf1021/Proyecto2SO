class Process:

    def __init__(self, id, arrival_time, burst_time, priority):
        self.id = id
        self.arrival_time = arrival_time
        self.burst_time = burst_time
        self.priority = priority
        self.waiting_time = 0
        self.turnaround_time = 0


def priority_scheduling(processes):
    processes.sort(key=lambda x: (x.priority, x.arrival_time))
    current_time = 0

    for process in processes:
        if current_time < process.arrival_time:
            current_time = process.arrival_time

        process.waiting_time = current_time - process.arrival_time
        process.turnaround_time = process.waiting_time + process.burst_time
        current_time += process.burst_time

    print("ID\tArrival\tBurst\tPriority\tWaiting\tTurnaround")
    for process in processes:
        print(
            f"{process.id}\t{process.arrival_time}\t{process.burst_time}\t{process.priority}\t{process.waiting_time}\t{process.turnaround_time}"
        )


if __name__ == "__main__":
    processes = [Process(1, 0, 5, 2), Process(2, 2, 3, 1), Process(3, 4, 1, 3)]
    priority_scheduling(processes)
