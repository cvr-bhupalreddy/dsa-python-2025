# Choose last element as pivot
# Partition array so that:
#     left of pivot  → smaller elements
#     right of pivot → larger elements
# After partition:
#     pivot is at correct sorted position
# Recursively sort:
#     left part
#     right part

def partition(arr, low, high):
    pivot = arr[high]        # Choose last element as pivot
    i = low                  # Position for smaller elements

    for j in range(low, high):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place pivot in correct sorted position
    arr[i], arr[high] = arr[high], arr[i]
    return i                 # Pivot index (sorted)


def partition_1(arr, low, high):
    pivot = arr[low]      # Choose first element as pivot
    i = low + 1           # Pointer for elements smaller than pivot

    for j in range(low + 1, high + 1):
        if arr[j] < pivot:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1

    # Place pivot in correct sorted position
    arr[low], arr[i - 1] = arr[i - 1], arr[low]
    return i - 1          # Pivot index (sorted)


def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)

        # Left side (smaller elements)
        quick_sort(arr, low, pivot_index - 1)

        # Right side (larger elements)
        quick_sort(arr, pivot_index + 1, high)


# Quick Sort follows Divide and Conquer.
# Choose a pivot, partition the array so that elements smaller than
# the pivot come to the left and larger ones to the right,
# then recursively sort both sides.

def partition_lomuto_asc(arr, low, high):
    pivot = arr[high]      # choose last element as pivot
    i = low - 1            # boundary for smaller elements

    for j in range(low, high):
        # place smaller elements to the left
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    # place pivot in its correct position
    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_ascending(arr, low, high):
    if low < high:
        p = partition_lomuto_asc(arr, low, high)
        quick_sort_ascending(arr, low, p - 1)
        quick_sort_ascending(arr, p + 1, high)


def partition_lomuto_desc(arr, low, high):
    pivot = arr[high]
    i = low - 1

    for j in range(low, high):
        # reverse comparison
        if arr[j] >= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort_descending(arr, low, high):
    if low < high:
        p = partition_lomuto_desc(arr, low, high)
        quick_sort_descending(arr, low, p - 1)
        quick_sort_descending(arr, p + 1, high)


def partition_hoare_asc(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        # move from left until >= pivot
        i += 1
        while arr[i] < pivot:
            i += 1

        # move from right until <= pivot
        j -= 1
        while arr[j] > pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_hoare_asc(arr, low, high):
    if low < high:
        p = partition_hoare_asc(arr, low, high)
        quick_sort_hoare_asc(arr, low, p)
        quick_sort_hoare_asc(arr, p + 1, high)


def partition_hoare_desc(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    while True:
        i += 1
        while arr[i] > pivot:
            i += 1

        j -= 1
        while arr[j] < pivot:
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i]


def quick_sort_hoare_desc(arr, low, high):
    if low < high:
        p = partition_hoare_desc(arr, low, high)
        quick_sort_hoare_desc(arr, low, p)
        quick_sort_hoare_desc(arr, p + 1, high)
