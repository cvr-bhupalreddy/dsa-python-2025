# PROBLEM SUMMARY
#
# You are given an n x m grid:
#
# 0 → Empty cell
# 1 → Fresh orange
# 2 → Rotten orange
#
# Rules:
#
# Every minute, a fresh orange becomes rotten if it is 4-directionally adjacent to a rotten orange.
# Return the minimum number of minutes until no fresh orange remains.
# If it is impossible, return -1.


# CORE IDEA (COPY-READY)
# Add all initially rotten oranges to a queue.
# Count the number of fresh oranges.
#
# Perform BFS:
#     For each minute, process all currently rotten oranges.
#     Rot adjacent fresh oranges.
#     Decrease fresh count.
#     Increment time after each BFS level.
# If fresh oranges remain → return -1
#
# Else → return time


from collections import deque


def oranges_rotting(grid):
    if not grid or not grid[0]:
        return -1

    rows, cols = len(grid), len(grid[0])
    queue = deque()
    fresh = 0

    # Step 1: Initialize queue with all rotten oranges
    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 2:
                queue.append((r, c))
            elif grid[r][c] == 1:
                fresh += 1

    # If no fresh oranges, time needed is 0
    if fresh == 0:
        return 0

    minutes = 0
    directions = [
        (-1, 0),  # up
        (1, 0),  # down
        (0, -1),  # left
        (0, 1)  # right
    ]

    # Step 2: BFS
    while queue and fresh > 0:
        for _ in range(len(queue)):
            r, c = queue.popleft()

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols:
                    if grid[nr][nc] == 1:
                        grid[nr][nc] = 2
                        fresh -= 1
                        queue.append((nr, nc))

        minutes += 1

    return minutes if fresh == 0 else -1


def main():
    grid = [
        [2, 1, 1],
        [1, 1, 0],
        [0, 1, 1]
    ]

    print("Minimum minutes:", oranges_rotting(grid))


if __name__ == "__main__":
    main()
