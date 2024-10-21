#include <stdio.h>

struct Process {
  int id;
  int arrival_time;
  int burst_time;
  int remaining_time;
  int waiting_time;
  int turnaround_time;
};

void round_robin(struct Process processes[], int n, int quantum) {
  int current_time = 0;
  int processes_done = 0;
  while (processes_done < n) {
    for (int i = 0; i < n; i++) {
      if (processes[i].remaining_time > 0) {
        if (processes[i].remaining_time > quantum) {
          current_time += quantum;
          processes[i].remaining_time -= quantum;
        } else {
          current_time += processes[i].remaining_time;
          processes[i].waiting_time = current_time - processes[i].arrival_time -
                                      processes[i].burst_time;
          processes[i].turnaround_time =
              current_time - processes[i].arrival_time;
          processes[i].remaining_time = 0;
          processes_done++;
        }
      }
    }
  }

  printf("ID\tArrival\tBurst\tWaiting\tTurnaround\n");
  for (int i = 0; i < n; i++) {
    printf("%d\t%d\t%d\t%d\t%d\n", processes[i].id, processes[i].arrival_time,
           processes[i].burst_time, processes[i].waiting_time,
           processes[i].turnaround_time);
  }
}

int main() {
  struct Process processes[] = {{1, 0, 5, 5}, {2, 1, 3, 3}, {3, 2, 8, 8}};
  int n = sizeof(processes) / sizeof(processes[0]);
  int quantum = 2;
  round_robin(processes, n, quantum);
  return 0;
}
