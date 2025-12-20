# Brute Force
def find_celebrity_bruteforce(n, knows):
    """
    n: number of people (0..n-1)
    knows: function knows(a, b) -> bool
    returns celebrity index or -1
    """
    for i in range(n):
        is_celeb = True
        for j in range(n):
            if i == j:
                continue
            if knows(i, j) or not knows(j, i):
                is_celeb = False
                break
        if is_celeb:
            return i
    return -1


# Stack Elimination

# 2) Better — Stack elimination
#
# Core idea: Put all people on a stack. Pop two (a, b), use knows(a,b):
#
# If a knows b → a cannot be celebrity → discard a, keep b.
# Else → b cannot be celebrity → discard b, keep a
#
# After reducing to one candidate, verify it by scanning everyone.


# Better: Stack-based elimination
def find_celebrity_stack(n, knows):
    stack = list(range(n))
    # Reduce to one candidate
    while len(stack) > 1:
        a = stack.pop()
        b = stack.pop()
        if knows(a, b):
            # a cannot be celeb
            stack.append(b)
        else:
            # b cannot be celeb
            stack.append(a)

    if not stack:
        return -1

    cand = stack.pop()
    # Verify candidate
    for i in range(n):
        if i == cand:
            continue
        if knows(cand, i) or not knows(i, cand):
            return -1
    return cand



# 3) Optimal — Two-pointer elimination (O(1) space)
#
# Core idea: Use two indices i = 0, j = n-1. Compare i and j:
# If knows(i, j) is True → i cannot be celebrity → i += 1.
# Else → j cannot be celebrity → j -= 1.
# Continue until i == j. That index is the candidate; verify by scanning everyone.

# Optimal: Two-pointer elimination
def find_celebrity_two_pointer(n, knows):
    i, j = 0, n - 1
    while i < j:
        if knows(i, j):
            # i knows j => i cannot be celeb
            i += 1
        else:
            # i does not know j => j cannot be celeb
            j -= 1

    cand = i
    # Verify candidate
    for k in range(n):
        if k == cand:
            continue
        if knows(cand, k) or not knows(k, cand):
            return -1
    return cand
