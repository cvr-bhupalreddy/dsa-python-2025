def length_of_longest_substring_brute(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        for j in range(i, n):
            substr = s[i:j + 1]
            if len(set(substr)) == len(substr):  # check uniqueness
                max_len = max(max_len, j - i + 1)

    return max_len


def length_of_longest_substring_brute_hash(s):
    n = len(s)
    max_len = 0

    for i in range(n):
        visited = {}  # hashmap to store characters in current substring
        for j in range(i, n):
            if s[j] in visited:
                break  # duplicate found, stop extending this substring
            visited[s[j]] = True
            max_len = max(max_len, j - i + 1)

    return max_len


def length_of_longest_substring_better(s):
    n = len(s)
    visited = set()
    max_len = 0
    left = 0

    for right in range(n):
        while s[right] in visited:
            visited.remove(s[left])
            left += 1
        visited.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len


# Sliding Window / Optimal Approach
# 1. Use two pointers: left and right to maintain a sliding window [left, right].
# 2. Use a hashmap (or array) to store the last index of each character seen.
# 3. Iterate with right pointer over the string:
#     a. If s[right] is in hashmap and its last index >= left:
#     - Move left to last_index + 1 (shrink window to remove duplicate)
#     b. Update hashmap with s[right] = right
#     c. Update max_len = max(max_len, right - left + 1)
# 4. Return max_len

def length_of_longest_substring_optimal(s):
    n = len(s)
    visited_index = {}
    left = 0
    max_len = 0

    for right in range(n):
        if s[right] in visited_index and visited_index[s[right]] >= left:
            left = visited_index[s[right]] + 1
        visited_index[s[right]] = right
        max_len = max(max_len, right - left + 1)

    return max_len


#
# | Approach                 | Time Complexity | Space Complexity | Notes                                             |
# | ------------------------ | --------------- | ---------------- | ------------------------------------------------- |
# | Brute-force with set     | O(n³)           | O(n)             | Creates set for every substring                   |
# | Brute-force with hashmap | O(n²)           | O(n)             | Stops on duplicate, uses hashmap                  |
# | Sliding window / optimal | O(n)            | O(min(n,a))      | Best approach, uses hashmap to track last indices |
# | Better (Sliding Window + Set)| O(2n) ≈ O(n)| O(min(n,a))      | Maintain a sliding window with left and right,
# store seen characters in a set, shrink window on duplicate.

