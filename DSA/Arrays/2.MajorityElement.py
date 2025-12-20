def majority_element(nums):
    candidate, count = None, 0
    for num in nums:
        if count == 0:
            candidate, count = num, 1
        elif num == candidate:
            count += 1
        else:
            count -= 1
    return candidate


# Example:
nums = [3, 3, 4, 2, 3, 3, 1]
print(majority_element(nums))  # Output: 3


# 2️⃣ Majority Element II
# Problem:
#     Find all elements appearing more than n/3 times.
#     There can be at most 2 such elements.


def majority_element_ii(nums):
    if not nums:
        return []

    cand1, cand2, count1, count2 = None, None, 0, 0

    # Step 1: Find 2 candidates
    for num in nums:
        if cand1 == num:
            count1 += 1
        elif cand2 == num:
            count2 += 1
        elif count1 == 0:
            cand1, count1 = num, 1
        elif count2 == 0:
            cand2, count2 = num, 1
        else:
            count1 -= 1
            count2 -= 1

    # Step 2: Verify candidates
    res = []
    for cand in [cand1, cand2]:
        if nums.count(cand) > len(nums) // 3:
            res.append(cand)
    return res


# Example:
nums = [1, 2, 2, 3, 2, 1, 1, 3]
print(majority_element_ii(nums))  # Output: [1,2]
