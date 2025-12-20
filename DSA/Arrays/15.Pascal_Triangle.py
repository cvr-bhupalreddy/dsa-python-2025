import math


def pascal_bruteforce(n):
    triangle = []
    for i in range(n):
        row = []
        for j in range(i + 1):
            val = math.factorial(i) // (math.factorial(j) * math.factorial(i - j))
            row.append(val)
        triangle.append(row)
    return triangle

# C(i,0) = 1
# C(i,j) = C(i,j-1) * (i-j) // (j)

def pascal_better(n):
    triangle = []
    for i in range(n):
        row = []
        val = 1
        for j in range(i+1):
            row.append(val)
            val = val * (i - j) // (j + 1)
        triangle.append(row)
    return triangle


# row[j] = prev_row[j-1] + prev_row[j]

def pascal_optimal(n):
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        if i >= 2:
            for j in range(1, i):
                row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)
    return triangle


# Approach        | Idea                                               | Time    | Space
# -----------------------------------------------------------------------------------------
# Brute           | Use factorial formula nCk                          | O(n³)   | O(1)
# Better          | Compute nCk iteratively using formula              | O(n²)   | O(1)
# Optimal         | Build row from previous row (DP)                   | O(n²)   | O(1)
