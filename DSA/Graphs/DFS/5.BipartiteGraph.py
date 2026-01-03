# • Use DFS instead of BFS
# • Maintain a color map:
#     0 → first set
#     1 → second set
# • For every unvisited node:
#     - Assign color 0
#     - DFS its neighbors
# • During DFS:
#     - If neighbor is uncolored → assign opposite color
#     - If neighbor has same color → NOT bipartite
# • Repeat for all components


# Why DFS Works
#     • DFS enforces alternating colors along recursion path
#     • Any odd-length cycle causes a same-color conflict
#     • Conflict immediately proves graph is NOT bipartite


def is_bipartite_dfs(graph):
    color = {}   # node -> 0 or 1

    def dfs(u):
        for v in graph[u]:
            if v not in color:
                color[v] = 1 - color[u]
                if not dfs(v):
                    return False
            elif color[v] == color[u]:
                return False   # same color conflict , Odd length cycle also
        return True

    for node in graph:
        if node not in color:
            color[node] = 0
            if not dfs(node):
                return False

    return True
