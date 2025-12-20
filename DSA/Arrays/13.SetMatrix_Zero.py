# 1️⃣ Problem Statement
#
# Given an m x n integer matrix:
#
# If an element is 0, set its entire row and column to 0.
# Do it in-place.


# A. Brute Force (Marking With a Placeholder)
#
# Idea:
# Traverse the matrix, mark all positions that are 0 using a placeholder (like -1 if all elements ≥0).
# Traverse again to set the rows and columns to 0.


def setZeroes_brute(matrix):
    m, n = len(matrix), len(matrix[0])
    to_zero = []

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                to_zero.append((i, j))

    for i, j in to_zero:
        # Set row
        for col in range(n):
            matrix[i][col] = 0
        # Set column
        for row in range(m):
            matrix[row][j] = 0


# B. Better Approach (Use Extra Space for Row & Column Flags)
#
# Idea:
# Maintain two arrays: row_flags and col_flags to track rows & columns that should be zeroed.
# Traverse the matrix to fill flags.
# Update matrix based on flags.

def setZeroes_better(matrix):
    m, n = len(matrix), len(matrix[0])
    row_flag = [False] * m
    col_flag = [False] * n

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == 0:
                row_flag[i] = True
                col_flag[j] = True

    for i in range(m):
        for j in range(n):
            if row_flag[i] or col_flag[j]:
                matrix[i][j] = 0

# C. Optimal Approach (In-Place, O(1) Extra Space)
#
# Idea:
#     Use first row and first column as flags to indicate which rows/columns need to be zeroed.
#     Keep two additional variables for first row and first column themselves to handle overlap.
#     Update the matrix based on these flags.


def setZeroes_optimal(matrix):
    m, n = len(matrix), len(matrix[0])
    first_row_zero = any(matrix[0][j] == 0 for j in range(n))
    first_col_zero = any(matrix[i][0] == 0 for i in range(m))

    # Use first row and column as flags
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][j] == 0:
                matrix[i][0] = 0
                matrix[0][j] = 0

    # Set cells to zero based on flags
    for i in range(1, m):
        for j in range(1, n):
            if matrix[i][0] == 0 or matrix[0][j] == 0:
                matrix[i][j] = 0

    # Update first row and column if needed
    if first_row_zero:
        for j in range(n):
            matrix[0][j] = 0
    if first_col_zero:
        for i in range(m):
            matrix[i][0] = 0
