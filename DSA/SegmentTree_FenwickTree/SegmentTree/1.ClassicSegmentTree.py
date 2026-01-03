from math import gcd


# ------------------------------
# MERGE FUNCTIONS
# ------------------------------
def merge_sum(a, b): return a + b


def merge_min(a, b): return min(a, b)


def merge_max(a, b): return max(a, b)


def merge_gcd(a, b): return gcd(a, b)


# ------------------------------
# BUILD SEGMENT TREE
# ------------------------------
def build(node, l, r, arr, tree, merge=merge_sum):
    """Recursively build segment tree"""
    if l == r:
        tree[node] = arr[l]
        return
    mid = (l + r) // 2
    build(2 * node + 1, l, mid, arr, tree, merge)
    build(2 * node + 2, mid + 1, r, arr, tree, merge)
    tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])


# ------------------------------
# QUERY SEGMENT TREE
# ------------------------------
def query(node, l, r, ql, qr, tree, merge=merge_sum, neutral=0):
    """Query in range [ql, qr]"""
    # no overlap
    if qr < l or r < ql:
        return neutral
    # total overlap
    if ql <= l and r <= qr:
        return tree[node]
    # partial overlap
    mid = (l + r) // 2
    left = query(2 * node + 1, l, mid, ql, qr, tree, merge, neutral)
    right = query(2 * node + 2, mid + 1, r, ql, qr, tree, merge, neutral)
    return merge(left, right)


# ------------------------------
# UPDATE SEGMENT TREE
# ------------------------------
def update(node, l, r, idx, val, tree, merge=merge_sum):
    if l == r:  # leaf node
        tree[node] = val
        return
    mid = (l + r) // 2
    if idx <= mid:
        update(2 * node + 1, l, mid, idx, val, tree, merge)
    else:
        update(2 * node + 2, mid + 1, r, idx, val, tree, merge)
    tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])


# ------------------------------
# USAGE EXAMPLE
# ------------------------------
arr = [2, 1, 5, 3]
n = len(arr)
tree = [0] * (4 * n)

# 1️⃣ Sum Segment Tree
build(0, 0, n - 1, arr, tree, merge_sum)
print("Sum [0,3]:", query(0, 0, n - 1, 0, 3, tree, merge_sum, neutral=0))
update(0, 0, n - 1, 2, 10, tree, merge_sum)
print("Sum [0,3] after update:", query(0, 0, n - 1, 0, 3, tree, merge_sum, neutral=0))

# 2️⃣ Min Segment Tree
build(0, 0, n - 1, arr, tree, merge_min)
print("Min [0,3]:", query(0, 0, n - 1, 0, 3, tree, merge_min, neutral=float('inf')))

# 3️⃣ Max Segment Tree
build(0, 0, n - 1, arr, tree, merge_max)
print("Max [0,3]:", query(0, 0, n - 1, 0, 3, tree, merge_max, neutral=float('-inf')))

# 4️⃣ GCD Segment Tree
build(0, 0, n - 1, arr, tree, merge_gcd)
print("GCD [0,3]:", query(0, 0, n - 1, 0, 3, tree, merge_gcd, neutral=0))


# ⏱️ Time Complexity
# | Operation    | Complexity |
# | ------------ | ---------- |
# | Build Tree   | O(n)       |
# | Point Update | O(log n)   |
# | Range Query  | O(log n)   |
# | Space        | O(4 * n)   |
