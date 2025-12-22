# • Maintain connected components
#     • union(x, y) → merge sets
#     • find(x) → representative of x's set
#     • Path compression: flatten tree for fast find


class UnionFind:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n  # Optional: for union by rank

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])  # Path compression
        return self.parent[x]

    def union(self, x, y):
        xroot = self.find(x)
        yroot = self.find(y)

        if xroot == yroot:
            return False  # Already connected

        # Union by rank
        if self.rank[xroot] < self.rank[yroot]:
            self.parent[xroot] = yroot
        elif self.rank[xroot] > self.rank[yroot]:
            self.parent[yroot] = xroot
        else:
            self.parent[yroot] = xroot
            self.rank[xroot] += 1
        return True


# ==================== KRUSKAL'S ALGORITHM ====================
# Core Idea
#     • Sort all edges by weight
#     • Pick edges one by one
#     • Include edge if it does NOT form a cycle (use Union-Find)
#     • Repeat until V-1 edges


def kruskal_mst(n, edges):
    """
    n: number of nodes (0 to n-1)
    edges: list of (u, v, w)
    """
    edges.sort(key=lambda x: x[2])  # Sort by weight
    uf = UnionFind(n)
    mst_weight = 0
    mst_edges = []

    for u, v, w in edges:
        if uf.union(u, v):
            mst_weight += w
            mst_edges.append((u, v, w))

    return mst_weight, mst_edges


def make_union_find(n):
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # Path compression
        return parent[x]

    def union(x, y):
        xroot = find(x)
        yroot = find(y)

        if xroot == yroot:
            return False  # Already connected

        # Union by rank
        if rank[xroot] < rank[yroot]:
            parent[xroot] = yroot
        elif rank[xroot] > rank[yroot]:
            parent[yroot] = xroot
        else:
            parent[yroot] = xroot
            rank[xroot] += 1

        return True

    # Expose the functions
    return find, union


# Initialize arrays globally
def make_set(n):
    global parent, rank
    parent = [i for i in range(n)]
    rank = [0] * n


# Find with path compression
def find(x):
    if parent[x] != x:
        parent[x] = find(parent[x])  # Path compression
    return parent[x]


# Union by rank
def union(x, y):
    xroot = find(x)
    yroot = find(y)

    if xroot == yroot:
        return False  # Already connected

    if rank[xroot] < rank[yroot]:
        parent[xroot] = yroot
    elif rank[xroot] > rank[yroot]:
        parent[yroot] = xroot
    else:
        parent[yroot] = xroot
        rank[xroot] += 1

    return True
