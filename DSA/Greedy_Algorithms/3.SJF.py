# 🧩 SJF Scheduling Problem — Shortest Job First
#
# Shortest Job First (SJF) is a CPU scheduling algorithm where:
#     The process with the smallest burst time is executed first.
#     It can be Preemptive (SRTF) or Non-preemptive (SJF).
#
# This is one of the most asked OS scheduling questions.

# this assumes all jobs came at same time 0
def sjf_same_arrival(processes):
    """
    processes = [(pid, burst_time)]
    All AT = 0
    """
    # Sort by burst time
    processes = sorted(processes, key=lambda x: x[1])

    current_time = 0
    result = []

    for pid, bt in processes:
        ct = current_time + bt
        tat = ct  # AT = 0
        wt = tat - bt
        result.append((pid, bt, ct, tat, wt))
        current_time = ct

    return result


# this assumes jobs come at different times 
def sjf_non_preemptive(processes):
    # processes = [(pid, arrival, burst)]
    n = len(processes)
    processes.sort(key=lambda x: x[1])  # sort by arrival time

    time = 0
    completed = 0
    visited = [False] * n
    result = []

    while completed < n:
        idx = -1
        min_bt = float('inf')

        # find process with minimum burst among arrived
        for i in range(n):
            pid, at, bt = processes[i]
            if at <= time and not visited[i]:
                if bt < min_bt:
                    min_bt = bt
                    idx = i

        if idx == -1:  # no process arrived
            time += 1
            continue

        pid, at, bt = processes[idx]
        time += bt
        ct = time
        tat = ct - at
        wt = tat - bt

        result.append((pid, at, bt, ct, tat, wt))
        visited[idx] = True
        completed += 1

    return result


def srtf(processes):
    # processes = [(pid, arrival, burst)]
    n = len(processes)
    rem = {pid: bt for pid, _, bt in processes}
    time = 0
    completed = 0
    done = set()
    result = {}
    last_time = {}

    while completed < n:
        # pick process with smallest remaining time among arrived
        ready = [(pid, rem[pid]) for pid, at, bt in processes if at <= time and pid not in done]
        if not ready:
            time += 1
            continue

        pid, _ = min(ready, key=lambda x: x[1])
        rem[pid] -= 1

        if rem[pid] == 0:
            ct = time + 1
            done.add(pid)
            completed += 1
            arrival = next(at for p, at, bt in processes if p == pid)
            bt = next(bt for p, at, bt in processes if p == pid)
            tat = ct - arrival
            wt = tat - bt
            result[pid] = (arrival, bt, ct, tat, wt)

        time += 1

    return result


import heapq


def srtf_with_heap(processes):
    """
    processes = [(pid, arrival_time, burst_time)]
    Returns dict: pid → (AT, BT, CT, TAT, WT)
    """
    # Sort by arrival time
    processes = sorted(processes, key=lambda x: x[1])
    n = len(processes)

    # Min-heap: (remaining_time, arrival_time, pid)
    heap = []
    time = 0
    i = 0  # index for arrival
    completed = 0
    result = {}

    # Remaining burst times
    rem = {pid: bt for pid, at, bt in processes}

    while completed < n:

        # Push all processes arriving at current time
        while i < n and processes[i][1] <= time:
            pid, at, bt = processes[i]
            heapq.heappush(heap, (rem[pid], at, pid))
            i += 1

        # If no process is ready, jump to next arrival time
        if not heap:
            time = processes[i][1]
            continue

        # Pop process with smallest remaining time
        rt, at, pid = heapq.heappop(heap)

        # Execute for 1 time unit
        rem[pid] -= 1
        time += 1

        # If still remaining → push back
        if rem[pid] > 0:
            heapq.heappush(heap, (rem[pid], at, pid))
        else:
            # Process finished
            ct = time
            bt = next(b for p, a, b in processes if p == pid)
            tat = ct - at
            wt = tat - bt
            result[pid] = (at, bt, ct, tat, wt)
            completed += 1

    return result

# 📌 Summary Table — Final Interview-Ready Answer
# | SJF Version                         | Time Complexity | Space Complexity | Notes
# | ----------------------------------- | --------------- | ---------------- | ----------------------------------------
# | **Non-Preemptive SJF**              | **O(N²)**       | **O(N)**         | For every process, we scan all processes
# | **Preemptive SJF (SRTF)**           | **O(N²)**       | **O(N)**         | Linear scan every time unit
# | **SRTF (Optimized using Min-Heap)** | **O(N log N)**  | **O(N)**         | Recommended optimized version
