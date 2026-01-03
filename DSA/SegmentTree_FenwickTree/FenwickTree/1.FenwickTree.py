# Each node stores Range of [ LSB(i)+1 -> i]
#
# LSB(i) = i & (-i)


# Fenwick Tree does NOT store individual values.
# It stores partial prefix sums.
# Update jumps upward using LSB.
# Query jumps downward using LSB.


class FenwickTree:
    def __init__(self, n):
        self.n = n
        self.bit = [0] * (n + 1)

    def lsb(self, i):
        """
        Returns the Lowest Set Bit (LSB) of i.
        Determines the size of range this index controls.
        """
        return i & (-i)

    def update(self, i, delta):
        """
        Adds delta to index i (1-based indexing).
        Propagates update to all Fenwick nodes covering index i.
        """
        while i <= self.n:
            self.bit[i] += delta
            i += self.lsb(i)   # move to next responsible index

    def query(self, i):
        """
        Returns prefix sum from index 1 to i.
        """
        s = 0
        while i > 0:
            s += self.bit[i]
            i -= self.lsb(i)   # move to parent prefix
        return s

    def range_query(self, l, r):
        """
        Returns sum from l to r (inclusive).
        """
        return self.query(r) - self.query(l - 1)


# 🔹 Time Complexity Table
# | Operation                            | Description            | Time Complexity |
# | ------------------------------------ | ---------------------- | --------------- |
# | **Point Update**                     | `arr[i] += delta`      | **O(log N)**    |
# | **Prefix Query**                     | `sum(1..i)`            | **O(log N)**    |
# | **Range Query**                      | `sum(l..r)`            | **O(log N)**    |
# | **Range Update (Diff Array)**        | update `[l, r]`        | **O(log N)**    |
# | **Point Query (after range update)** | value at index         | **O(log N)**    |
# | **Prefix Min / Max**                 | monotonic updates only | **O(log N)**    |
# | **Kth Smallest**                     | binary lifting         | **O(log N)**    |
# | **Kth Largest**                      | same as kth smallest   | **O(log N)**    |
# | **Build Tree**                       | insert N elements      | **O(N log N)**  |
#
# 🔹 Space Complexity Table
# | Feature                    | Space          |
# | -------------------------- | -------------- |
# | Fenwick array              | **O(N)**       |
# | Coordinate compression map | **O(N)**       |
# | Binary lifting             | **O(1)** extra |
# | Total                      | **O(N)**       |
