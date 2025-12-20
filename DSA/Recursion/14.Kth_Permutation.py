# ✅ Core Idea
#
# There are n! total permutations for n numbers.
#
# Fix one number at a time (most significant position):
#
# 1. There are (n-1)! permutations starting with each number.
# 2. Determine which number should be at the current position by checking how many permutations to skip.
# 3. Reduce k and repeat for the remaining numbers.
#
# This way, we directly compute the k-th permutation without generating all permutations.
#
# Steps:
#
# 1. Create a list of numbers [1, 2, ..., n].
# 2. Compute factorials fact[i] = i! for i = 0..n.
# 3. For each position:
# - Find index = (k-1) // (n-1)! → number to pick.
# - Remove that number from the list.
# - Update k = k - index * (n-1)! -> k = k%(n-1)!
# 4. Repeat until the permutation is complete.


def getPermutation(n, k):
    from math import factorial

    nums = [str(i) for i in range(1, n+1)]
    k -= 1  # 0-based index
    res = []

    for i in range(n, 0, -1):
        fact = factorial(i-1)
        index = k // fact
        res.append(nums.pop(index))
        k %= fact

    return ''.join(res)
