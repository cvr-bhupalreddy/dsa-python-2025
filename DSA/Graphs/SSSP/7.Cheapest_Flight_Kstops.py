# 🔹 Cheapest Flight Within K Stops
# 📌 Problem Explanation
#
# You are given:
# n cities labeled 0 … n-1
#
# A list of flights
# flights[i] = [u, v, price]
# meaning a flight from u → v with cost price
#
# A source city src
# A destination city dst
# An integer K → maximum allowed stops


# 🔹 Why Normal Dijkstra Fails
# Standard Dijkstra:
#     Minimizes cost only
#     Ignores number of stops
#
# But here:
#     Path with more stops but cheaper cost may be invalid
#     Path with less stops but higher cost may be valid

# ➡️ Cost + Stops = state constraint

# 🔹 Modified Relaxation Rule
#     We allow visiting a node multiple times if:
#         cost is smaller
#         stops are within limit


# 1. Build adjacency list
# 2. Use min-heap
# 3. Push (0, src, 0)
# 4. While heap not empty:
#     pop smallest cost
#     if node == dst → return cost
#     if stops > K → skip
#         relax neighbors


import heapq
from collections import defaultdict, deque
from typing import List


def findCheapestPrice(n, flights, src, dst, K):
    # Build adjacency list: city -> [(neighbor, price)]
    adj = defaultdict(list)
    for u, v, w in flights:
        adj[u].append((v, w))

    # Min-heap storing (total_cost, current_city, stops_used)
    heap = [(0, src, 0)]

    # best[(city, stops)] = minimum cost to reach `city` using `stops` flights
    best = {}

    while heap:
        cost, city, stops = heapq.heappop(heap)

        # If destination is reached, this is the minimum possible cost
        if city == dst:
            return cost

        # If stops exceed allowed limit, skip this path
        if stops > K:
            continue

        # Explore neighbors
        for nei, price in adj[city]:
            new_cost = cost + price
            new_stops = stops + 1

            # Relaxation condition:
            # Allow visiting the same city again if:
            # - it is reached with fewer stops
            # - or with lower cost for same stops
            if (nei, new_stops) not in best or new_cost < best[(nei, new_stops)]:
                best[(nei, new_stops)] = new_cost
                heapq.heappush(heap, (new_cost, nei, new_stops))

    # Destination not reachable within K stops
    return -1


def findCheapestPrice_2(n, flights, src, dst, K):
    graph = defaultdict(list)

    for u, v, w in flights:
        graph[u].append((v, w))

    # (cost, node, stops)
    pq = [(0, src, 0)]

    # best[node][stops] = minimum cost
    best = [[float('inf')] * (K + 2) for _ in range(n)]
    best[src][0] = 0

    while pq:
        cost, u, stops = heapq.heappop(pq)

        # reached destination
        if u == dst:
            return cost

        # stop limit exceeded
        if stops > K:
            continue

        for v, price in graph[u]:
            new_cost = cost + price

            if new_cost < best[v][stops + 1]:
                best[v][stops + 1] = new_cost
                heapq.heappush(pq, (new_cost, v, stops + 1))

    return -1


# Can we remove the heap?
# ✅ YES — because of the K stops constraint
#
# Key observation:
#     Max path length = K + 1 edges
#     We don’t need global shortest path
#     We only care about paths with ≤ K stops
#
# So we can do:
#     Level-by-level BFS
#     Each level = 1 flight taken
#     Relax costs like Bellman-Ford
#     This is exactly Bellman-Ford with K+1 iterations, optimized with a queue.


def CheapestFlight_queue(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v, w in flights:
        adj[u].append((v, w))

    # Distance array per node per stops: best[node][stops] = min cost
    best = [[float('inf')] * (k + 2) for _ in range(n)]
    best[src][0] = 0

    # Queue storing elements: (stops_used, node, cost_so_far)
    q = deque()
    q.append((0, src, 0))

    while q:
        stops, node, cost = q.popleft()

        if stops > k:
            continue

        for nei, wt in adj[node]:
            new_cost = cost + wt
            new_stops = stops + 1

            if new_cost < best[nei][new_stops]:
                best[nei][new_stops] = new_cost
                q.append((new_stops, nei, new_cost))

    ans = min(best[dst])
    return -1 if ans == float('inf') else ans


def CheapestFlight_queue2(n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
    # Build adjacency list
    adj = [[] for _ in range(n)]
    for u, v, w in flights:
        adj[u].append((v, w))

    # Distance array per node per stops: best[node][stops] = min cost
    best = [float('inf')] * n
    best[src] = 0

    # Queue storing elements: (stops_used, node, cost_so_far)
    q = deque()
    q.append((0, src, 0))

    while q:
        stops, node, cost = q.popleft()

        if stops > k:
            continue

        for nei, wt in adj[node]:
            new_cost = cost + wt

            if new_cost < best[nei] and stops <= k:
                best[nei] = new_cost
                q.append((stops+1, nei, new_cost))

    return -1 if best[dst] == float('inf') else best[dst]
