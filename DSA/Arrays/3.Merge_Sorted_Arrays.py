# Core Idea
#
# Treat arr1 and arr2 as a single combined array.
# Initialize a gap = ceil((n+m)/2).
#
# Compare elements i and i+gap:
#     If arr[i] > arr[i+gap], swap them.
# Reduce gap: gap = ceil(gap/2)
# Repeat until gap = 0.
#
# This is similar to Shell Sort logic.


import math


def merge_sorted_arrays(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = math.ceil((n + m) / 2)

    while gap > 0:
        i = 0
        j = gap

        while j < n + m:
            # Case 1: both in arr1
            if i < n and j < n:
                if arr1[i] > arr1[j]:
                    arr1[i], arr1[j] = arr1[j], arr1[i]

            # Case 2: i in arr1, j in arr2
            elif i < n <= j:
                if arr1[i] > arr2[j - n]:
                    arr1[i], arr2[j - n] = arr2[j - n], arr1[i]

            # Case 3: both in arr2
            else:
                if arr2[i - n] > arr2[j - n]:
                    arr2[i - n], arr2[j - n] = arr2[j - n], arr2[i - n]

            i += 1
            j += 1

        if gap == 1:
            gap = 0
        else:
            gap = math.ceil(gap / 2)
