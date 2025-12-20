from collections import deque

def shortestPathBinaryMaze(grid, source, destination):
    n = len(grid)
    m = len(grid[0])

    # If source or destination is blocked
    if grid[source[0]][source[1]] == 0 or grid[destination[0]][destination[1]] == 0:
        return -1

    # (row, col, distance)
    q = deque([(source[0], source[1], 0)])

    # Directions: up, down, left, right
    directions = [(-1,0), (1,0), (0,-1), (0,1)]

    visited = [[False]*m for _ in range(n)]
    visited[source[0]][source[1]] = True

    while q:
        x, y, dist = q.popleft()

        # If we reached destination
        if (x, y) == destination:
            return dist

        for dx, dy in directions:
            nx, ny = x + dx, y + dy

            if 0 <= nx < n and 0 <= ny < m and not visited[nx][ny] and grid[nx][ny] == 1:
                visited[nx][ny] = True
                q.append((nx, ny, dist + 1))

    return -1  # if destination not reachable
