from collections import defaultdict


def kosaraju_scc(n, edges):
    graph = defaultdict(list)
    rev_graph = defaultdict(list)

    for u, v in edges:
        graph[u].append(v)
        rev_graph[v].append(u)

    visited = [False] * n
    stack = []

    # 1st DFS: order by finish time
    def dfs1(u):
        visited[u] = True
        for v in graph[u]:
            if not visited[v]:
                dfs1(v)
        stack.append(u)

    for i in range(n):
        if not visited[i]:
            dfs1(i)

    # 2nd DFS: on reversed graph
    visited = [False] * n
    sccs = []

    def dfs2(u, component):
        visited[u] = True
        component.append(u)
        for v in rev_graph[u]:
            if not visited[v]:
                dfs2(v, component)

    while stack:
        node = stack.pop()
        if not visited[node]:
            component = []
            dfs2(node, component)
            sccs.append(component)

    return sccs
