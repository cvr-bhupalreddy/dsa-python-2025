# We use recursion + backtracking.
# At each digit:
# - Look up which letters it maps to.
# - Try each letter by appending it to current path.
# - Recurse to next digit.
# - Backtrack (remove the last letter) to explore next option.
#
# Base Case:
# If current index == length of digits, we have a complete combination.
# Add it to answer list.


def letterCombinations(digits):
    if not digits:
        return []

    mapping = {
        '2': "abc", '3': "def", '4': "ghi", '5': "jkl",
        '6': "mno", '7': "pqrs", '8': "tuv", '9': "wxyz"
    }

    result = []
    path = []

    def backtrack(idx):
        # Base case
        if idx == len(digits):
            result.append("".join(path))
            return

        # current digit
        digit = digits[idx]

        # try all letters for this digit
        for ch in mapping[digit]:
            path.append(ch)       # choose
            backtrack(idx + 1)    # explore
            path.pop()            # un-choose (backtrack)

    backtrack(0)
    return result


def letterCombinations_thread_safe(digits):
    if not digits:
        return []

    mapping = {
        '2': "abc", '3': "def", '4': "ghi",
        '5': "jkl", '6': "mno", '7': "pqrs",
        '8': "tuv", '9': "wxyz"
    }

    res = []

    def backtrack(index, path):
        # If full length reached → add to result
        if index == len(digits):
            res.append("".join(path))
            return

        # For every letter corresponding to current digit
        for ch in mapping[digits[index]]:
            # pass a *new list* to next recursion (thread-safe)
            backtrack(index + 1, path + [ch])

    backtrack(0, [])
    return res
