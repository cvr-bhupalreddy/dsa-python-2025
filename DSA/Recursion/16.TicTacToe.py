# We use the Minimax Algorithm.
#
# 1. If current board is a terminal state:
# - X wins → return +1
# - O wins → return -1
# - Draw → return 0
#
# 2. If it is X's turn:
# - Try all empty cells by placing X
# - Recursively evaluate using minimax
# - Choose the move with maximum score
#
# 3. If it is O's turn:
# - Try all empty cells by placing O
# - Recursively evaluate using minimax
# - Choose the move with minimum score
#
# 4. The best move for the current player is the one
# that leads to max (for X) or min (for O) score.


def check_winner(board):
    # Check rows, cols, diagonals
    lines = []

    # rows
    for r in range(3):
        lines.append(board[r])

    # cols
    for c in range(3):
        lines.append([board[r][c] for r in range(3)])

    # diagonals
    lines.append([board[i][i] for i in range(3)])
    lines.append([board[i][2 - i] for i in range(3)])

    if ['X', 'X', 'X'] in lines:
        return 'X'
    if ['O', 'O', 'O'] in lines:
        return 'O'
    return None


def minimax(board, is_x_turn):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    if winner == 'O':
        return -1

    # check draw
    if all(board[r][c] != ' ' for r in range(3) for c in range(3)):
        return 0

    best_score = -float('inf') if is_x_turn else float('inf')

    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                # try move
                board[r][c] = 'X' if is_x_turn else 'O'
                score = minimax(board, not is_x_turn)
                board[r][c] = ' '  # undo

                if is_x_turn:
                    best_score = max(best_score, score)
                else:
                    best_score = min(best_score, score)

    return best_score


def best_move(board, player):
    is_x_turn = (player == 'X')
    best_score = -float('inf') if is_x_turn else float('inf')
    move = None

    for r in range(3):
        for c in range(3):
            if board[r][c] == ' ':
                board[r][c] = player
                score = minimax(board, not is_x_turn)
                board[r][c] = ' '

                if player == 'X':
                    if score > best_score:
                        best_score = score
                        move = (r, c)
                else:
                    if score < best_score:
                        best_score = score
                        move = (r, c)

    return move
