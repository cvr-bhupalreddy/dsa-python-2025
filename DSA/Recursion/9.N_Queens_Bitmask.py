def total_n_queens_bitmask(n):
    count = 0

    def solve(row, cols, diag1, diag2):
        nonlocal count
        if row == n:
            count += 1
            return

        # Positions available for current row
        available = ((1 << n) - 1) & ~(cols | diag1 | diag2)

        while available:
            pos = available & -available  # rightmost 1-bit
            available -= pos               # remove pos from available

            solve(row + 1,
                  cols | pos,
                  (diag1 | pos) << 1,
                  (diag2 | pos) >> 1)

    solve(0, 0, 0, 0)
    return count


# -----------------
# RUN EXAMPLE
# -----------------
if __name__ == "__main__":
    n = 14
    print(f"Total {n}-Queens solutions (bitmask):", total_n_queens_bitmask(n))
