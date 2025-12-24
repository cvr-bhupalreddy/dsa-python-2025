from collections import deque


def nearest_one_distance(grid):
    n, m = len(grid), len(grid[0])
    dist = [[-1] * m for _ in range(n)]
    queue = deque()

    # Step 1: Push all 1s into queue
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                dist[i][j] = 0
                queue.append((i, j))

    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1)  # right
    ]

    # Step 2: BFS
    while queue:
        r, c = queue.popleft()
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    queue.append((nr, nc))

    return dist


def main():
    grid = [
        [0, 1, 1],
        [1, 1, 0],
        [0, 0, 1]
    ]

    result = nearest_one_distance(grid)

    print("Distance Matrix:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
