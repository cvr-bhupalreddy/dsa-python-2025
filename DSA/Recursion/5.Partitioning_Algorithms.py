# QUICKSORT PARTITIONING ALGORITHMS
# ---------------------------------
#
# 1) LOMUTO PARTITION (Single Pointer)
# ------------------------------------
# Core Idea:
# • Use the last element as pivot.
# • Maintain one pointer 'i' for the boundary of elements < pivot.
# • Scan array with 'j'. If arr[j] < pivot, swap it with arr[i] and move i.
#
# Partition Logic:
#     pivot = arr[high]
# i = low
# for j in range(low, high):
#     if arr[j] < pivot:
# swap(arr[i], arr[j])
# i += 1
# swap(arr[i], arr[high])
# return i   (pivot index)
#
# Good:
# • Very simple.
# Bad:
# • Performs badly on already-sorted arrays.
# • Many swaps.
#
#
# 2) HOARE PARTITION (Two Pointers)
# ---------------------------------
# Core Idea:
# • Choose pivot = arr[low].
# • Use two pointers:
# i → moves right until arr[i] >= pivot
# j → moves left until arr[j] <= pivot
# • Swap arr[i], arr[j] until i >= j.
#
# Partition Logic:
# pivot = arr[low]
# i = low - 1
# j = high + 1
# while True:
#     do i += 1 until arr[i] >= pivot
#     do j -= 1 until arr[j] <= pivot
#     if i >= j: return j
#     swap(arr[i], arr[j])
#
# Good:
# • Fewer swaps.
# • Great performance on average.
# Bad:
# • Pivot returned splits as [low..j] and [j+1..high]
# (not j and j+1 like Lomuto).
# • More complex.
#
#
# 3) DUTCH NATIONAL FLAG PARTITION (3-Way Partition)
# ---------------------------------------------------
# Core Idea:
# • Used when array contains many duplicate elements.
# • Partition into three regions:
# < pivot | == pivot | > pivot
# • Use three pointers: low, mid, high.
#
# Partition Logic:
# pivot = arr[mid]
# low = mid = lowIndex
# high = highIndex
#
# while mid <= high:
#     if arr[mid] < pivot:
#         swap(arr[low], arr[mid])
#         low += 1; mid += 1
#     elif arr[mid] > pivot:
#         swap(arr[mid], arr[high])
#         high -= 1
#     else:
#         mid += 1
#
# Good:
# • Best for many repeated values.
# • Reduces worst-case drastically.
# Bad:
# • Slightly more logic to remember.
#
#
# 4) RANDOMIZED PARTITION
#               ------------------------
# Core Idea:
# • Randomly pick an index between low and high.
# • Swap it with last element.
# • Apply Lomuto partition normally.
#
# Why:
#     • Avoids worst-case O(n²) on sorted arrays.
# • Gives expected O(n log n).
#
# Partition Logic:
# randomIndex = random(low, high)
# swap(arr[randomIndex], arr[high])
# return Lomuto(arr, low, high)
#
#
# 5) MEDIAN OF THREE PARTITION (Improved Pivot Selection)
# --------------------------------------------------------
# Core Idea:
# • Pick pivot as the median of:
# arr[low], arr[mid], arr[high]
# • Reduces chance of bad pivots.
# • Often used with Hoare partition.
#
# Steps:
#     mid = (low+high)//2
# pivot = median(arr[low], arr[mid], arr[high])
# move pivot to front or end and partition normally.
#
# Good:
# • Excellent practical performance.
# • Reduces worst-case occurrences.
# Bad:
# • Extra comparisons.
#
#
# 6) TWO-PASS PARTITION (Stable Partition)
# -----------------------------------------
# Core Idea:
# • First pass: count elements < pivot.
# • Second pass: build two arrays:
# smaller[] and larger[]
# • Merge back.
#
# Steps:
# • Not used in practical quicksort because:
# - Requires extra space O(n)
#                        - Not in-place
#
# Used when:
# • Stability is required (rare in quicksort).
#
#
#   ----------------------------------------
# SUMMARY TABLE
#         ----------------------------------------
# Lomuto       → Simple, more swaps, last-element pivot
# Hoare        → Faster, fewer swaps, dual pointers
# DNF (3-way)  → Best with duplicates
# Randomized   → Prevents worst-case
# Median-3     → Better pivot selection
# 2-pass       → Stable but uses extra space


# def hoare_partition(arr, low, high):
#     pivot = arr[low]  # choose first element as pivot
#     i = low - 1
#     j = high + 1
#
#     while True:
#         # Move i to the right until arr[i] >= pivot
#         i += 1
#         while arr[i] < pivot:
#             i += 1
#
#         # Move j to the left until arr[j] <= pivot
#         j -= 1
#         while arr[j] > pivot:
#             j -= 1
#
#         # If pointers cross, return j (partition index)
#         if i >= j:
#             return j
#
#         # Swap elements at i and j
#         arr[i], arr[j] = arr[j], arr[i]

def hoare_partition(arr, low, high):
    pivot = arr[low]
    i = low - 1
    j = high + 1

    # Loop while pointers have not crossed
    while i < j:

        # Move i to the right
        i += 1
        while arr[i] < pivot:
            i += 1

        # Move j to the left
        j -= 1
        while arr[j] > pivot:
            j -= 1

        # If pointers met or crossed, we stop & return j
        if i >= j:
            return j

        # Swap
        arr[i], arr[j] = arr[j], arr[i]


def quicksort(arr, low, high):
    if low < high:
        p = hoare_partition(arr, low, high)
        quicksort(arr, low, p)  # Note: p (not p-1)
        quicksort(arr, p + 1, high)  # Note: p+1 (not p)


def partition_with_pivot_swap(arr, low, high):
    pivot = arr[low]
    i = low + 1
    j = high

    while True:

        # Move i right until we find an element >= pivot
        while i <= j and arr[i] < pivot:
            i += 1

        # Move j left until we find an element <= pivot
        while i <= j and arr[j] > pivot:
            j -= 1

        # Pointers cross → break
        if i > j:
            break

        # Swap mismatched pair
        arr[i], arr[j] = arr[j], arr[i]

    # Final pivot swap
    arr[low], arr[j] = arr[j], arr[low]

    return j  # pivot index


def quicksort1(arr, low, high):
    if low < high:
        p = partition_with_pivot_swap(arr, low, high)
        quicksort1(arr, low, p - 1)
        quicksort1(arr, p + 1, high)
