import heapq

def shortest_path_grid(grid):
    n = len(grid)
    dist = [[float('inf')] * n for _ in range(n)]
    parent = [[None]*n for _ in range(n)]

    dist[0][0] = grid[0][0]
    heap = [(dist[0][0], 0, 0)]
    directions = [(-1,0),(1,0),(0,-1),(0,1)]

    while heap:
        cost, x, y = heapq.heappop(heap)

        if (x, y) == (n-1, n-1):
            # Reconstruct path
            path = []
            while (x, y) is not None:
                path.append((x, y))
                x, y = parent[x][y] if parent[x][y] is not None else (None, None)
            path.reverse()
            return dist[n-1][n-1], path

        if cost > dist[x][y]:
            continue  # stale entry

        for dx, dy in directions:
            nx, ny = x+dx, y+dy
            if 0 <= nx < n and 0 <= ny < n:
                new_cost = cost + grid[nx][ny]
                if new_cost < dist[nx][ny]:
                    dist[nx][ny] = new_cost
                    parent[nx][ny] = (x, y)
                    heapq.heappush(heap, (new_cost, nx, ny))

    return -1, []  # unreachable
