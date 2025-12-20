# T(n) = 2·T(n/2) + O(n)

# mergeSort(arr, l, r):
#     if l >= r: return
#     mid = (l + r) // 2
#     mergeSort(arr, l, mid)
#     mergeSort(arr, mid+1, r)
#     merge(arr, l, mid, r)


def merge(arr, l, m, r):
    # Create temp arrays
    left = arr[l:m + 1]
    right = arr[m + 1:r + 1]  # slicing operation [ ) => Lower bound included and upper bound excluded

    i = j = 0
    k = l

    # Merge temp arrays back into arr
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left
    while i < len(left):
        arr[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right
    while j < len(right):
        arr[k] = right[j]
        j += 1
        k += 1


def merge_sort(arr, l=0, r=None):
    if r is None:
        r = len(arr) - 1

    if l >= r:
        return

    mid = (l + r) // 2
    merge_sort(arr, l, mid)
    merge_sort(arr, mid + 1, r)
    merge(arr, l, mid, r)
