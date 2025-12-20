# ✅ Variation-2: Search in Rotated Sorted Array (WITH duplicates)
#
# Why harder?
# Because duplicates break the logic:
#
#     arr[low] == arr[mid] == arr[high]
#
#
# In this case, you cannot decide which half is sorted →
# Shrink both boundaries.
#
#     If arr[low] == arr[mid] == arr[high] → move low++ and high--
#     Otherwise same logic as Variation-1.

def search_rotated_with_duplicates(arr, target):
    low, high = 0, len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == target:
            return True   # only existence

        # If duplicates block identification
        if arr[low] == arr[mid] == arr[high]:
            low += 1
            high -= 1
            continue

        # Left sorted part
        if arr[low] <= arr[mid]:
            if arr[low] <= target < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        # Right sorted part
        else:
            if arr[mid] < target <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False

# 📌 Time Complexity Comparison
# | Variation | Array Type      | Time           | Notes                       |
# | --------- | --------------- | -------------- | --------------------------- |
# | **1**     | No duplicates   | **O(log n)**   | Pure binary search          |
# | **2**     | With duplicates | **Worst O(n)** | Because low++, high-- cases |
