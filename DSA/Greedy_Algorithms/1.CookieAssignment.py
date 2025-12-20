# 🍪 Cookie Assignment Problem (Greedy Algorithm)
# ✅ Problem Statement
#
# You are given:
#     An array g representing the greed factor of each child
#     An array s representing the size of each cookie
#     A child with greed g[i] will be satisfied only if they get a cookie of size ≥ g[i].

# Each child gets at most one cookie
# Each cookie can be assigned to only one child
# Child is satisfied only if:
#     cookie_size >= greed_factor
# Goal:
#     Assign cookies to maximize the number of satisfied children.
#     (Most children you can satisfy, not maximum sum.)


def findContentChildren(g, s):
    g.sort()
    s.sort()

    i = j = 0
    count = 0

    while i < len(g) and j < len(s):
        if s[j] >= g[i]:  # Cookie satisfies the child
            count += 1
            i += 1
            j += 1
        else:
            j += 1  # Use a bigger cookie

    return count

# 🍪 VERSION 2 — Children Can Receive MULTIPLE Cookies
#

#
# Strategy
#
# Sort children by greed
# Sort cookies by size
# For each child:
#     Keep giving smallest remaining cookies
#     Accumulate sum
#     Stop when sum ≥ greed
#
# Move to next child


def findContentChildrenMulti(g, s):
    g.sort()
    s.sort()

    i = 0  # child index
    j = 0  # cookie index
    count = 0

    while i < len(g) and j < len(s):
        required = g[i]
        total = 0

        # Give multiple cookies to the child
        while j < len(s) and total < required:
            total += s[j]
            j += 1

        if total >= required:
            count += 1
            i += 1
        else:
            break  # No more cookies left

    return count
