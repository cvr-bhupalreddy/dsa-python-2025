# ✅ Explanation / Features
#
#     Pivot detection: Checks if arr[mid] > arr[mid + 1] → pivot at mid
#     Rotation count: Index of minimum element
#     Min/Max element: Min = arr[min_index], Max = arr[pivot_index]
#     Duplicates: Handled by shrinking high when arr[mid] == arr[high]
#     Fully sorted array: Works with rotation count = 0


def analyze_rotated_array(arr):
    """
    Returns a dictionary with:
    - min_val: minimum element
    - max_val: maximum element
    - pivot_index: index of maximum element
    - rotation_count: index of minimum element
    Works for arrays with or without duplicates.
    """

    low, high = 0, len(arr) - 1

    # Initialize variables
    min_val = arr[0]
    n = len(arr)

    while low < high:
        mid = (low + high) // 2

        # Case 1: mid is pivot if arr[mid] > arr[mid + 1]
        if mid < n - 1 and arr[mid] > arr[mid + 1]:
            pivot_index = mid
            min_index = mid + 1
            min_val = arr[min_index]
            max_val = arr[pivot_index]
            return {
                "min_val": min_val,
                "max_val": max_val,
                "pivot_index": pivot_index,
                "rotation_count": min_index
            }

        # Case 2: Right half unsorted → pivot in right half
        if arr[mid] > arr[high]:
            low = mid + 1

        # Case 3: Left half unsorted or duplicates
        elif arr[mid] < arr[high]:
            high = mid

        else:  # arr[mid] == arr[high], duplicates, shrink high
            high -= 1

    # If we exit the loop, array is fully sorted or single element
    min_index = low
    min_val = arr[min_index]
    pivot_index = (min_index - 1 + n) % n
    max_val = arr[pivot_index]
    rotation_count = min_index

    return {
        "min_val": min_val,
        "max_val": max_val,
        "pivot_index": pivot_index,
        "rotation_count": rotation_count
    }
