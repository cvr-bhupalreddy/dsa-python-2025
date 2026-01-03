# ✅ Problem
#
# You are given an n × n binary grid:
#     1 → land
#     0 → water
#
# An island is a group of 1s connected up, down, left, or right.
#
# You are allowed to:
# 👉 Change at most ONE 0 into 1
#
# Your task:
#     Return the maximum possible island size after this one optional change


# 🧠 Core DSU Idea
# Step 1: Build DSU for existing 1s
#     Treat each cell as a node: id = row * n + col
#     Union adjacent 1s
#     Maintain component size
#
# Step 2: Try flipping each 0
#     Look at its 4 neighbors
#     Collect unique parent components
#     New island size = 1 + sum(sizes of unique neighbors)
#
# Step 3: Track the maximum result


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            px, py = py, px
        self.parent[py] = px
        self.size[px] += self.size[py]


def largestIsland(grid):
    n = len(grid)
    dsu = DSU(n * n)
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    # Step 1: Union all existing land
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 1:
                idx = r * n + c
                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        dsu.union(idx, nr * n + nc)

    # Track current max island (in case no 0 flip helps)
    max_island = max(dsu.size[dsu.find(i)] for i in range(n * n) if grid[i // n][i % n] == 1) if any(
        1 in row for row in grid) else 0

    # max_island = 0
    #
    # # Check if there is any 1 in the grid
    # has_land = False
    # for row in grid:
    #     if 1 in row:
    #         has_land = True
    #         break
    #
    # if has_land:
    #     for i in range(n * n):
    #         r = i // n
    #         c = i % n
    #         if grid[r][c] == 1:
    #             root = dsu.find(i)
    #             island_size = dsu.size[root]
    #             if island_size > max_island:
    #                 max_island = island_size
    # else:
    #     max_island = 0

    # Step 2: Try flipping each 0
    for r in range(n):
        for c in range(n):
            if grid[r][c] == 0:
                seen = set()
                new_size = 1  # flipping this 0

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if 0 <= nr < n and 0 <= nc < n and grid[nr][nc] == 1:
                        parent = dsu.find(nr * n + nc)
                        if parent not in seen:
                            seen.add(parent)
                            new_size += dsu.size[parent]

                max_island = max(max_island, new_size)

    return max_island


class Solution:
    pass
