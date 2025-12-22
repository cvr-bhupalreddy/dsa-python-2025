# What is the Transitive Closure Problem?
# Problem Definition
#
# Given a directed graph G(V, E):
# Transitive Closure tells us: For every pair of vertices (u, v), is there a path from u to v?


# reach[u][v] = True   if v is reachable from u
# reach[u][v] = False  otherwise


def transitive_closure(n, edges):
    # Initialize reachability matrix
    reach = [[False] * n for _ in range(n)]

    # Every node reaches itself
    for i in range(n):
        reach[i][i] = True

    # Direct edges
    for u, v in edges:
        reach[u][v] = True

    # Floyd–Warshall
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if reach[i][k] and reach[k][j]:
                    reach[i][j] = True

    return reach
