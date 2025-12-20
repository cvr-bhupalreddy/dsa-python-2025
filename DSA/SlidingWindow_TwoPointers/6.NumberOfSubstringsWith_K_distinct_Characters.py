# Number of Substrings or sub arrays solution is same no difference , not even single line

def count_substrings_exact_k_bruteforce(s, K):
    n = len(s)
    count = 0

    for i in range(n):
        distinct = set()

        for j in range(i, n):
            distinct.add(s[j])

            if len(distinct) == K:
                count += 1
            elif len(distinct) > K:
                break  # no need to continue

    return count


def count_substrings_exact_k_bruteforce_optimized(s, K):
    n = len(s)
    total = 0

    for i in range(n):
        distinct = set()

        for j in range(i, n):
            distinct.add(s[j])

            # If distinct > K, no need to continue
            if len(distinct) > K:
                break

            # If exactly K distinct chars
            if len(distinct) == K:
                # All substrings from j to end are valid
                total += (n - j)
                break

    return total


def atMostK(s, K):
    left = 0
    count = 0
    freq = {}

    for right in range(len(s)):
        freq[s[right]] = freq.get(s[right], 0) + 1

        # shrink window if too many distinct chars
        while len(freq) > K:
            freq[s[left]] -= 1
            if freq[s[left]] == 0:
                del freq[s[left]]
            left += 1

        # number of substrings ending at 'right'
        count += (right - left + 1)

    return count


def substrings_with_exactly_k_distinct(s, K):
    return atMostK(s, K) - atMostK(s, K - 1)

    """ Function to find the number of substrings 
    containing all characters 'a', 'b', 'c' in string s. """


def numberOfSubstrings(self, s: str) -> int:
    """Array to store the last seen
        index of characters 'a', 'b', 'c'"""
    last_seen = [-1, -1, -1]

    count = 0

    # Iterate through each character in string s
    for i in range(len(s)):

        """ Update last_seen index
            for current character"""
        last_seen[ord(s[i]) - ord('a')] = i

        """ Check if all characters 'a',
            'b', 'c' have been seen"""
        if last_seen[0] != -1 and last_seen[1] != -1 and last_seen[2] != -1:
            """ Count valid substrings 
                ending at current index"""
            count += 1 + min(last_seen[0], last_seen[1], last_seen[2])

    # Return the total count of substrings
    return count


def numberOfSubstrings1(s: str) -> int:
    last = [-1, -1, -1]   # last positions of 'a', 'b', 'c'
    count = 0

    for i, ch in enumerate(s):
        last[ord(ch) - ord('a')] = i   # update last seen

        # only if all a, b, c have appeared at least once
        if min(last) != -1:
            count += min(last) + 1     # substrings ending at i

    return count
