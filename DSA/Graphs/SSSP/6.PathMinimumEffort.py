# 🔹 Path With Minimum Effort
# 📌 Problem Explanation
#
# You are given a 2D grid heights where:
#     heights[i][j] = height of the cell
# You start at top-left (0,0)
# You want to reach bottom-right (n-1, m-1)
# You can move up, down, left, right
#
# 🔹 What is "Effort"?
# The effort of a path is defined as:
# The maximum absolute difference in heights between any two consecutive cells along the path.

# 🔹 Why This Is NOT a Normal Shortest Path
# | Standard Shortest Path  | Minimum Effort Path          |
# | ----------------------- | ---------------------------- |
# | Minimize sum of weights | Minimize maximum edge weight |
# | Uses `+`                | Uses `max()`                 |
# | Distance accumulates    | Bottleneck minimization      |


# effort[r][c] = minimum effort required to reach cell (r,c)
#
# new_effort = max(current_effort, abs(height_diff))

# 1. Use Dijkstra with min-heap
# 2. Start at (0,0) with effort = 0
# 3. For each neighbor:
#     effort = max(current_effort, height_diff)
# 4. Choose the path that minimizes this effort
# 5. Stop when destination is reached


import heapq


def minimumEffortPath(heights):
    n = len(heights)
    m = len(heights[0])

    # effort[r][c] = minimum effort to reach (r,c)
    effort = [[float('inf')] * m for _ in range(n)]
    effort[0][0] = 0

    # min heap: (effort, row, col)
    pq = [(0, 0, 0)]

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while pq:
        curr_effort, r, c = heapq.heappop(pq)

        # destination reached
        if r == n - 1 and c == m - 1:
            return curr_effort

        # skip outdated entry
        if curr_effort > effort[r][c]:
            continue

        for dr, dc in directions:
            nr, nc = r + dr, c + dc

            if 0 <= nr < n and 0 <= nc < m:
                diff = abs(heights[r][c] - heights[nr][nc])
                new_effort = max(curr_effort, diff)

                if new_effort < effort[nr][nc]:
                    effort[nr][nc] = new_effort
                    heapq.heappush(pq, (new_effort, nr, nc))

    return 0

# 🔹 Time & Space Complexity
# | Metric | Complexity           |
# | ------ | -------------------- |
# | Nodes  | `n × m`              |
# | Time   | `O((n×m) log (n×m))` |
# | Space  | `O(n×m)`             |


# 🔹 Why Dijkstra Works Here
# | Property            | Reason                            |
# | ------------------- | --------------------------------- |
# | Non-decreasing cost | `max()` never decreases           |
# | Greedy choice       | Lowest effort node expanded first |
# | No negative weights | Absolute differences ≥ 0          |
