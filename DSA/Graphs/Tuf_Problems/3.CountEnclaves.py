# CORE IDEA
#
# Traverse all boundary cells.
# Whenever a boundary cell is land (1):
# Run DFS/BFS from it
# Mark all connected land as sea (or visited)
# After processing all boundaries:
#     Remaining land cells are enclaves
#     Count remaining land cells
#
# Why it works:
#     Any land connected to boundary can escape
#     Only fully surrounded land cannot escape


def num_enclaves(grid):
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m:
            return
        if grid[r][c] == 0:
            return

        # Mark land as sea (visited)
        grid[r][c] = 0

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Step 1: Remove boundary-connected land
    for i in range(n):
        if grid[i][0] == 1:
            dfs(i, 0)
        if grid[i][m - 1] == 1:
            dfs(i, m - 1)

    for j in range(m):
        if grid[0][j] == 1:
            dfs(0, j)
        if grid[n - 1][j] == 1:
            dfs(n - 1, j)

    # Step 2: Count remaining land
    enclaves = 0
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1:
                enclaves += 1

    return enclaves


def main():
    grid = [
        [0, 0, 0, 0],
        [1, 0, 1, 0],
        [0, 1, 1, 0],
        [0, 0, 0, 0]
    ]

    print("Number of enclave land cells:", num_enclaves(grid))


if __name__ == "__main__":
    main()
