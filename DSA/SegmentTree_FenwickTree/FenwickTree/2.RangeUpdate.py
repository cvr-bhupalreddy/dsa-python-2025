# A Fenwick Tree supports point update + prefix query.
# To support range update [l, r]:
#
# Use a difference array:
#     - Add +val at l
#     - Add -val at r+1
#
# Prefix sum restores actual values.

class FenwickRangeUpdate:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def lsb(self, i):
        return i & -i

    def _update(self, i, delta):
        while i <= self.n:
            self.bit[i] += delta
            i += self.lsb(i)

    def range_update(self, l, r, val):
        """
        Add val to all indices in [l, r]
        """
        self._update(l, val)
        self._update(r + 1, -val)

    def point_query(self, i):
        """
        Get value at index i
        """
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= self.lsb(i)
        return s
