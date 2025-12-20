# ✅ 1. Combination Sum I (unlimited use of each number)

def combination_sum_I(nums, target):
    result = []

    def dfs(i, t, path):
        if t == 0:
            result.append(path[:])
            return
        if i == len(nums) or t < 0:
            return

        # pick (stay on same index)
        dfs(i, t - nums[i], path + [nums[i]])  # this is immutable operation , not changing path

        # skip
        dfs(i + 1, t, path)

    dfs(0, target, [])
    return result


# ✅ 2. Combination Sum II (each number once, avoid duplicates)

def combination_sum_II(nums, target):
    nums.sort()
    result = []

    def dfs(i, t, path):
        if t == 0:
            result.append(path[:])
            return
        if i == len(nums) or t < 0:
            return

        # choose nums[i]
        dfs(i + 1, t - nums[i], path + [nums[i]])  # this is immutable operation , not changing path

        # skip all duplicates
        j = i + 1
        while j < len(nums) and nums[j] == nums[i]:
            j += 1

        dfs(j, t, path)

    dfs(0, target, [])
    return result


# ✅ 3. Combination Sum III (pick k numbers from 1..9)
def combination_sum_III(k, target):
    result = []

    def dfs(num, k_left, t, path):
        if k_left == 0:
            if t == 0:
                result.append(path[:])
            return
        if num > 9 or t < 0:
            return

        # pick
        dfs(num + 1, k_left - 1, t - num, path + [num])

        # skip
        dfs(num + 1, k_left, t, path)

    dfs(1, k, target, [])
    return result


# ✅ 4. Combination Sum IV (order matters → permutations)
def combination_sum_IV(nums, target):
    ways = 0

    def dfs(t):
        nonlocal ways
        if t == 0:
            ways += 1
            return
        if t < 0:
            return
        for x in nums:
            dfs(t - x)

    dfs(target)
    return ways


# ✅ 5. Subset Sum (Boolean decision)

def subsets_sum_k(arr, k):
    result = []

    def dfs(index, curr, curr_sum):
        if index == len(arr):
            if curr_sum == k:
                result.append(curr[:])  # make a copy
            return

        # ---- Pick current element ----
        curr.append(arr[index])
        dfs(index + 1, curr, curr_sum + arr[index])
        curr.pop()  # backtrack

        # ---- Skip current element ----
        dfs(index + 1, curr, curr_sum)

    dfs(0, [], 0)
    return result


def subset_sum(nums, target):
    def dfs(i, t):
        if t == 0:
            return True
        if i == len(nums):
            return False
        return dfs(i + 1, t) or dfs(i + 1, t - nums[i])

    return dfs(0, target)


def subsetsWithDup(nums):
    # this code is same as Combination sum except here no sum is involved
    # we will use length to terminate
    nums.sort()
    result = []
    n = len(nums)

    def dfs(i, path):
        # Every path is a valid subset

        if i == n:
            result.append(path[:])
            return

        # ---------- PICK ----------
        dfs(i + 1, path + [nums[i]])

        # ---------- NON-PICK ----------
        # Skip all duplicates for the non-pick branch
        j = i + 1
        while j < n and nums[j] == nums[i]:
            j += 1

        dfs(j, path)

    dfs(0, [])
    return result


def subsets_sum_k_distinct(arr, k):
    arr.sort()  # sort to handle duplicates
    result = []

    def dfs(index, curr, curr_sum):
        if curr_sum == k:
            result.append(curr[:])
            return
        if index == len(arr) or curr_sum > k:
            return

        # ---- Pick current element ----
        curr.append(arr[index])
        dfs(index + 1, curr, curr_sum + arr[index])
        curr.pop()  # backtrack

        # ---- Skip duplicates ----
        next_index = index + 1
        while next_index < len(arr) and arr[next_index] == arr[index]:
            next_index += 1

        # ---- Non-pick / skip current element ----
        dfs(next_index, curr, curr_sum)

    dfs(0, [], 0)
    return result


# ✅ 6. Count Subsets With Sum = Target

def count_subsets(nums, target):
    def dfs(i, t):
        if t == 0:
            return 1
        if i == len(nums):
            return 0
        return dfs(i + 1, t) + dfs(i + 1, t - nums[i])

    return dfs(0, target)


# ✅ 7. Partition Equal Subset Sum

def partition_equal_subset(nums):
    total = sum(nums)
    if total % 2 != 0:
        return False
    target = total // 2

    def dfs(i, t):
        if t == 0:
            return True
        if i == len(nums):
            return False
        return dfs(i + 1, t) or dfs(i + 1, t - nums[i])

    return dfs(0, target)


# ✅ 8. Minimum Difference Partition (Brute Force)

def min_subset_diff(nums):
    total = sum(nums)
    target = total // 2
    best = 0  # store largest subset sum <= target

    def dfs(i, curr):
        nonlocal best
        if curr > target:
            return  # pruning
        if i == len(nums):
            best = max(best, curr)
            return

        # choose nums[i]
        dfs(i + 1, curr + nums[i])

        # skip nums[i]
        dfs(i + 1, curr)

    dfs(0, 0)

    subset1 = best
    subset2 = total - subset1
    return abs(subset1 - subset2)


# ✅ 9. Target Sum (assign + and -)

def target_sum(nums, target):
    ways = 0

    def dfs(i, t):
        nonlocal ways
        if i == len(nums):
            if t == target:
                ways += 1
            return
        dfs(i + 1, t + nums[i])
        dfs(i + 1, t - nums[i])

    dfs(0, 0)
    return ways
