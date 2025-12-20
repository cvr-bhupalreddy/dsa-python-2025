# For each empty cell (i,j):
# Try digits '1' to '9':
# If placing digit is valid in row, column, and 3x3 box:
# Place digit
# Recurse to next cell
# If stuck, backtrack (reset cell to '.')
# Stop when all cells are filled


def solve_sudoku(board):
    def is_valid(r, c, ch):
        # Check row
        for j in range(9):
            if board[r][j] == ch:
                return False
        # Check column
        for i in range(9):
            if board[i][c] == ch:
                return False
        # Check 3x3 box
        start_r, start_c = 3 * (r // 3), 3 * (c // 3)
        for i in range(start_r, start_r + 3):
            for j in range(start_c, start_c + 3):
                if board[i][j] == ch:
                    return False
        return True

    def is_valid_optimal(r, c, ch):
        # Starting row and column of the 3x3 box
        start_r = 3 * (r // 3)
        start_c = 3 * (c // 3)

        for k in range(9):
            # Row check
            if board[r][k] == ch:
                return False

            # Column check
            if board[k][c] == ch:
                return False

            # Convert k into 3x3 box coordinates
            br = start_r + (k // 3)
            bc = start_c + (k % 3)

            # Box check
            if board[br][bc] == ch:
                return False

        return True

    def backtrack():
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    for ch in '123456789':
                        if is_valid(i, j, ch):
                            board[i][j] = ch
                            if backtrack():
                                return True
                            board[i][j] = '.'  # backtrack
                    return False  # no valid number found
        return True  # all cells filled

    backtrack()
    return board
