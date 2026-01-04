# Shell Sort is a generalization of insertion sort:
#     - Compare elements far apart and move them closer
#     - Reduces overall number of swaps
#     - Gap sequence decreases over iterations (common: n//2, n//4, ..., 1)
#
# Steps:
#     1. Initialize gap = n//2
#     2. Do gapped insertion sort for this gap
#     3. Reduce gap and repeat
#     4. Gap = 1 → regular insertion sort


def shell_sort(arr):
    n = len(arr)
    gap = n // 2

    # Reduce gap until 1
    while gap > 0:
        # Do gapped insertion sort
        for i in range(gap, n):
            temp = arr[i]
            j = i
            while j >= gap and arr[j - gap] > temp:
                arr[j] = arr[j - gap]
                j -= gap
            arr[j] = temp
        gap //= 2
