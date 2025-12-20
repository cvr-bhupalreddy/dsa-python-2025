# ✅ 1. Brute Force Approach (Merge + Track)
# Core Idea:
#     Merge the two sorted arrays into a new sorted array.
#     Return the (k–1)th element of the merged array.

def kth_bruteforce(A, B, k):
    i = j = 0
    merged = []

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            merged.append(A[i]);
            i += 1
        else:
            merged.append(B[j]);
            j += 1

    merged.extend(A[i:])
    merged.extend(B[j:])

    return merged[k - 1]


# ✅ 2. Better Approach (Two-Pointer Without Extra Space)
#     Use two pointers like merge-sort.
#     Increment the pointer of the smaller element.
#     Stop when we reach the k-th popped element.
#     No need to store the entire merged array.

def kth_better(A, B, k):
    i = j = 0
    count = 0
    val = -1

    while i < len(A) and j < len(B):
        if A[i] < B[j]:
            val = A[i];
            i += 1
        else:
            val = B[j];
            j += 1
        count += 1
        if count == k:
            return val

    # If A still has elements
    while i < len(A):
        val = A[i];
        i += 1
        count += 1
        if count == k:
            return val

    # If B still has elements
    while j < len(B):
        val = B[j];
        j += 1
        count += 1
        if count == k:
            return val


def kth_optimal(A, B, k):
    if len(A) > len(B):
        return kth_optimal(B, A, k)

    m, n = len(A), len(B)
    low = max(0, k - n)
    high = min(k, m)

    while low <= high:
        i = (low + high) // 2  # elements from A
        j = k - i  # elements from B [In median case we need [(n1+n2+1)/2 ] elements on left side , for this case K ele

        A_left = float('-inf') if i == 0 else A[i - 1]
        A_right = float('inf') if i == m else A[i]
        B_left = float('-inf') if j == 0 else B[j - 1]
        B_right = float('inf') if j == n else B[j]

        if A_left <= B_right and B_left <= A_right:
            return max(A_left, B_left)

        elif A_left > B_right:
            high = i - 1
        else:
            low = i + 1


# ✅ Median via K-th Element
def kth_element(A, B, k):
    i = j = 0

    while True:
        if i == len(A):
            return B[j + k - 1]
        if j == len(B):
            return A[i + k - 1]
        if k == 1:
            return min(A[i], B[j])

        half = k // 2
        new_i = min(i + half, len(A)) - 1
        new_j = min(j + half, len(B)) - 1

        if A[new_i] <= B[new_j]:
            k -= (new_i - i + 1)
            i = new_i + 1
        else:
            k -= (new_j - j + 1)
            j = new_j + 1


def find_median_sorted_arrays(A, B):
    total = len(A) + len(B)

    if total % 2 == 1:
        return kth_element(A, B, total // 2 + 1)
    else:
        left = kth_element(A, B, total // 2)
        right = kth_element(A, B, total // 2 + 1)
        return (left + right) / 2
