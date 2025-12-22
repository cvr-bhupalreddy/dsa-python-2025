# Let dist[i][j] = shortest path from i to j
#
# For every intermediate node k:
# dist[i][j] = min(
#     dist[i][j],
#     dist[i][k] + dist[k][j]
# )


def floyd_warshall(n, edges):
    INF = float('inf')

    # Initialize distance matrix
    dist = [[INF] * n for _ in range(n)]

    # Distance from node to itself = 0
    for i in range(n):
        dist[i][i] = 0

    # Fill direct edges
    for u, v, w in edges:
        dist[u][v] = min(dist[u][v], w)

    # Main DP
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if dist[i][k] != INF and dist[k][j] != INF:
                    dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j])

    # Detect negative cycle
    for i in range(n):
        if dist[i][i] < 0:
            return None  # Negative cycle exists

    return dist
