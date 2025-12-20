# ✅ Approach 1 — Backtracking (Swap Method)

def permute_swap(nums):
    result = []

    def backtrack(i):
        if i == len(nums):
            result.append(nums[:])
            return

        for j in range(i, len(nums)):
            nums[i], nums[j] = nums[j], nums[i]  # swap
            backtrack(i + 1)
            nums[i], nums[j] = nums[j], nums[i]  # backtrack (undo swap)

    backtrack(0)
    return result


def permute_swap1(nums):
    result = []

    def backtrack(i):
        print(f"\n---- Enter backtrack(i={i}) ----")
        print("Current nums:", nums)

        if i == len(nums):
            print(">> Reached end, append:", nums)
            result.append(nums[:])
            return

        for j in range(i, len(nums)):
            print(f"\nSwap nums[{i}] and nums[{j}] --> swap {nums[i]} with {nums[j]}")
            nums[i], nums[j] = nums[j], nums[i]
            print("After swap:", nums)

            backtrack(i + 1)

            print(f"Backtrack: undo swap nums[{i}] and nums[{j}]")
            nums[i], nums[j] = nums[j], nums[i]
            print("After undo:", nums)

    backtrack(0)
    return result


if __name__ == "__main__":
    arr = [1, 2, 3]
    print("Input array:", arr)

    perms = permute_swap1(arr)
    print("\n===== FINAL PERMUTATIONS =====")
    for p in perms:
        print(p)


# Approach 2 — Backtracking (Pick Unused Elements)

def permute_pick(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True
                backtrack(path + [nums[i]])
                used[i] = False

    backtrack([])
    return result


def permute_pick1(nums):
    result = []
    used = [False] * len(nums)

    def backtrack(path):
        if len(path) == len(nums):
            result.append(path[:])
            return

        for i in range(len(nums)):
            if not used[i]:
                used[i] = True

                # Explicit ADD
                path.append(nums[i])

                backtrack(path)

                # Explicit REMOVE (undo)
                path.pop()

                used[i] = False

    backtrack([])
    return result


# Example
print(permute_pick([1, 2, 3]))


# Approach 3 — Iterative Using Next Permutation (Lexicographic Order)

def next_permutation(nums):
    i = len(nums) - 2
    while i >= 0 and nums[i] >= nums[i + 1]:
        i -= 1
    if i == -1:
        return False

    j = len(nums) - 1
    while nums[j] <= nums[i]:
        j -= 1

    nums[i], nums[j] = nums[j], nums[i]
    nums[i + 1:] = reversed(nums[i + 1:])
    return True


def permute_iterative(nums):
    nums.sort()
    result = [nums[:]]

    while next_permutation(nums):
        result.append(nums[:])

    return result


# Example
print(permute_iterative([1, 2, 3]))
