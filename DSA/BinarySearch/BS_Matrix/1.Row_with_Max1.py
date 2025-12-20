def row_with_max_ones_bruteforce(mat):
    max_row = -1
    max_ones = 0

    for i, row in enumerate(mat):
        count = sum(row)
        if count > max_ones:
            max_ones = count
            max_row = i

    return max_row


# ✅ APPROACH 2 — Better (Binary Search per Row)
#
# Because each row is sorted, find the first 1 using binary search.
#
# Number of 1s = M – firstOneIndex
# Time → O(N × log M)

import bisect


def row_with_max_ones_binary(mat):
    max_row = -1
    max_ones = 0

    for i, row in enumerate(mat):
        idx = bisect.bisect_left(row, 1)
        ones = len(row) - idx

        if ones > max_ones:
            max_ones = ones
            max_row = i

    return max_row


def row_with_max_ones_binary_better(mat):
    n = len(mat)
    m = len(mat[0])

    def first_one_index(row):
        low, high = 0, m - 1
        first = m  # default = no 1's found

        while low <= high:
            mid = (low + high) // 2

            if row[mid] == 1:
                first = mid  # possible first 1
                high = mid - 1  # go left
            else:
                low = mid + 1  # go right

        return first

    max_row = -1
    max_ones = 0

    for i in range(n):
        idx = first_one_index(mat[i])
        ones = m - idx

        if ones > max_ones:
            max_ones = ones
            max_row = i

    return max_row

# ⭐ APPROACH 3 — Optimal (Top-Right Walk / Staircase Search)
# This is the best solution.
# Logic
#     Start from top-right corner:
#     If you see 1, move left
#     If you see 0, move down
#     This works because rows are sorted.


def row_with_max_ones_optimal(mat):
    n = len(mat)
    m = len(mat[0])

    row = 0
    col = m - 1
    max_row = -1

    while row < n and col >= 0:
        if mat[row][col] == 1:
            max_row = row
            col -= 1      # move left
        else:
            row += 1      # move down

    return max_row


# | Approach    | Description                   | Time         | Space |
# | ----------- | ----------------------------- | ------------ | ----- |
# | **Brute**   | Count 1s row by row           | O(NM)        | O(1)  |
# | **Better**  | Binary search first 1 per row | O(N log M)   | O(1)  |
# | **Optimal** | Top-right pointer walk        | **O(N + M)** | O(1)  |
