# • Dynamic Programming / Relaxation
# • Relax all edges V-1 times
# • Can handle NEGATIVE weights
# • Can detect NEGATIVE cycles


def bellman_ford(n, edges, src):
    dist = [float('inf')] * n
    dist[src] = 0

    # Relax edges V-1 times
    for _ in range(n - 1):
        updated = False
        for u, v, w in edges:
            if dist[u] != float('inf') and dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                updated = True
        if not updated:
            break

    # Detect negative cycle
    for u, v, w in edges:
        if dist[u] != float('inf') and dist[u] + w < dist[v]:
            return None  # Negative cycle detected

    return dist
