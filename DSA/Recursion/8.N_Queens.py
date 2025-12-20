def solve_n_queens(n):
    result = []
    board = [["."] * n for _ in range(n)]

    cols = set()
    diag1 = set()  # row - col
    diag2 = set()  # row + col

    def backtrack(r):
        if r == n:
            # convert board to required format
            result.append(["".join(row) for row in board])
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue  # not safe

            # place queen
            board[r][c] = "Q"
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            # undo
            board[r][c] = "."
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return result


def solve_n_queens_visual(n):
    board = [["."] * n for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()
    result = []

    def backtrack(r):
        print(f"\n>>> Trying row {r}")

        if r == n:
            print("Solution found:")
            result.append(["".join(row) for row in board])
            return

        for c in range(n):
            print(f"Trying position ({r}, {c})...")

            if c in cols:
                print("❌ Same column conflict")
                continue
            if (r - c) in diag1:
                print("❌ Main diagonal conflict")
                continue
            if (r + c) in diag2:
                print("❌ Anti-diagonal conflict")
                continue

            print(f"✔ Placing queen at ({r}, {c})")
            board[r][c] = "Q"

            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            print(f"🔙 Backtracking from ({r}, {c})")
            board[r][c] = "."

            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return result


def solve_n_queens_visual1(n):
    board = [["."] * n for _ in range(n)]
    cols, diag1, diag2 = set(), set(), set()

    def print_board():
        for row in board:
            print(" ".join(row))
        print()

    def backtrack(r):
        print(f"\n>>> Trying row {r}")

        if r == n:
            print("Solution found:")
            print_board()
            return

        for c in range(n):
            print(f"Trying position ({r}, {c})...")

            if c in cols:
                print("❌ Same column conflict")
                continue
            if (r - c) in diag1:
                print("❌ Main diagonal conflict")
                continue
            if (r + c) in diag2:
                print("❌ Anti-diagonal conflict")
                continue

            print(f"✔ Placing queen at ({r}, {c})")
            board[r][c] = "Q"
            print_board()

            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            print(f"🔙 Backtracking from ({r}, {c})")
            board[r][c] = "."
            print_board()

            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)


def count_n_queens(n):
    count = 0
    cols, diag1, diag2 = set(), set(), set()

    def backtrack(r):
        nonlocal count
        if r == n:
            count += 1
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return count


def count_n_queens_distinct(n):
    unique_solutions = set()
    cols, diag1, diag2 = set(), set(), set()
    queen_pos = [-1] * n  # queen_pos[row] = column

    def rotate_90(pos):
        return [pos.index(i) for i in range(n - 1, -1, -1)]

    def reflect_vertical(pos):
        return [n - 1 - c for c in pos]

    def canonical(pos):
        transformations = []
        p = pos[:]
        for _ in range(4):
            p = rotate_90(p)
            transformations.append(tuple(p))
            transformations.append(tuple(reflect_vertical(p)))
        return min(transformations)

    def backtrack(r):
        if r == n:
            c_form = canonical(queen_pos)
            unique_solutions.add(c_form)
            return

        for c in range(n):
            if c in cols or (r - c) in diag1 or (r + c) in diag2:
                continue

            queen_pos[r] = c
            cols.add(c)
            diag1.add(r - c)
            diag2.add(r + c)

            backtrack(r + 1)

            queen_pos[r] = -1
            cols.remove(c)
            diag1.remove(r - c)
            diag2.remove(r + c)

    backtrack(0)
    return len(unique_solutions)


# -------------------------
# MAIN FUNCTION / ENTRY POINT
# -------------------------
if __name__ == "__main__":
    n = 8
    total_distinct = count_n_queens_distinct(n)
    total_sol = count_n_queens(8)
    print(f"Number of distinct {n}-Queens solutions:", total_distinct)
    print(f"Total solutions {n}-Queens solutions:", total_sol)
    # solutions = solve_n_queens_visual(n)
    # print(f"Total solutions for {n}-Queens:", len(solutions))
    # for sol in solutions:
    #     for row in sol:
    #         print(row)
    #     print()