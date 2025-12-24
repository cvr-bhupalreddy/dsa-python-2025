def count_islands(grid):
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]

    # 8 possible directions (including diagonals)
    directions = [
        (-1, -1), (-1, 0), (-1, 1),
        ( 0, -1),          ( 0, 1),
        ( 1, -1), ( 1, 0), ( 1, 1)
    ]

    def dfs(row, col):
        visited[row][col] = True
        for dr, dc in directions:
            nr, nc = row + dr, col + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == '1' and not visited[nr][nc]:
                    dfs(nr, nc)

    island_count = 0

    for i in range(n):
        for j in range(m):
            if grid[i][j] == '1' and not visited[i][j]:
                island_count += 1
                dfs(i, j)

    return island_count


def main():
    grid = [
        ['1', '1', '0', '0'],
        ['0', '1', '0', '0'],
        ['1', '0', '1', '1'],
        ['0', '0', '1', '1']
    ]

    result = count_islands(grid)
    print("Number of Islands:", result)


if __name__ == "__main__":
    main()
