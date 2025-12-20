# Spiral Traversal (Clockwise & Anti-Clockwise)
#
# Approach:
#     Maintain boundaries: top, bottom, left, right
#     Print elements along boundary and shrink
#     Repeat until top > bottom or left > right


def spiral_traversal(mat):
    result = []
    top, bottom = 0, len(mat) - 1
    left, right = 0, len(mat[0]) - 1
    while top <= bottom and left <= right:
        # Top row
        for j in range(left, right + 1):
            result.append(mat[top][j])
        top += 1
        # Right column
        for i in range(top, bottom + 1):
            result.append(mat[i][right])
        right -= 1
        # Bottom row
        if top <= bottom:
            for j in range(right, left - 1, -1):
                result.append(mat[bottom][j])
            bottom -= 1
        # Left column
        if left <= right:
            for i in range(bottom, top - 1, -1):
                result.append(mat[i][left])
            left += 1
    return result


# 9️⃣ Generate Matrix in Spiral Form (1 to n²)
# Approach:
#     Same boundaries as spiral traversal
#     Fill numbers from 1 → n² instead of reading matrix


def generate_spiral_matrix(n):
    mat = [[0] * n for _ in range(n)]
    top, bottom = 0, n - 1
    left, right = 0, n - 1
    num = 1
    while top <= bottom and left <= right:
        for j in range(left, right + 1):
            mat[top][j] = num
            num += 1
        top += 1
        for i in range(top, bottom + 1):
            mat[i][right] = num
            num += 1
        right -= 1
        if top <= bottom:
            for j in range(right, left - 1, -1):
                mat[bottom][j] = num
                num += 1
            bottom -= 1
        if left <= right:
            for i in range(bottom, top - 1, -1):
                mat[i][left] = num
                num += 1
            left += 1
    return mat

# # 10️⃣ Flip Image (Invert + Reverse) – LeetCode 832
#     Flip horizontally (reverse the row)
#     Invert the bits (0 → 1 and 1 → 0)  # to Invert Bits XOR is better suited 1^1 = 0 , 1^0 = 1


# Row before invert: [0, 0, 1]
# Row after invert:  [1, 1, 0]

# Image
# [
#     [1, 1, 0],
#     [1, 0, 1],
#     [0, 0, 0]
# ]

# Inverted Image 
# [
#     [1, 0, 0],
#     [0, 1, 0],
#     [1, 1, 1]
# ]
