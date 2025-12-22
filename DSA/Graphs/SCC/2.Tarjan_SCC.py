# disc[u] = discovery time
# low[u]  = lowest reachable discovery time
#
# If disc[u] == low[u] → u is SCC root
# Pop stack until u


from collections import defaultdict


def tarjan_scc(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)

    disc = [-1] * n
    low = [0] * n
    on_stack = [False] * n
    stack = []
    time = 0
    sccs = []

    def dfs(u):
        nonlocal time
        disc[u] = low[u] = time
        time += 1
        stack.append(u)
        on_stack[u] = True

        for v in graph[u]:
            if disc[v] == -1:
                dfs(v)
                low[u] = min(low[u], low[v])
            elif on_stack[v]:
                low[u] = min(low[u], disc[v])

        # SCC root
        if disc[u] == low[u]:
            component = []
            while True:
                node = stack.pop()
                on_stack[node] = False
                component.append(node)
                if node == u:
                    break
            sccs.append(component)

    for i in range(n):
        if disc[i] == -1:
            dfs(i)

    return sccs
