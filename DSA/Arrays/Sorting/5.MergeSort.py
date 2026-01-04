# Merge Sort follows Divide and Conquer:
#
# 1. Divide the array into two halves.
# 2. Recursively sort each half.
# 3. Merge the two sorted halves into one sorted array.
#
# Key points:
#     - Always splits until single-element arrays (which are sorted by definition).
#     - Merge step ensures order.
#     - Stable and in-place with extra O(n) space for merging.


# Divide the array by indices [left, right]:
#     1. Find mid = (left + right) // 2
#     2. Recursively sort left half [left, mid]
#     3. Recursively sort right half [mid+1, right]
#     4. Merge the two sorted halves using merge(arr, left, mid, right)
#
# Advantages:
#     - Avoids extra slicing
#     - Works in-place with temp array for merging
#     - Standard competitive programming style


def merge(arr, left, mid, right):
    """
    Merge two sorted subarrays:
    arr[left..mid] and arr[mid+1..right] into one sorted array
    """
    # Create temporary arrays
    L = arr[left:mid + 1]
    R = arr[mid + 1:right + 1]

    i = j = 0      # Pointers for L and R
    k = left       # Pointer for arr

    # Merge while both arrays have elements
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:   # <= keeps it stable
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copy remaining elements from L (if any)
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copy remaining elements from R (if any)
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, left, right):
    """
    Main Merge Sort function using indices
    """
    if left < right:
        mid = (left + right) // 2
        merge_sort(arr, left, mid)        # Sort left half
        merge_sort(arr, mid + 1, right)   # Sort right half
        merge(arr, left, mid, right)      # Merge sorted halves
