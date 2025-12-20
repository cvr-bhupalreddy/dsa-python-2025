# ✅ 1️⃣ Brute Force Approach
# Core Idea
#
#     Scan the array linearly.
#     For each element, check if it is greater than or equal to its neighbors.
#     Return the first element that satisfies the peak property.
#
# Time Complexity: O(n)
# Space Complexity: O(1)

def peak_bruteforce(arr):
    n = len(arr)
    for i in range(n):
        left = arr[i-1] if i > 0 else float('-inf')
        right = arr[i+1] if i < n-1 else float('-inf')
        if arr[i] >= left and arr[i] >= right:
            return i  # returning index of a peak


# ✅ 2️⃣ Better Approach (Linear with Slope Check)
# Core Idea
#
#     Traverse the array and look for uphill → downhill transition.
#     The first index where arr[i] > arr[i+1] is a peak.
#     Handles strictly increasing/decreasing parts efficiently.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


def peak_better(arr):
    n = len(arr)
    for i in range(n-1):
        if arr[i] > arr[i+1]:
            return i
    return n-1  # last element is peak if array is increasing


# CORE IDEA — PEAK ELEMENT USING BINARY SEARCH (O(log n))
#
# 1. At any index mid, compare:
#     arr[mid]  vs  arr[mid + 1]
#
# 2. If arr[mid] < arr[mid + 1]:
#     You are on an ascending slope.
#     A peak MUST lie in the RIGHT half.
#     → move low to mid + 1
#
# 3. Else (arr[mid] >= arr[mid + 1]):
#     You are on a descending slope or at a peak.
#     A peak MUST lie in the LEFT half (including mid).
#     → move high to mid
#
# 4. Continue until low == high.
#     That index is guaranteed to be a peak.

def peak_binary_search(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2
        if arr[mid] < arr[mid + 1]:  # peak on right side
            low = mid + 1
        else:
            high = mid  # peak is on left side Include mid also since we are not comparing mid

    return low  # index of peak element


def all_peaks_binary(arr, low=0, high=None): # multiple peak elements are there
    if high is None:
        high = len(arr) - 1
    peaks = []

    if low > high:
        return peaks

    mid = (low + high) // 2
    left = arr[mid-1] if mid > 0 else float('-inf')
    right = arr[mid+1] if mid < len(arr)-1 else float('-inf')

    # Check if mid is a peak
    if arr[mid] >= left and arr[mid] >= right:
        peaks.append(mid)

    # Recur left and right
    peaks += all_peaks_binary(arr, low, mid-1)
    peaks += all_peaks_binary(arr, mid+1, high)

    return peaks
