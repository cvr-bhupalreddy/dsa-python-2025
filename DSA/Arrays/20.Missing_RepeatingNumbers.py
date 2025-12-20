# 2️⃣ Better Approach (In-place Negation)
#
# Idea:
# Use the array itself to mark visited numbers by negating the value at index abs(num)-1.
# If index already negative → repeating.
# After marking, the positive index +1 → missing.

# Time: O(n)
# Space: O(1)

def find_missing_repeating(arr):
    repeating = missing = -1
    n = len(arr)

    for i in range(n):
        num = abs(arr[i])
        if arr[num - 1] < 0:
            repeating = num
        else:
            arr[num - 1] *= -1

    for i in range(n):
        if arr[i] > 0:
            missing = i + 1
            break

    return repeating, missing


# 3️⃣ Optimal Approach (Mathematical: Sum and Sum of Squares)
#
# Idea:
#
# Let S = sum(1..n), P = sum of squares of 1..n
# sum(arr) = S - missing + repeating
# sum(arr^2) = P - missing^2 + repeating^2
# Solve the two equations to get missing and repeating.
# Time: O(n)
# Space: O(1)


def find_missing_repeating_1(arr):
    n = len(arr)
    S = n * (n + 1) // 2
    P = n * (n + 1) * (2 * n + 1) // 6

    sum_arr = sum(arr)
    sum_sq_arr = sum(x * x for x in arr)

    diff = S - sum_arr  # missing - repeating
    diff_sq = P - sum_sq_arr  # missing^2 - repeating^2

    missing_plus_repeating = diff_sq // diff
    missing = (diff + missing_plus_repeating) // 2
    repeating = missing - diff
    return repeating, missing
