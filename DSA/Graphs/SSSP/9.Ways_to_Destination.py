# Problem Recap
#
#     Weighted undirected graph with n intersections (0 to n-1)
#     roads[i] = [u, v, time]
#     Reachable: any intersection can be reached from any other
#     Question: Number of ways to reach n-1 from 0 in the shortest time
# Return result modulo 10^9 + 7

#
# 🔹 Core Idea
#
# Use Dijkstra's algorithm to find the shortest time from 0 → n-1
# Maintain a ways array: ways[i] = number of shortest paths to reach i
# When visiting a neighbor:
#     If new_distance < dist[neighbor] → update distance and set ways[neighbor] = ways[current]
#     If new_distance == dist[neighbor] → add ways[current] to ways[neighbor]
#
# Result = ways[n-1] % (10^9 + 7)
#
# Why Dijkstra?
#     Graph has positive edge weights (timei)
#     Need shortest path time, not just steps


import heapq

MOD = 10**9 + 7  # To return result modulo 10^9+7

def countPaths(n, roads):
    """
    Count the number of ways to reach intersection n-1 from 0
    in the shortest travel time.

    Parameters:
        n (int) : Number of intersections (0 to n-1)
        roads (List[List[int]]) : Each road as [u, v, time]

    Returns:
        int : Number of shortest paths modulo 10^9+7
    """

    # ------------------------------
    # Step 1: Build adjacency list
    # ------------------------------
    # graph[u] = list of (v, time) for neighbors
    graph = [[] for _ in range(n)]
    for u, v, time in roads:
        graph[u].append((v, time))
        graph[v].append((u, time))  # Because roads are bi-directional

    # ------------------------------
    # Step 2: Initialize distance and ways arrays
    # ------------------------------
    dist = [float('inf')] * n  # dist[i] = shortest distance from 0 to i
    ways = [0] * n             # ways[i] = number of shortest paths to i
    dist[0] = 0                # Distance to starting point is 0
    ways[0] = 1                # One way to reach start (itself)

    # ------------------------------
    # Step 3: Use min-heap for Dijkstra
    # ------------------------------
    # Heap element = (current_time_to_node, node_index)
    heap = [(0, 0)]

    while heap:
        time_u, u = heapq.heappop(heap)

        # ------------------------------
        # Skip if we already have a shorter path to u
        # ------------------------------
        if time_u > dist[u]:
            continue

        # ------------------------------
        # Explore neighbors of u
        # ------------------------------
        for v, t in graph[u]:
            new_time = time_u + t  # total time if we go from 0 → u → v

            if new_time < dist[v]:
                # Found strictly shorter path to v
                dist[v] = new_time
                ways[v] = ways[u]   # All paths to u extend to v
                heapq.heappush(heap, (new_time, v))

            elif new_time == dist[v]:
                # Found another shortest path to v
                # Increment number of ways
                ways[v] = (ways[v] + ways[u]) % MOD

    # ------------------------------
    # Step 4: Return number of shortest paths to destination
    # ------------------------------
    return ways[n - 1] % MOD
