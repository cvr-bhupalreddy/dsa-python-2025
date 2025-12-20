def single_non_duplicate_bruteforce(arr):
    n = len(arr)

    # Check pairs one by one
    for i in range(0, n - 1, 2):
        if arr[i] != arr[i + 1]:
            return arr[i]

    # If all pairs matched, the last element is the unique one
    return arr[-1]


def single_number(nums):
    """
    Returns the single element that appears once while all others appear twice.
    Example: [2,2,1,3,3] -> 1
    """
    res = 0
    for x in nums:
        res ^= x
    return res


# Example
print(single_number([2, 2, 1, 3, 3]))  # prints 1


# CORE IDEA — FIND SINGLE ELEMENT IN SORTED ARRAY (EVERY OTHER ELEMENT APPEARS TWICE)
#
# 1. In a valid sorted array:
#     Before the single element:
#         pairs appear as (even index, odd index):
#             arr[0] == arr[1]
#             arr[2] == arr[3]
#             arr[4] == arr[5]
# ...
#     After the single element:
#         the pair alignment flips:
#             arr[odd] == arr[even]
#
# 2. Binary Search Trick:
# • Always force mid to be EVEN index (mid -= 1 if mid is odd)
# • Compare arr[mid] with arr[mid + 1]:
#     If they form a correct pair → single is on the RIGHT side
#     Else → single is on the LEFT side (including mid)
#
# 3. When low == high → that index holds the single element.
#
# Time: O(log n)
# Space: O(1)


def single_non_duplicate(arr):
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        # Ensure mid always points to an EVEN index
        # because pairs are (even, odd)
        if mid % 2 == 1:
            mid -= 1

        # If arr[mid] and arr[mid+1] form a valid pair
        if arr[mid] == arr[mid + 1]:
            # Single element must be in the right half
            # Skip both indices: mid and mid+1
            low = mid + 2
        else:
            # Pair is broken → single is on left (including mid)
            high = mid

    # low == high → single element index
    return arr[low]


def singleNonDuplicate(self, nums):
    n = len(nums) # Size of the array.

    # Edge cases:
    if n == 1:
        return nums[0]
    if nums[0] != nums[1]:
        return nums[0]
    if nums[n - 1] != nums[n - 2]:
        return nums[n - 1]

    low, high = 1, n - 2
    while low <= high:
        mid = (low + high) // 2

        # If nums[mid] is the single element:
        if nums[mid] != nums[mid + 1] and nums[mid] != nums[mid - 1]:
            return nums[mid]

        # We are in the left part:
        if (mid % 2 == 1 and nums[mid] == nums[mid - 1]) or (mid % 2 == 0 and nums[mid] == nums[mid + 1]):
            # Eliminate the left half:
            low = mid + 1
        # We are in the right part:
        else:
            # Eliminate the right half:
            high = mid - 1

    # Dummy return statement:
    return -1