# • Track component size using size[]
# • Attach smaller component under larger component
# • Update size of new root


class DisjointSetBySize:
    def __init__(self, n):
        self.parent = [i for i in range(n+1)]
        self.size = [1] * (n+1)  # this code work for nodes are Zero based index or 1 Based index 

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # path compression
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)

        if rx == ry:
            return False  # already in same set

        if self.size[rx] < self.size[ry]:
            self.parent[rx] = ry
            self.size[ry] += self.size[rx]
        else:
            self.parent[ry] = rx
            self.size[rx] += self.size[ry]

        return True
