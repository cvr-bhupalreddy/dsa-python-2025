def solve_surrounded_regions(board):
    if not board or not board[0]:
        return

    n, m = len(board), len(board[0])

    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    def dfs(r, c):
        if r < 0 or r >= n or c < 0 or c >= m:
            return
        if board[r][c] != 'O':
            return

        # Mark as safe
        board[r][c] = 'T'

        for dr, dc in directions:
            dfs(r + dr, c + dc)

    # Step 1: Run DFS from border 'O's
    for i in range(n):
        if board[i][0] == 'O':
            dfs(i, 0)
        if board[i][m - 1] == 'O':
            dfs(i, m - 1)

    for j in range(m):
        if board[0][j] == 'O':
            dfs(0, j)
        if board[n - 1][j] == 'O':
            dfs(n - 1, j)

    # Step 2: Flip surrounded regions
    for i in range(n):
        for j in range(m):
            if board[i][j] == 'O':
                board[i][j] = 'X'
            elif board[i][j] == 'T':
                board[i][j] = 'O'


def main():
    board = [
        ['X', 'X', 'X', 'X'],
        ['X', 'O', 'O', 'X'],
        ['X', 'X', 'O', 'X'],
        ['X', 'O', 'X', 'X']
    ]

    solve_surrounded_regions(board)

    print("Final Board:")
    for row in board:
        print(row)


if __name__ == "__main__":
    main()
