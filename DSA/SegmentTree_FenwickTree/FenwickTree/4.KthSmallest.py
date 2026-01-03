# Fenwick Tree can store frequencies.
# To find kth smallest:
#     - Binary search using Fenwick prefix sums
#     - Use binary lifting on Fenwick Tree
# 🔷 What is Binary Lifting?
# Binary Lifting is a technique where we jump in powers of two (2⁰, 2¹, 2², …) instead of moving one step at a time.
# We jump:
# +16 → +8 → +4 → +2 → +1
# This reduces search time from O(N) to O(log N).

# 🔷 Why Binary Lifting in Fenwick Tree?
# Fenwick Tree stores:
#     prefix sums over ranges of size = LSB(index)
#
# So:
# Every index represents a power-of-two range
# We can jump over ranges using binary lifting
# This allows us to find an index by cumulative sum


class FenwickKth:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def lsb(self, i):
        return i & -i

    def update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += self.lsb(i)

    def kth_smallest(self, k):
        """
        Returns smallest index with prefix sum >= k
        """
        idx = 0
        bit_mask = 1 << (self.n.bit_length())

        while bit_mask > 0:
            next_idx = idx + bit_mask
            if next_idx <= self.n and self.bit[next_idx] < k:
                k -= self.bit[next_idx]
                idx = next_idx
            bit_mask >>= 1

        return idx + 1
