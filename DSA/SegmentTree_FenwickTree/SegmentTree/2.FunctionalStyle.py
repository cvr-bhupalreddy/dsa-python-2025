from math import gcd
from copy import deepcopy


# ------------------------------
# Merge Functions
# ------------------------------
def merge_sum(a, b): return a + b


def merge_min(a, b): return min(a, b)


def merge_max(a, b): return max(a, b)


def merge_gcd(a, b): return gcd(a, b)


# ------------------------------
# Build Segment Tree
# ------------------------------
def build(arr, merge=merge_sum):
    """Return segment tree for array arr using merge function"""
    n = len(arr)
    tree = [0] * (4 * n)

    def _build(node, l, r):
        if l == r:
            tree[node] = arr[l]
            return
        mid = (l + r) // 2
        _build(2 * node + 1, l, mid)
        _build(2 * node + 2, mid + 1, r)
        tree[node] = merge(tree[2 * node + 1], tree[2 * node + 2])

    _build(0, 0, n - 1)
    return tree, n


# ------------------------------
# Query Function
# ------------------------------
def query(tree, n, ql, qr, merge=merge_sum, neutral=0):
    """Query range [ql, qr]"""

    def _query(node, l, r):
        # no overlap
        if qr < l or r < ql:
            return neutral
        # total overlap
        if ql <= l and r <= qr:
            return tree[node]
        # partial overlap
        mid = (l + r) // 2
        left = _query(2 * node + 1, l, mid)
        right = _query(2 * node + 2, mid + 1, r)
        return merge(left, right)

    return _query(0, 0, n - 1)


# ------------------------------
# Functional Update (returns new tree)
# ------------------------------
def update(tree, n, idx, val, merge=merge_sum):
    """Return new tree after updating index idx with val"""
    new_tree = deepcopy(tree)  # functional: do not mutate original

    def _update(node, l, r):
        if l == r:
            new_tree[node] = val
            return
        mid = (l + r) // 2
        if idx <= mid:
            _update(2 * node + 1, l, mid)
        else:
            _update(2 * node + 2, mid + 1, r)
        new_tree[node] = merge(new_tree[2 * node + 1], new_tree[2 * node + 2])

    _update(0, 0, n - 1)
    return new_tree


# ------------------------------
# Example Usage
# ------------------------------
arr = [2, 1, 5, 3]

# Sum Segment Tree
tree_sum, n = build(arr, merge_sum)
print("Sum [0,3]:", query(tree_sum, n, 0, 3, merge_sum, neutral=0))
tree_sum2 = update(tree_sum, n, 2, 10, merge_sum)
print("Sum [0,3] after update:", query(tree_sum2, n, 0, 3, merge_sum, neutral=0))

# Min Segment Tree
tree_min, _ = build(arr, merge_min)
print("Min [0,3]:", query(tree_min, n, 0, 3, merge_min, neutral=float('inf')))

# Max Segment Tree
tree_max, _ = build(arr, merge_max)
print("Max [0,3]:", query(tree_max, n, 0, 3, merge_max, neutral=float('-inf')))

# GCD Segment Tree
tree_gcd, _ = build(arr, merge_gcd)
print("GCD [0,3]:", query(tree_gcd, n, 0, 3, merge_gcd, neutral=0))
