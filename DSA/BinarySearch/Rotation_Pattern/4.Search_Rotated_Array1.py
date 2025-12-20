# ✅ Variation-1: Search in Rotated Sorted Array (NO duplicates)
#
# Problem:
# Given a rotated sorted array (all elements distinct), find the index of target.
#
# Core Idea
#
# At every step, one half is guaranteed sorted.
# Check which half is sorted → decide if target lies inside it → move accordingly.

def search_rotated_no_duplicates(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return mid

        # Left half sorted
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right half sorted
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1
