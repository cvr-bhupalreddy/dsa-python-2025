# ✅ Task Scheduler Problem — Explanation
# Problem statement
#
# You are given:
#     A list of tasks, each represented by an uppercase letter A–Z
#     A cooling interval n
#     You must schedule tasks so that the same task must have at least n time units between two executions.
#
# Each time unit can:
#     run one task, OR
#     be idle.
#
# You want to compute the minimum total time units needed to finish all tasks.


# Greedy Goal:
#     Always run the task with the highest remaining frequency first (max-heap).
#     After using a task, it must go into a cooling queue for n cycles before it can return.
#     While a task is cooling, you try to run other tasks.
#     If no task is available → you insert idle time.
#
# We use two structures:
#
# 1️⃣ Max-Heap (frequency-based)
#
# Pick the task that appears the most → reduces idle time.
#
# 2️⃣ Queue (for cooling)
#     A queue stores:
#     (task_frequency_after_exec, time_when_available)

import heapq
from collections import deque


def leastInterval(tasks, n):
    # Step 1: Manual frequency array
    freq = [0] * 26
    for t in tasks:
        freq[ord(t) - ord('A')] += 1

    # Step 2: Build max heap (negative values)
    max_heap = []
    for f in freq:
        if f > 0:
            heapq.heappush(max_heap, -f)

    # Step 3: Cooling queue: (time_available, remaining_freq)
    cool = deque()
    time = 0

    while max_heap or cool:
        time += 1

        # Execute a task if possible
        if max_heap:
            cnt = heapq.heappop(max_heap) + 1  # +1 towards 0
            if cnt != 0:
                # Put in cooling queue
                cool.append((time + n, cnt))

        # Check if cooling queue head is ready
        if cool and cool[0][0] == time:
            available_time, freq_left = cool.popleft()
            heapq.heappush(max_heap, freq_left)

    return time
