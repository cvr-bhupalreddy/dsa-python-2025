import heapq


def dijkstra(V, adj, src):
    # V = number of vertices
    # adj = adjacency list, e.g. adj[u] = [(v, w), (x, w2), ...]

    dist = [float('inf')] * V
    dist[src] = 0
    pq = [(0, src)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)

        # Skip if we already found a shorter path
        if d > dist[node]:
            continue

        for neighbor, weight in adj[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                heapq.heappush(pq, (new_dist, neighbor))

    return dist
