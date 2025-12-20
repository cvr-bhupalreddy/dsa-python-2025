# ✅ Lower Bound (Array / Discrete Set)
# Definition:
# - Returns the index of the first element that is greater than or equal to the target.
# - In other words, it is the **smallest element ≥ target**.
# Equivalent Concept:
# - Lower Bound ≡ Least Upper Bound (LUB) ≡ Ceiling
#
# ✅ Upper Bound (Array / Discrete Set)
# Definition:
# - Returns the index of the first element that is strictly greater than the target.
# - In other words, it is the smallest element > target.
# Equivalent Concept:
# - Upper Bound ≡ Strict Least Upper Bound
# - Can be seen as the “next position after LUB” for insertion
#
# ✅ Comparison Table
#
# | Concept          | Meaning in Array                     | Related Math Concept      |
# |-----------------|-------------------------------------|--------------------------|
# | Lower Bound      | First element ≥ target              | LUB / Ceiling            |
# | Upper Bound      | First element > target              | Strict LUB               |
# | GLB / Floor      | Largest element ≤ target            | GLB / Floor              |


def lower_bound(arr, target):  # LUB
    low, high = 0, len(arr)
    while low < high:
        mid = low + (high - low) // 2  # this is to avoid overflow [mid = (low+high)/2]
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low


def upper_bound(arr, target):  # this is Tight Upper bound
    low, high = 0, len(arr)
    while low < high:
        mid = low + (high - low) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low


def insertion_position(arr, target):
    return lower_bound(arr, target)


# | Function                            | Returns                            | Meaning             |
# | ----------------------------------- | ---------------------------------- | ------------------- |
# | **lower_bound(arr, target)**        | first index with `arr[i] ≥ target` | left boundary       |
# | **upper_bound(arr, target)**        | first index with `arr[i] > target` | right boundary      |
# | **insertion_position(arr, target)** | same as lower_bound                | sorted insert index |
