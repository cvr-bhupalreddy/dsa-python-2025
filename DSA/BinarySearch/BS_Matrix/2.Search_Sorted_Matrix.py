# | Approach                            | Use When                                | Complexity |
# | ----------------------------------- | --------------------------------------- | ---------- |
# | **Bruteforce**                      | Matrix small or unsorted                | O(N×M)     |
# | **Better (Staircase)**              | Matrix sorted row-wise + column-wise    | O(N+M)     |
# | **Optimal (Flatten Binary Search)** | Matrix fully sorted like a single array | O(log(NM)) |

def search_matrix_bruteforce(mat, target):
    for row in mat:
        for val in row:
            if val == target:
                return True
    return False


# Core Idea — Copy Ready
#     Start from top-right (or bottom-left).
#     If current value is greater than target → move left
#     If current value is less than target → move down
#     Because every move eliminates one row or one column.


def search_matrix_staircase(mat, target):
    n = len(mat)
    m = len(mat[0])

    r, c = 0, m - 1  # start top-right

    while r < n and c >= 0:
        if mat[r][c] == target:
            return True
        elif mat[r][c] > target:
            c -= 1
        else:
            r += 1

    return False

# Core Idea — Copy Ready
#
# Treat the matrix like a single sorted 1-D array.
# Map mid index → (row, col) using:
#
# row = mid // cols
# col = mid % cols


def search_matrix_binary(mat, target):
    n = len(mat)
    m = len(mat[0])

    low, high = 0, n * m - 1

    while low <= high:
        mid = (low + high) // 2
        r = mid // m
        c = mid % m

        if mat[r][c] == target:
            return True
        elif mat[r][c] < target:
            low = mid + 1
        else:
            high = mid - 1

    return False

