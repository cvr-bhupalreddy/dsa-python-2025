def transpose_inplace(mat):
    n = len(mat)
    for i in range(n):  # n-1 is enough
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]


def transpose_extra(mat):
    n = len(mat)
    m = len(mat[0])
    T = [[0] * n for _ in range(m)]
    for i in range(n):
        for j in range(m):
            T[j][i] = mat[i][j]
    return T


def rotate90_clockwise(mat):
    n = len(mat)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Reverse rows
    for row in mat:
        row.reverse()


def rotate180(mat):
    n = len(mat)
    # Reverse rows
    mat.reverse()
    # Reverse columns
    for i in range(n):
        mat[i].reverse()


def rotate270_clockwise(mat):
    n = len(mat)
    # Transpose
    for i in range(n):
        for j in range(i + 1, n):
            mat[i][j], mat[j][i] = mat[j][i], mat[i][j]
    # Reverse columns
    for j in range(n):  # Two pointer on each col
        top, bottom = 0, n - 1
        while top < bottom:
            mat[top][j], mat[bottom][j] = mat[bottom][j], mat[top][j]
            top += 1
            bottom -= 1


def reverse_rows(mat):
    for row in mat:
        row.reverse()


def reverse_columns(mat):
    n = len(mat)
    for j in range(len(mat[0])):
        top, bottom = 0, n - 1
        while top < bottom:
            mat[top][j], mat[bottom][j] = mat[bottom][j], mat[top][j]
            top += 1
            bottom -= 1


# 6️⃣ Matrix Reflection (Horizontal / Vertical / Diagonal)
#
# Approach:
#     Horizontal: Reverse all rows (flip top ↔ bottom)
#     Vertical: Reverse all columns (flip left ↔ right)
#     Main diagonal: Transpose
#     Anti-diagonal: Transpose + reverse rows & columns

def reflect_horizontal(mat):
    mat.reverse()


def reflect_vertical(mat):
    reverse_columns(mat)


def reflect_main_diagonal(mat):
    transpose_inplace(mat)


def reflect_anti_diagonal(mat):
    transpose_inplace(mat)
    reflect_vertical(mat)
    reflect_horizontal(mat)


# 7️⃣ Check if Two Matrices are Rotations of Each Other
#
# Approach:
#     Check if matrix B equals A rotated by 0°, 90°, 180°, 270° clockwise


def are_rotations(A, B):
    import copy
    mat = copy.deepcopy(A)
    for _ in range(4):
        rotate90_clockwise(mat)
        if mat == B:
            return True
    return False


# Idea 1: Use a helper function to return a rotated matrix instead of modifying in-place

def rotate90_clockwise_copy(mat):
    n = len(mat)
    # create new matrix
    rotated = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            rotated[j][n - 1 - i] = mat[i][j]
    return rotated


def are_rotations_1(A, B):
    mat = A  # no deepcopy
    for _ in range(4):
        mat = rotate90_clockwise_copy(mat)
        if mat == B:
            return True
    return False
