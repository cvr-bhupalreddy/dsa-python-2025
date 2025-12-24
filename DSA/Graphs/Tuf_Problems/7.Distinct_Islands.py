# Given an N x M binary grid:
#
# 1 → land
# 0 → water
#
# Task:
#     Count the number of distinct islands
#     Two islands are considered same if the shape (relative arrangement of 1s) is identical
#     Rotations or reflections are NOT allowed
#
# Connectivity:
#     4-directional (up, down, left, right)


# CORE IDEA
#
# Traverse the grid.
# When a land cell (1) is found, start DFS/BFS.
# Record the relative coordinates of all land cells with respect to the starting cell.
#     This is the canonical shape of the island
#     For example, if starting at (i0,j0) and visiting (i1,j1), record (i1-i0, j1-j0)
# Convert the shape into a tuple of coordinates and store in a set of shapes.
# After traversing the entire grid, the size of the set = number of distinct islands.
#
# Why it works:
# By storing relative positions, islands with same shape are recognized regardless of position in grid.


def num_distinct_islands(grid):
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    shapes = set()

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    def dfs(r, c, r0, c0, shape):
        visited[r][c] = True
        # Record relative position
        shape.append((r - r0, c - c0))

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr, nc, r0, c0, shape)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                shape = []
                dfs(i, j, i, j, shape)
                # Use tuple to store in set
                shapes.add(tuple(shape))

    return len(shapes)


def main():
    grid = [
        [1,1,0,0,0],
        [1,1,0,0,0],
        [0,0,0,1,1],
        [0,0,0,1,1]
    ]

    print("Number of distinct islands:", num_distinct_islands(grid))


if __name__ == "__main__":
    main()
