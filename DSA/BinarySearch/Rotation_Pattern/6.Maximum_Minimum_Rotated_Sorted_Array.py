def find_min(arr):
    low, high = 0, len(arr) - 1

    while low <= high:
        # Case 1: Array not rotated
        if arr[low] <= arr[high]:
            return arr[low]

        mid = (low + high) // 2

        # Case 2: Left half sorted → pivot must be in right half
        if arr[mid] >= arr[low]:
            low = mid + 1

        # Case 3: left half unsorted → pivot must be in left half
        else:
            high = mid  # why we are not doing mid-1 here , mid might store minimum so have mid else below code


def find_min_modified(arr):
    low, high = 0, len(arr) - 1
    min_val = float('inf')

    # Early check: array not rotated
    if arr[low] <= arr[high]:
        return arr[low]

    while low <= high:
        mid = (low + high) // 2
        min_val = min(min_val, arr[mid])  # keep track of minimum

        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1  # safe now because min_val stores possible minimum

    return min_val


def find_min_1(arr):
    low, high = 0, len(arr) - 1

    # Early check: array not rotated
    if arr[low] <= arr[high]:
        return arr[low]

    while low < high:
        mid = (low + high) // 2

        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


# ✅ 2. Minimum in Rotated Sorted Array (WITH duplicates)
# Core Idea
#
# Duplicates break strict comparisons.
# When equality blocks decision:
#
#     arr[mid] == arr[high]
#     → shrink high--

# ✔ Final Truth
# Shrinking high is always safe
# Shrinking low is not always safe
#
# → because low may store the true minimum.
#


def find_min_with_duplicates(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        elif arr[mid] < arr[high]:
            high = mid
        else:
            high -= 1  # duplicates case

    return arr[low]


def find_max_no_duplicates(arr):
    low, high = 0, len(arr) - 1

    # Not rotated
    if arr[low] <= arr[high]:
        return arr[high]

    while low <= high:
        mid = (low + high) // 2

        # Check if mid is pivot max
        if arr[mid] > arr[mid + 1]:
            return arr[mid]

        if arr[mid] >= arr[low]:
            low = mid + 1
        else:
            high = mid - 1


def find_max_with_duplicates(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high + 1) // 2  # bias right to avoid infinite loop

        if arr[mid] < arr[low]:
            high = mid - 1
        elif arr[mid] > arr[low]:
            low = mid
        else:
            low += 1  # duplicates case

    return arr[low]
