import heapq


def minimumEffortPath(grid):
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')] * m for _ in range(n)]
    dist[0][0] = 0

    heap = [(0, 0, 0)]  # (effort, x, y)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        effort, x, y = heapq.heappop(heap)

        # If reached destination
        if x == n - 1 and y == m - 1:
            return effort

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                next_effort = max(effort, abs(grid[nx][ny] - grid[x][y]))
                if next_effort < dist[nx][ny]:
                    dist[nx][ny] = next_effort
                    heapq.heappush(heap, (next_effort, nx, ny))


def minimumEffortPathWithPath(grid):
    n, m = len(grid), len(grid[0])
    dist = [[float('inf')] * m for _ in range(n)]
    parent = [[None] * m for _ in range(n)]

    dist[0][0] = 0
    heap = [(0, 0, 0)]  # (effort, x, y)
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

    while heap:
        effort, x, y = heapq.heappop(heap)

        if x == n - 1 and y == m - 1:
            # Reconstruct path
            path = []
            while (x, y) is not None:
                path.append((x, y))
                x, y = parent[x][y] if parent[x][y] is not None else (None, None)
            path.reverse()
            return effort, path

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < n and 0 <= ny < m:
                next_effort = max(effort, abs(grid[nx][ny] - grid[x][y]))
                if next_effort < dist[nx][ny]:
                    dist[nx][ny] = next_effort
                    parent[nx][ny] = (x, y)
                    heapq.heappush(heap, (next_effort, nx, ny))

    return -1, []  # unreachable
