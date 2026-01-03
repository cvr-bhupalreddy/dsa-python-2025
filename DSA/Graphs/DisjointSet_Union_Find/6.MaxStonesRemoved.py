# Core Idea
#
# Treat each stone as a node.
# Connect stones if they share same row or column → forms connected components.
# Stones in a connected component can be removed all but one.
# max_stones_removed = total_stones - number_of_connected_components


class DSU:
    def __init__(self, n):
        self.parent = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx, ry = self.find(x), self.find(y)
        if rx == ry:
            return False
        if self.size[rx] < self.size[ry]:
            self.parent[rx] = ry
            self.size[ry] += self.size[rx]
        else:
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]
        return True


def removeStones(stones):
    n = len(stones)
    dsu = DSU(n)

    # Union stones in same row or same column
    for i in range(n):
        for j in range(i+1, n):
            if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                dsu.union(i, j)

    # Count connected components
    components = set()
    for i in range(n):
        components.add(dsu.find(i))

    return n - len(components)


# Example
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(removeStones(stones))  # Output: 5
