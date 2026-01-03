# Recursive segment trees allocate 4n to safely handle uneven trees built top-down,
# while iterative segment trees use 2n because they store a perfect bottom-up binary tree
# with exactly n leaves and n−1 internal nodes.

# 🔥 Key Difference Visualization
# | Feature     | Recursive Segment Tree | Iterative Segment Tree |
# | ----------- | ---------------------- | ---------------------- |
# | Build style | Top-down               | Bottom-up              |
# | Tree shape  | Possibly uneven        | Perfect binary tree    |
# | Storage     | 4n (safe upper bound)  | 2n (exact)             |
# | Indexing    | `2*i+1`, `2*i+2`       | `i//2`, `2*i`, `2*i+1` |
# | Speed       | Slightly slower        | Faster                 |
# | Stack usage | Uses recursion         | No recursion           |

# Important Observations (Interview Gold)
#     Leaves start at index n
#     Root is always at index 1 [ Index 0 is unused ]
#     Parent index = i // 2
#     Left child = 2*i, Right child = 2*i + 1
#     Total size = 2n
#     Works even when n is not a power of 2
# N-1 Internal Nodes
# N Leaf Nodes

# ------------------------------
# Iterative Segment Tree
# Supports: point update + range query
# ------------------------------

class IterativeSegmentTree:
    def __init__(self, arr, merge=lambda a, b: a + b, neutral=0):
        """Initialize segment tree"""
        self.n = len(arr)
        self.tree = [neutral] * (2 * self.n)  # 0-indexed
        self.merge = merge
        self.neutral = neutral

        # Build leaves
        for i in range(self.n):
            self.tree[self.n + i] = arr[i]

        # Build internal nodes
        for i in range(self.n - 1, 0, -1):
            self.tree[i] = self.merge(self.tree[2 * i], self.tree[2 * i + 1])

    def update(self, idx, value):
        """Point update: arr[idx] = value"""
        idx += self.n  # move to leaf
        self.tree[idx] = value

        # Update parents
        while idx > 1:
            idx //= 2  # parent is stored at index/2
            self.tree[idx] = self.merge(self.tree[2 * idx], self.tree[2 * idx + 1])

    def query(self, left, right):
        """Range query [left, right] inclusive"""
        left += self.n
        right += self.n
        res = self.neutral

        while left <= right:
            if left % 2 == 1:  # left is right child
                res = self.merge(res, self.tree[left])
                left += 1
            if right % 2 == 0:  # right is left child
                res = self.merge(res, self.tree[right])
                right -= 1
            left //= 2
            right //= 2
        return res

# Why This Works (Intuition)
# Odd left → right child → segment fully inside → take it
# Even right → left child → segment fully inside → take it
# After taking, shrink range and move to parent
# Each step removes unnecessary segments
# Total steps = O(log n)

# Reasoning:
#
# At any level:
#     left marks the first index not yet consumed
#     If left is a right child, then:
#     Its left sibling lies before the query
#     So parent segment cannot be fully used
#     But the right child alone is perfectly aligned

# 1️⃣ Iterative Segment Tree – Core Idea
#
# Tree stored in a flat array of size 2n
# Leaves at indices [n … 2n-1]
# Parents at indices [1 … n-1]
# Built bottom-up


# BUILD(arr, n):
# tree[0 .. 2n-1]
#
# // Step 1: place array elements at leaves
# for i = 0 to n-1:
#     tree[n + i] = arr[i]
#
# // Step 2: build internal nodes bottom-up
# for i = n-1 down to 1:
#     tree[i] = MERGE(tree[2*i], tree[2*i + 1])

# 📌 MERGE can be sum, min, max, gcd, etc.


# 3️⃣ RANGE QUERY / SEARCH [L, R] (Iterative)
# QUERY(L, R, n):
# L = L + n
# R = R + n
# result = NEUTRAL_VALUE
#
# while L <= R:
#     if L is a right child (L % 2 == 1):
#         result = MERGE(result, tree[L])
#         L = L + 1
#
#     if R is a left child (R % 2 == 0):
#         result = MERGE(result, tree[R])
#         R = R - 1
#
#     L = L // 2
#     R = R // 2
#
# return result


# 4️⃣ POINT UPDATE (Iterative)
# UPDATE(index, value, n):
# pos = index + n
# tree[pos] = value
#
# while pos > 1:
#     pos = pos // 2
#     tree[pos] = MERGE(tree[2*pos], tree[2*pos + 1])
