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



def max_min_path(n, edges):
    """
    Compute max-min (bottleneck) path between all pairs using Floyd-Warshall.
    """
    INF = 0  # For bottleneck, no edge = 0 (assuming positive weights)
    # Step 1: Initialize matrix
    bottleneck = [[INF]*n for _ in range(n)]
    for i in range(n):
        bottleneck[i][i] = float('inf')  # Self-loop: infinite capacity

    for u, v, w in edges:
        bottleneck[u][v] = w
        bottleneck[v][u] = w  # undirected

    # Step 2: Floyd-Warshall variant
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Update path i->j via k
                bottleneck[i][j] = max(bottleneck[i][j],
                                       min(bottleneck[i][k], bottleneck[k][j]))

    return bottleneck
