# 1️⃣ Problem Recap
#
# Rearrange the array so that positive and negative numbers alternate. Extra positives or negatives appear at the end.


def rearrange_by_sign(nums):
    pos = [x for x in nums if x >= 0]
    neg = [x for x in nums if x < 0]

    result = []
    i = j = 0
    # alternate insertion
    while i < len(pos) and j < len(neg):
        result.append(neg[j])
        result.append(pos[i])
        i += 1
        j += 1

    # append remaining elements
    while j < len(neg):
        result.append(neg[j])
        j += 1
    while i < len(pos):
        result.append(pos[i])
        i += 1

    return result

#
# 5️⃣ Optimal In-Place Approach (Without Extra Space)
#
# Partition negatives and positives using a variant of partitioning logic (like QuickSort).
# Then, starting from first index, swap alternate elements until alternating pattern is achieved.
#
# Time Complexity: O(n)
# Space Complexity: O(1)


# ✅ Key Points
# Maintain relative order if needed → use extra space.
# Without extra space → only approximate alternating order possible.


# How it Works
#
# i → next position for negative number
# j → current element being checked


def rearrange_by_sign_inplace(nums):
    n = len(nums)
    # Step 1: Partition negatives to left, positives to right
    i, j = 0, 0
    while j < n:
        if nums[j] < 0:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
        j += 1

    # i = index of first positive element
    neg_index, pos_index = 0, i

    # Step 2: Swap alternate elements
    while neg_index < pos_index < n and nums[neg_index] < 0:
        nums[neg_index], nums[pos_index] = nums[pos_index], nums[neg_index]
        neg_index += 2
        pos_index += 1

    return nums
