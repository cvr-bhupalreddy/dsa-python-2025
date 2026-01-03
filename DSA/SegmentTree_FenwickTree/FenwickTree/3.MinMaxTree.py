# Fenwick Tree can support min/max queries if:
# - Updates only reduce (for min) or increase (for max)
# - Queries are prefix-based

class FenwickMin:
    def __init__(self, n):
        self.n = n
        self.bit = [float('inf')] * (n + 1)

    def lsb(self, i):
        return i & -i

    def update(self, i, val):
        """
        Update index i with minimum value
        """
        while i <= self.n:
            self.bit[i] = min(self.bit[i], val)
            i += self.lsb(i)

    def query(self, i):
        """
        Get minimum from 1 to i
        """
        res = float('inf')
        while i > 0:
            res = min(res, self.bit[i])
            i -= self.lsb(i)
        return res
