# A connected graph with n nodes needs at least n - 1 edges
# Extra edges inside components are redundant
# Each redundant edge can be:
#     Removed
#     Reused to connect two disconnected components


# 1. Use DSU to detect connected components
# 2. Count redundant edges (edges forming cycles)
# 3. Count number of connected components = C
# 4. Minimum edges needed to connect components = C - 1
# 5. If redundant_edges >= C - 1 → return C - 1
# 6. Else → return -1


def min_operations_to_connect(n, edges):
    parent = [i for i in range(n)]
    rank = [0] * n

    def find(x):
        if parent[x] != x:
            parent[x] = find(parent[x])  # path compression
        return parent[x]

    def union(x, y):
        px, py = find(x), find(y)
        if px == py:
            return False  # redundant edge
        if rank[px] < rank[py]:
            parent[px] = py
        elif rank[px] > rank[py]:
            parent[py] = px
        else:
            parent[py] = px
            rank[px] += 1
        return True

    redundant = 0

    for u, v in edges:
        if not union(u, v):
            redundant += 1

    # count connected components
    components = len(set(find(i) for i in range(n)))

    # need (components - 1) edges to connect all components
    if redundant >= components - 1:
        return components - 1
    else:
        return -1
