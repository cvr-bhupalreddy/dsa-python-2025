# (Two Pointer + Sort)
# Use two pointers:
#     • i at end of arr1
#     • j at start of arr2
#
# If arr1[i] > arr2[j]:
#     swap them
#     move pointers inward
#
# After all swaps:
#     • arr1 may be unsorted
#     • arr2 may be unsorted
#
# So finally:
#     • sort arr1
#     • sort arr2
import math


def merge_two_sorted_arrays(arr1, arr2):
    """
    Merge two sorted arrays without extra space using
    two pointers and final sorting.
    """

    n = len(arr1)
    m = len(arr2)

    # Pointer i starts from end of arr1
    i = n - 1

    # Pointer j starts from beginning of arr2
    j = 0

    # Step 1: Swap misplaced elements
    while i >= 0 and j < m:
        # If element in arr1 is greater, it belongs to arr2
        if arr1[i] > arr2[j]:
            arr1[i], arr2[j] = arr2[j], arr1[i]
        else:
            # Since arrays are sorted, no more swaps needed
            break

        i -= 1
        j += 1

    # Step 2: Restore sorted order
    arr1.sort()
    arr2.sort()


# ⏱️ Complexity
# | Operation | Complexity           |
# | --------- | -------------------- |
# | Swapping  | O(min(n, m))         |
# | Sorting   | O(n log n + m log m) |
# | Space     | **O(1)**             |


# Use Shell-Sort style GAP method:
#     • Treat both arrays as a single virtual array
#     • Compare elements that are 'gap' distance apart
#     • Swap if out of order
#     • Reduce gap until it becomes 0
#     • Result: both arrays remain sorted in-place


def merge_without_extra_space(arr1, arr2):
    """
    Merges two sorted arrays arr1 and arr2 in-place without using extra space.
    Uses the GAP method (Shell Sort idea).
    """

    n = len(arr1)
    m = len(arr2)

    # Initial gap (ceiling of half of total length)
    gap = math.ceil((n + m) / 2)

    # Continue until gap becomes 0
    while gap > 0:
        i = 0
        j = gap

        # Compare elements gap distance apart
        while j < (n + m):

            # Case 1: both pointers in arr1
            if i < n and j < n:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # Case 2: i in arr1, j in arr2
            elif i < n and j >= n:
                if arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]

            # Case 3: both pointers in arr2
            else:
                if arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

            i += 1
            j += 1

        # Reduce gap
        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)

# 🧠 When to Use Which?
# | Method             | Use When      |
# | ------------------ | ------------- |
# | Two pointer + sort | Simplicity    |
# | GAP method         | Optimal time  |
# | Extra array        | Space allowed |


# | Method                   | Time Complexity           | Space Complexity | Notes                          |
# | ------------------------ | ------------------------- | ---------------- | ------------------------------ |
# | **Two-Pointer + Sort**   | **O(n log n + m log m)**  | **O(1)**         | Simpler, but sorting dominates |
# | **GAP Method (Optimal)** | **O((n + m) log(n + m))** | **O(1)**         | Faster overall, no final sort  |
