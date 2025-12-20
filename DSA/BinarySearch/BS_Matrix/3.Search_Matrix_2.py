# you want Binary Search on a Matrix where:
# Each row is sorted (left → right)
# Each column is sorted (top → bottom)
# BUT the matrix is not globally sorted, so you cannot flatten it and apply binary search on a virtual 1-D array.
# This is the classic "Search in a 2D Matrix II" pattern.


def search_matrix_bruteforce(mat, target):
    for row in mat:
        for val in row:
            if val == target:
                return True
    return False


# ✅ 2. Better (O(N log M)) — Binary Search Each Row

def search_matrix_row_bs(mat, target):
    for row in mat:
        if row[0] <= target <= row[-1]:  # possible row
            # binary search manually
            low, high = 0, len(row) - 1
            while low <= high:
                mid = (low + high) // 2
                if row[mid] == target:
                    return True
                elif row[mid] < target:
                    low = mid + 1
                else:
                    high = mid - 1
    return False


# ✅ 3. Optimal (O(N + M)) — Staircase Search

# Core Idea — Copy Ready
#     Start at top-right corner.
#     If current value > target → move left
#     If current value < target → move down
#     Because each step eliminates one row or one column.

# Why this works:
#     Moving left always decreases values (row sorted).
#     Moving down always increases values (column sorted).

def search_matrix_staircase(mat, target):
    n = len(mat)
    m = len(mat[0])

    r, c = 0, m - 1  # start at top-right

    while r < n and c >= 0:
        if mat[r][c] == target:
            return True
        elif mat[r][c] > target:
            c -= 1
        else:
            r += 1

    return False
