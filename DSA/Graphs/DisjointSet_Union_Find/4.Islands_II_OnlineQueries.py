# You are given:
#     A grid of size n × m
#     Initially, all cells are water (0)
#     You are given k operations
#     Each operation turns one water cell into land (1)
#     After each operation, you must return how many islands exist.


# What is an Island?
#     An island is a group of connected land cells
#     Connectivity is 4-directional:
#     Up, Down, Left, Right
#     Diagonals do not count


# Why DSU (Union-Find)?
#
# DSU is perfect for dynamic connectivity:
# Each land cell is a node
# When a new land appears:
#     It starts as a new island
#     If neighbors are already land → union them
#     Each successful union reduces island count


# Core DSU Idea
# Add land:
#     islands += 1
#
# For each neighboring land:
#     if they are in different sets:
#         union them
#         islands -= 1


# Mapping 2D → 1D
# We convert (row, col) to a unique DSU index:
# index = row * m + col


# Initialize DSU for n*m cells
# Initialize grid with all water
# Initialize island_count = 0
# Initialize answer list
#
# For each operation (r, c):
#     If cell already land:
#         append island_count
#         continue
#
#     Mark cell as land
#     island_count += 1
#
#     For each 4-direction neighbor:
#     If neighbor is land:
#         If they belong to different DSU sets:
#             union them
#             island_count -= 1
#
# Append island_count to answer

#
# | Aspect | Complexity        |
# | ------ | ----------------- |
# | Time   | O(k α(nm)) ≈ O(k) |
# | Space  | O(nm)             |


def numIslands2(n, m, operations):
    parent = [-1] * (n * m)
    rank = [0] * (n * m)

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        root_x = find(x)
        root_y = find(y)

        if root_x == root_y:
            return False  # already connected

        # union by rank
        if rank[root_x] < rank[root_y]:
            parent[root_x] = root_y
        elif rank[root_x] > rank[root_y]:
            parent[root_y] = root_x
        else:
            parent[root_y] = root_x
            rank[root_x] += 1

        return True

    grid = [[0] * m for _ in range(n)]
    islands = 0
    result = []

    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    for r, c in operations:
        if grid[r][c] == 1:
            result.append(islands)
            continue

        grid[r][c] = 1
        idx = r * m + c
        parent[idx] = idx
        islands += 1

        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                nidx = nr * m + nc
                if union(idx, nidx):
                    islands -= 1

        result.append(islands)

    return result


class DisjointSet:
    def __init__(self, size):
        self.parent = list(range(size))
        self.rank = [0] * size

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        px, py = self.find(x), self.find(y)
        if px == py:
            return False  # already connected

        if self.rank[px] < self.rank[py]:
            self.parent[px] = py
        elif self.rank[px] > self.rank[py]:
            self.parent[py] = px
        else:
            self.parent[py] = px
            self.rank[px] += 1

        return True


class Solution:
    def numIslands2(self, n, m, operators):
        dsu = DisjointSet(n * m)
        grid = [[0] * m for _ in range(n)]
        islands = 0
        result = []

        directions = [(1,0), (-1,0), (0,1), (0,-1)]

        for r, c in operators:
            if grid[r][c] == 1:
                result.append(islands)
                continue

            grid[r][c] = 1
            islands += 1

            node = r * m + c

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                    neighbor = nr * m + nc
                    if dsu.union(node, neighbor):
                        islands -= 1

            result.append(islands)

        return result
