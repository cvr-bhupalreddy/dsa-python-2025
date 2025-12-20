# Given a sorted array of distinct positive integers `arr[]` in strictly increasing order,
# and an integer `k`, find the k-th missing positive integer that is **not present in the array**.
#
# Constraints / Rules:
#
#     1. `arr` is sorted in strictly increasing order.
#     2. `arr` contains **distinct positive integers**.
#     3. Missing numbers are positive integers that **do not appear in the array**.
#     4. The first element of the array does **not necessarily start at 1**.
#     5. The k-th missing number may occur:
#     a) **Before the first element** of the array (e.g., if arr[0] > 1),
#     b) **Between elements** in the array, or
#     c) **After the last element** of the array.
#     6. All numbers are considered in natural increasing order (1, 2, 3, ...).
#
# Goal:
# Return the **k-th missing positive integer** counting from 1.


#
# 1. Missing numbers until arr[i] = arr[i] - (i + 1)
#     - This counts how many numbers are missing up to index i.
# 2. Use binary search to find the **first index where missing_count >= k**
#     - This index acts as an **upper bound**.
# 3. The previous index (index - 1) acts as the **lower bound**.
# 4. If the k-th missing number is after the last element, handle explicitly:
#     - missing_count at last index = arr[-1] - len(arr)
#     - k-th missing number = arr[-1] + (k - missing_count_last)


#  Bruteforce


# Core Idea:
#     - Start with the candidate missing number = k.
#     - Traverse the array:
#     - If arr[i] <= k, then this number is not missing,
#     so shift k to the next possible missing → k = k + 1.
#         - If arr[i] > k, then k is truly missing → return k.
#         - After the loop, return k (it is missing beyond the last element).

def kth_missing_simple(arr, k):
    for num in arr:
        if num <= k:
            k += 1
        else:
            break
    return k


# ✅ 2. Better / Linear Scan Using Gaps — O(N)

# Core Idea:
#     1. Each gap between consecutive elements contributes missing numbers:
#         missing = arr[i] - arr[i-1] - 1
#     2. Traverse array, subtract gaps from k until k <= 0.
#     3. If k still remains after last element, answer = arr[-1] + k.
#     4. If k-th missing is before first element, answer = k.


def kth_missing_linear(arr, k):
    prev = 0  # virtual 0 before first element
    for num in arr:
        missing = num - prev - 1
        if k <= missing:
            return prev + k
        k -= missing
        prev = num
    # k-th missing is after last element
    return arr[-1] + k


# ✅ 3. Optimal — Binary Search — O(log N)
#
# Core Idea:
#     1. Missing numbers until index i = arr[i] - (i + 1)
#     2. Use binary search to find the **first index** where missing_count >= k (upper bound).
#     3. Previous index = lower bound.
#     4. Answer:
#         a) Before array → return k
#         b) After array → return arr[-1] + (k - missing_count_last)
#         c) Between elements → arr[low-1] + k - missing_until(low-1)


def kth_missing_clean(arr, k):
    """
    Find the k-th missing positive number in a sorted array of distinct positive integers.

    Args:
    arr : List[int] - sorted array of distinct positive integers
    k   : int       - k-th missing number to find

    Returns:
    int - k-th missing number
    """
    n = len(arr)

    # Case 1: k-th missing is before the first element
    if k < arr[0]:
        return k

    # Case 2: k-th missing is after the last element
    missing_until_last = arr[-1] - n
    if k > missing_until_last:
        return arr[-1] + (k - missing_until_last)

    # Binary search for k-th missing number between elements
    def missing_until(i):
        # Number of missing numbers until index i
        return arr[i] - (i + 1)

    low, high = 0, n - 1
    while low <= high:  # breaks when high < low => answer is at Array[low-1]
        mid = (low + high) // 2
        if missing_until(mid) < k:
            low = mid + 1
        else:
            high = mid - 1

    # k-th missing is between arr[low-1] and arr[low]
    return arr[low - 1] + k - missing_until(low - 1)


# when above while breaks high < low and , high = low -1
# so  arr[low - 1] + k - missing_until(low - 1) = arr[high] + k -(arr[high] - low)
#  arr[low-1] + k - missing_until(low - 1) = low + k this works for all cases

def kth_missing_simple_clean(arr, k):
    """
    Find the k-th missing positive number in a sorted array of distinct positive integers.

    Args:
    arr : List[int] - sorted array of distinct positive integers
    k   : int       - k-th missing number to find

    Returns:
    int - k-th missing number
    """
    n = len(arr)

    low, high = 0, n - 1

    def missing_until(i):
        # Number of missing numbers until index i
        return arr[i] - (i + 1)

    # Binary search for the first index where missing_until(i) >= k
    while low <= high:
        mid = (low + high) // 2
        if missing_until(mid) < k:
            low = mid + 1
        else:
            high = mid - 1

    # k-th missing number = k + number of elements before it (low)
    return k + low
