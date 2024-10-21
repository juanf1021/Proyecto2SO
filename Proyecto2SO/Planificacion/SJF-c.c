#include <stdio.h>

struct Process {
  int id;
  int arrival_time;
  int burst_time;
  int waiting_time;
  int turnaround_time;
};

void sjf(struct Process processes[], int n) {
  struct Process temp;
  for (int i = 0; i < n - 1; i++) {
    for (int j = i + 1; j < n; j++) {
      if (processes[i].burst_time > processes[j].burst_time) {
        temp = processes[i];
        processes[i] = processes[j];
        processes[j] = temp;
      }
    }
  }

  int current_time = 0;
  for (int i = 0; i < n; i++) {
    if (current_time < processes[i].arrival_time)
      current_time = processes[i].arrival_time;

    processes[i].waiting_time = current_time - processes[i].arrival_time;
    processes[i].turnaround_time =
        processes[i].waiting_time + processes[i].burst_time;
    current_time += processes[i].burst_time;
  }

  printf("ID\tArrival\tBurst\tWaiting\tTurnaround\n");
  for (int i = 0; i < n; i++) {
    printf("%d\t%d\t%d\t%d\t%d\n", processes[i].id, processes[i].arrival_time,
           processes[i].burst_time, processes[i].waiting_time,
           processes[i].turnaround_time);
  }
}

int main() {
  struct Process processes[] = {{1, 0, 5}, {2, 2, 3}, {3, 4, 1}};
  int n = sizeof(processes) / sizeof(processes[0]);
  sjf(processes, n);
  return 0;
}
