# We recursively build partitions starting from index 0.
# At each index:
# Try every possible substring s[i:j+1]
# If substring is a palindrome:
# Add it to the current path
# Recurse from j+1
# Remove it after recursion (backtracking)
# Stop when i reaches end → Add current partition to result.


def palindrome_partition(s):
    result = []
    n = len(s)

    def is_palindrome(l, r):
        while l < r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        return True

    def dfs(i, path):
        if i == n:
            result.append(path[:])
            return

        # try all substrings starting at index i
        for j in range(i, n):
            if is_palindrome(i, j):
                path.append(s[i:j+1])
                dfs(j + 1, path)
                path.pop()   # backtrack

    dfs(0, [])
    return result
