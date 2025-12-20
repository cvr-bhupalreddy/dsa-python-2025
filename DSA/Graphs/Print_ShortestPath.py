import heapq

def dijkstra_with_path(V, adj, src):
    dist = [float('inf')] * V
    parent = [-1] * V  # to reconstruct path
    dist[src] = 0

    pq = [(0, src)]  # (distance, node)

    while pq:
        d, node = heapq.heappop(pq)
        if d > dist[node]:
            continue

        for neighbor, weight in adj[node]:
            new_dist = d + weight
            if new_dist < dist[neighbor]:
                dist[neighbor] = new_dist
                parent[neighbor] = node
                heapq.heappush(pq, (new_dist, neighbor))

    return dist, parent


def get_path(parent, target):
    """Reconstruct path from source to target"""
    path = []
    while target != -1:
        path.append(target)
        target = parent[target]
    path.reverse()
    return path


# Example usage
if __name__ == "__main__":
    adj = {
        0: [(1, 1), (2, 4)],
        1: [(2, 2), (3, 6)],
        2: [(3, 3)],
        3: []
    }

    V = 4
    src = 0
    dist, parent = dijkstra_with_path(V, adj, src)

    print("Shortest distances from source:", dist)
    print("Parent array:", parent)

    # Print shortest path to all nodes
    for i in range(V):
        path = get_path(parent, i)
        print(f"Path to {i}: {path}, Distance: {dist[i]}")
