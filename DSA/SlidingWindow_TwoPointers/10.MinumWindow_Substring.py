# Brute Force Solution
#     Check all substrings of s.
#     For each substring, check if it contains all characters of t.
#     Time Complexity: O(n^2 * |t|)
#     Space Complexity: O(|t|)

def min_window_brute(s, t):
    from collections import Counter
    n = len(s)
    target_count = Counter(t)
    min_len = float('inf')
    result = ""

    for i in range(n):
        for j in range(i, n):
            window = s[i:j + 1]
            window_count = Counter(window)
            if all(window_count[c] >= target_count[c] for c in target_count):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    result = window
    return result


def min_window_brute_dict(s, t):
    n = len(s)

    # Build target frequency map
    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) + 1

    min_len = float('inf')
    result = ""

    # Check all substrings
    for i in range(n):
        window_count = {}
        for j in range(i, n):
            char = s[j]
            if char in target_count:
                window_count[char] = window_count.get(char, 0) + 1

            # Check if current window satisfies target
            if all(window_count.get(c, 0) >= target_count[c] for c in target_count):
                if j - i + 1 < min_len:
                    min_len = j - i + 1
                    result = s[i:j + 1]
                break  # No need to expand further, we found a valid window
    return result


# Better Approach (Sliding Window, Two Pointers)
#
#     Expand right pointer to include characters.
#     Use a hashmap to count characters.
#     Once window contains all target characters, shrink left pointer.
#     Time Complexity: O(n) in average case (each char visited twice)
#     Space Complexity: O(|t|)


def min_window_dict(s, t):
    # Build target frequency map
    target_count = {}
    for char in t:
        if char in target_count:
            target_count[char] += 1
        else:
            target_count[char] = 1

    window_count = {}
    required = len(target_count)
    formed = 0
    left = 0
    min_len = float('inf')
    ans = (0, 0)

    for right, char in enumerate(s):
        # Update window count
        window_count[char] = window_count.get(char, 0) + 1

        # Check if current char satisfies requirement
        if char in target_count and window_count[char] == target_count[char]:
            formed += 1

        # Try shrinking the window
        while left <= right and formed == required:
            if right - left + 1 < min_len:
                min_len = right - left + 1
                ans = (left, right)

            # Remove char at left
            window_count[s[left]] -= 1
            if s[left] in target_count and window_count[s[left]] < target_count[s[left]]:
                formed -= 1
            left += 1

    return "" if min_len == float('inf') else s[ans[0]:ans[1] + 1]


def min_window_optimal_dict(s, t):
    # Build target frequency map
    target_count = {}
    for char in t:
        target_count[char] = target_count.get(char, 0) + 1

    required = len(target_count)
    # Filter s to only include characters in t
    filtered_s = [(i, c) for i, c in enumerate(s) if c in target_count]

    left = 0
    formed = 0
    window_count = {}
    ans = (float('inf'), None, None)

    for right, (idx, char) in enumerate(filtered_s):
        # Add current char to window
        window_count[char] = window_count.get(char, 0) + 1
        if window_count[char] == target_count[char]:
            formed += 1

        # Shrink the window as much as possible
        while left <= right and formed == required:
            start = filtered_s[left][0]
            end = idx
            if end - start + 1 < ans[0]:
                ans = (end - start + 1, start, end)

            # Remove char at left
            left_char = filtered_s[left][1]
            window_count[left_char] -= 1
            if window_count[left_char] < target_count[left_char]:
                formed -= 1
            left += 1

    return "" if ans[0] == float('inf') else s[ans[1]:ans[2] + 1]



def minWindow(self, s: str, t: str) -> str:

    """ Variable to store the minimum
    length of substring found """
    minLen = float('inf')

    """ Variable to store the starting index
    of the minimum length substring """
    sIndex = -1

    """ Array to count frequencies
    of characters in string t"""
    hash = [0] * 256

    # Count the frequencies of characters in t
    for c in t:
        hash[ord(c)] += 1

    count = 0
    l, r = 0, 0

    # Iterate through current window
    while r < len(s):
        # Include the current character in the window
        if hash[ord(s[r])] > 0:
            count += 1
        hash[ord(s[r])] -= 1

        """ If all characters from t 
        are found in current window """
        while count == len(t):

            """ Update minLen and sIndex
            if current window is smaller """
            if r - l + 1 < minLen:
                minLen = r - l + 1
                sIndex = l

            # Remove leftmost character from window
            hash[ord(s[l])] += 1
            if hash[ord(s[l])] > 0:
                count -= 1
            l += 1
        r += 1

    # Return minimum length substring from s
    return s[sIndex:sIndex + minLen] if sIndex != -1 else ""


def min_window_single_map(s, t):
    if not s or not t:
        return ""

    # Frequency dictionary for characters in t
    freq = {}
    for c in t:
        freq[c] = freq.get(c, 0) + 1

    left = 0
    count = 0  # Number of characters from t included in window
    min_len = float('inf')
    start_index = 0

    for right, char in enumerate(s):
        # Decrement in map while adding to window
        if char in freq:
            freq[char] -= 1
            if freq[char] >= 0:
                count += 1

        # Shrink from left if all characters are included
        while count == len(t):
            if right - left + 1 < min_len:
                min_len = right - left + 1
                start_index = left

            left_char = s[left]
            if left_char in freq:
                freq[left_char] += 1
                if freq[left_char] > 0:
                    count -= 1
            left += 1

    return s[start_index:start_index + min_len] if min_len != float('inf') else ""

# Example
s = "ADOBECODEBANC"
t = "ABC"
print(min_window_single_map(s, t))  # Output: "BANC"
