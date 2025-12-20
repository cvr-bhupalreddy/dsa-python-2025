# Use backtracking to explore all valid moves from (row, col).
#
# Steps:
# 1. If (row, col) is out of bounds OR blocked OR already visited → stop.
# 2. If we reach bottom-right cell → record the current path.
# 3. Mark current cell as visited.
# 4. Try all 4 directions in a fixed order:
# Down, Left, Right, Up
# 5. After exploring each direction, unmark visited (backtrack).


def rat_in_maze(maze):
    n = len(maze)
    result = []
    visited = [[False] * n for _ in range(n)]

    # Directions: D, L, R, U
    dirs = [(1, 0, 'D'), (0, -1, 'L'), (0, 1, 'R'), (-1, 0, 'U')]

    def dfs(r, c, path):
        # If out of bounds or blocked or visited → stop
        if r < 0 or c < 0 or r >= n or c >= n:
            return
        if maze[r][c] == 0 or visited[r][c]:
            return

        # If reached destination → add path
        if r == n - 1 and c == n - 1:
            result.append(path)
            return

        # Mark visited
        visited[r][c] = True

        # Explore directions
        for dr, dc, move in dirs:
            dfs(r + dr, c + dc, path + move)

        # Backtrack
        visited[r][c] = False

    # Start only if source cell open
    if maze[0][0] == 1:
        dfs(0, 0, "")

    return result
