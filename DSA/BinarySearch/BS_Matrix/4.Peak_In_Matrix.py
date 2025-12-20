# ✅ 1. Brute Force — O(N × M)
# -----------------------------------------------------
# Core Idea
#
# Check every cell and compare it with its valid neighbors (up/down/left/right).
# If a cell is ≥ all neighbors → it is a peak.

def find_peak_bruteforce(mat):
    n, m = len(mat), len(mat[0])

    for r in range(n):
        for c in range(m):
            val = mat[r][c]

            if (r == 0 or val >= mat[r - 1][c]) and \
                    (r == n - 1 or val >= mat[r + 1][c]) and \
                    (c == 0 or val >= mat[r][c - 1]) and \
                    (c == m - 1 or val >= mat[r][c + 1]):
                return (r, c)

    return None


# ✅ 2. Better — Column-wise Maximum + Check Peak
# -----------------------------------------------------
# Time: O(N × log M)
# Core Idea

# Binary search on columns:
#     Choose mid column
#     Find max element in that column
#     Check if that element is a peak
#     If left neighbor > val → move left
#     Else if right neighbor > val → move right
#     Else this is a peak

def find_peak_better(mat):
    n, m = len(mat), len(mat[0])

    low, high = 0, m - 1

    while low <= high:
        mid = (low + high) // 2

        # Find max element in mid column
        max_row = 0
        for r in range(n):
            if mat[r][mid] > mat[max_row][mid]:
                max_row = r

        val = mat[max_row][mid]

        left = mat[max_row][mid - 1] if mid - 1 >= 0 else -float('inf')
        right = mat[max_row][mid + 1] if mid + 1 < m else -float('inf')

        if val >= left and val >= right:
            return (max_row, mid)

        if left > val:
            high = mid - 1
        else:
            low = mid + 1

    return None

# ⭐⭐⭐ 3. Optimal — O(N log M) (Divide & Conquer)
# -----------------------------------------------------
#
# This is the official optimal method used in most interview problems.
#
# Core Idea
#
# Binary search on columns.
#     For the mid column, find the maximum element.
#     Compare with left and right neighbors:
#     If left > mid → peak lies in left half
#     If right > mid → peak lies in right half
#     Else → mid element is peak.
# This reduces search space by half every step.


def find_peak_optimal(mat):
    n, m = len(mat), len(mat[0])

    low, high = 0, m - 1

    while low <= high:
        mid = (low + high) // 2

        # find max row in this column
        max_row = max(range(n), key=lambda r: mat[r][mid])

        val = mat[max_row][mid]

        left  = mat[max_row][mid-1] if mid > 0     else -float('inf')
        right = mat[max_row][mid+1] if mid < m-1   else -float('inf')

        if val >= left and val >= right:
            return (max_row, mid)

        if left > val:
            high = mid - 1
        else:
            low = mid + 1

    return None
