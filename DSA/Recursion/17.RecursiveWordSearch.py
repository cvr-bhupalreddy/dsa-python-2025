class Solution:
    def exist(self, board, word):
        n, m = len(board), len(board[0])

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            # boundary or mismatch
            if r < 0 or r >= n or c < 0 or c >= m:
                return False
            if board[r][c] != word[idx]:
                return False

            # mark visited
            temp = board[r][c]
            board[r][c] = '#'     # visited marker

            # explore 4 directions
            found = (dfs(r+1, c, idx+1) or
                     dfs(r-1, c, idx+1) or
                     dfs(r, c+1, idx+1) or
                     dfs(r, c-1, idx+1))

            board[r][c] = temp  # backtrack (unmark)

            return found

        # try starting from every cell
        for i in range(n):
            for j in range(m):
                if dfs(i, j, 0):
                    return True
        return False
