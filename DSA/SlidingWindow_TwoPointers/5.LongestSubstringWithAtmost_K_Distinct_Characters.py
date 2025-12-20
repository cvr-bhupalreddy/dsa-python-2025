def longest_substring_k_distinct_bruteforce(s, k):
    n = len(s)
    best = 0

    for i in range(n):
        seen = set()

        for j in range(i, n):
            seen.add(s[j])

            # If distinct characters exceed k → stop this substring
            if len(seen) > k:
                break

            best = max(best, j - i + 1)

    return best


def longest_substring_k_distinct_better(s, k):
    left = 0
    freq = {}
    best = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        while len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                freq.pop(s[left])
            left += 1

        best = max(best, right - left + 1)

    return best


def longest_substring_k_distinct_optimal(s, k):
    left = 0
    freq = {}
    best = 0

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        # Fix violation (more than K distinct)
        if len(freq) > k:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                freq.pop(s[left])
            left += 1

        # Valid window → update
        if len(freq) <= k:
            best = max(best, right - left + 1)

    return best
