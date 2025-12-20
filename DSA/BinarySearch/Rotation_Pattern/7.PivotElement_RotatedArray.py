# ✅ 1. Find Pivot (Maximum Element) — No Duplicates
# Core Idea
#     Pivot (max) is the element just before the minimum.
#     If array is not rotated, the last element is the maximum.
#
# Binary search:
#     If arr[mid] > arr[mid + 1] → mid is pivot
#     If arr[mid] >= arr[low] → pivot in right half
#     Else → pivot in left half
#
# Code

def find_pivot(arr):
    low, high = 0, len(arr) - 1

    # Array not rotated
    if arr[low] <= arr[high]:
        return high  # last element is max

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is pivot
        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1


# ✅ 2. Find Pivot (Maximum Element) — With Duplicates
# Core Idea
#
# Duplicates make binary search ambiguous.
#     When arr[mid] == arr[low] == arr[high], shrink boundaries safely:
#     low += 1 or high -= 1 (careful to avoid skipping pivot)
#
# Otherwise same logic as no duplicates.

def find_pivot_with_duplicates(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if mid < len(arr) - 1 and arr[mid] > arr[mid + 1]:
            return mid

        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] < arr[high]:
            high = mid
        else:
            high -= 1  # duplicates, safe shrink

    return high
