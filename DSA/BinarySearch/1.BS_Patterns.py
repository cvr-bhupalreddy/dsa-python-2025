# 1) Standard Binary Search
# 📌 Problem: Search Insert Position

def binary_search_iterative(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = low + (high - low) // 2  # avoids overflow

        if arr[mid] == target:
            return mid  # element found
        elif arr[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return -1  # element not found


def binary_search_recursive(arr, target, low=0, high=None):
    if high is None:
        high = len(arr) - 1

    # Base case
    if low > high:
        return -1

    mid = low + (high - low) // 2

    if arr[mid] == target:
        return mid
    elif arr[mid] < target:
        return binary_search_recursive(arr, target, mid + 1, high)
    else:
        return binary_search_recursive(arr, target, low, mid - 1)


# | Approach  | Time Complexity | Space Complexity |
# | --------- | --------------- | ---------------- |
# | Iterative | O(log n)        | O(1)             |
# | Recursive | O(log n)        | O(log n)         |


# 🔶 Variation A — Classic Binary Search with ans variable
# If feasible(mid), store mid in ans and move high = mid – 1
#     ✔️ mid is feasible → record it
#     ✔️ but maybe a smaller feasible exists → search left side
# def binary_search_1(target):
#     low = something
#     high = something
#     ans = large_number
#
#     while low <= high:
#         mid = (low + high)//2
#         if feasible(mid):
#             ans = mid            # store best so far
#             high = mid - 1       # search smaller
#         else:
#             low = mid + 1
#
#     return ans
#
#
# 🔶 Variation B — Shrinking window using high = mid
# If feasible(mid) → search left by doing high = mid
#     ✔️ No need to explicitly store ans
#     ✔️ Loop invariant ensures low ends at the minimum feasible value
# def binary_search_2(target):
#     low = something
#     high = something
#
#     while low < high:
#         mid = (low + high)//2
#         if feasible(mid):
#             high = mid      # mid is feasible → include mid
#         else:
#             low = mid + 1
#
#     return low


# 🟩 Which One Is Better?
# ⭐ Variation B (high = mid) is preferred
#
#     Cleaner
#     No need for ans
#     Most LeetCode editorial patterns use this
#     Perfect for "find the minimum feasible value"
#
# ⭐ Variation A is also correct, but more verbose
#     Needed when the binary search conditions don’t form a perfectly monotonic pattern
#     Very explicit about tracking the “best answer so far”


# 🟨 Summary Comparison Table
# | Feature                               | Variation A (`ans`, high=mid–1`) | Variation B (`high=mid`) |
# | ------------------------------------- | -------------------------------- | ------------------------ |
# | Need `ans` variable?                  | ✔️ Yes                           | ❌ No                     |
# | Loop condition                        | `low <= high`                    | `low < high`               |
# | Standard textbook?                    | ✔️ Yes                           | ✔️ Yes                   |
# | Cleaner & shorter                     | ❌ No                            | ✔️ Yes                   |
# | Recommended for “min feasible value”? | 👍 Works                         | ⭐ **Best choice**        |


# ✅ PATTERN 2 — Find Maximum Feasible Value
# If mid is feasible, go right to maximize.
# ✔ Variation A — Classic (store answer + low = mid + 1)

def find_max_feasible_A(check, low, high):
    ans = low
    while low <= high:
        mid = low + (high - low) // 2
        if check(mid):  # mid is feasible
            ans = mid  # store best so far
            low = mid + 1  # try bigger feasible
        else:
            high = mid - 1  # infeasible → move left
    return ans


# ✔ Variation B — Tight monotonic (low = mid)

def find_max_feasible_B(check, low, high):
    while low < high:
        mid = low + (high - low + 1) // 2  # upper mid avoids infinite loop
        if check(mid):  # feasible → go right
            low = mid
        else:  # infeasible → go left
            high = mid - 1
    return low
