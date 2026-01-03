# 🔹 Shortest Path in a Binary Maze
# 📌 Problem Explanation
#
# You are given a binary matrix (grid) where:
#     1 → cell is walkable
#     0 → cell is blocked
#
# You can move in 4 directions: up, down, left, right
# Each move has a cost = 1
#
# Given:
# source = (sr, sc)
# destination = (dr, dc)
#
# Find the shortest path length from source to destination
#
# If not reachable → return -1


# 1. Use a min-heap (priority queue)
# 2. Store (distance, row, col)
# 3. Start from source with distance = 0
# 4. For each cell:
#     Try all 4 directions
#     If next cell is valid and walkable:
#         relax the distance
# 5. Stop when destination is reached


import heapq


def shortestPathBinaryMaze(grid, src, dest):
    n = len(grid)
    m = len(grid[0])

    sr, sc = src
    dr, dc = dest

    # if source or destination is blocked
    if grid[sr][sc] == 0 or grid[dr][dc] == 0:
        return -1

    # distance matrix initialized to infinity
    dist = [[float('inf')] * m for _ in range(n)]
    dist[sr][sc] = 0

    # min heap -> (distance, row, col)
    pq = [(0, sr, sc)]

    # 4-directional movement
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

    while pq:
        d, r, c = heapq.heappop(pq)

        # if reached destination
        if (r, c) == (dr, dc):
            return d

        # ignore outdated distances
        if d > dist[r][c]:
            continue

        for drn, dcn in directions:
            nr = r + drn
            nc = c + dcn

            if 0 <= nr < n and 0 <= nc < m and grid[nr][nc] == 1:
                new_dist = d + 1

                if new_dist < dist[nr][nc]:
                    dist[nr][nc] = new_dist
                    heapq.heappush(pq, (new_dist, nr, nc))

    return -1
