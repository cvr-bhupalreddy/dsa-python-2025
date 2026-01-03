# 6️⃣ Lazy Propagation — Core Idea
# Problem
#     Range update + range query is slow without optimization.
#
# Solution
#     Delay updates until needed


# Lazy Propagation Rules
#     Store pending updates in lazy[node]
#     Apply only when:
#         Query touches the node
#         Going deeper in recursion
#     Push updates to children only when required


# 🔹 Rules of Lazy Propagation
#
# Update a range [l, r]
#     If the current segment is completely inside [l, r], update current node and mark children lazy.
#     If partial overlap → push lazy values to children and recurse.
#
# Query a range [l, r]
#     If lazy value pending at a node → push it before using the value.
#     Partial overlap → recurse to children.
#
# How to know lazy update is pending?
#     lazy[node] != 0 (for sum updates)
#     Node value is outdated → must push.

class LazySegmentTree:
    def __init__(self, arr):
        """
        Initialize segment tree with lazy propagation
        """
        self.n = len(arr)
        self.tree = [0] * (4 * self.n)   # segment tree array
        self.lazy = [0] * (4 * self.n)   # lazy updates array
        self.build(arr, 0, self.n - 1, 1)

    def build(self, arr, l, r, node):
        """
        Recursively build the segment tree
        """
        if l == r:
            self.tree[node] = arr[l]  # leaf node
            return
        mid = (l + r) // 2
        self.build(arr, l, mid, node * 2)        # build left child
        self.build(arr, mid + 1, r, node * 2 + 1)  # build right child
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]  # sum aggregation

    def push(self, node, l, r):
        """
        Push lazy updates from current node to children
        """
        if self.lazy[node] != 0:  # lazy update pending
            # Apply the lazy value to current node
            self.tree[node] += (r - l + 1) * self.lazy[node]

            if l != r:  # if not a leaf, propagate lazy to children
                self.lazy[node*2] += self.lazy[node]
                self.lazy[node*2+1] += self.lazy[node]

            # Clear lazy at current node
            self.lazy[node] = 0

    def update(self, ql, qr, val, l=0, r=None, node=1):
        """
        Update the range [ql, qr] by adding 'val'
        """
        if r is None:
            r = self.n - 1

        # Push any pending updates at this node before processing
        self.push(node, l, r)

        # No overlap
        if qr < l or ql > r:
            return

        # Total overlap → mark lazy and push
        if ql <= l and r <= qr:
            self.lazy[node] += val
            self.push(node, l, r)
            return

        # Partial overlap → recurse to children
        mid = (l + r) // 2
        self.update(ql, qr, val, l, mid, node*2)
        self.update(ql, qr, val, mid+1, r, node*2+1)

        # Update current node based on children
        self.tree[node] = self.tree[node*2] + self.tree[node*2+1]

    def query(self, ql, qr, l=0, r=None, node=1):
        """
        Query the sum of range [ql, qr]
        """
        if r is None:
            r = self.n - 1

        # Push lazy updates if any pending at this node
        self.push(node, l, r)

        # No overlap
        if qr < l or ql > r:
            return 0  # sum identity

        # Total overlap → use current node
        if ql <= l and r <= qr:
            return self.tree[node]

        # Partial overlap → query both children
        mid = (l + r) // 2
        left_sum = self.query(ql, qr, l, mid, node*2)
        right_sum = self.query(ql, qr, mid+1, r, node*2+1)
        return left_sum + right_sum
