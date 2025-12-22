# ==================== PRIM'S ALGORITHM ====================
# Core Idea
#     • Start from any node
#     • Use min-heap to select edge with smallest weight to unvisited nodes
#     • Repeat until all nodes included


# 1. Start from any node (say 0)
# 2. Use a min-heap to always pick the edge with minimum weight to an unvisited node
# 3. For each chosen edge, mark the new node as visited and add the edge to MST
# 4. Repeat until all nodes are included

import heapq
from collections import defaultdict


def prim_mst(n, edges):
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False] * n
    min_heap = [(0, 0)]  # (weight, node)
    mst_weight = 0
    mst_edges = []

    while min_heap:
        w, u = heapq.heappop(min_heap)
        if visited[u]:
            continue
        visited[u] = True
        mst_weight += w

        # Optional: track edges
        # For that, store (weight, from, to) in heap
        for v, weight in graph[u]:
            if not visited[v]:
                heapq.heappush(min_heap, (weight, v))

    return mst_weight


def prim_mst_with_edges(n, edges):
    """
    Returns MST weight and list of edges
    edges: list of (u, v, w)
    """
    graph = defaultdict(list)
    for u, v, w in edges:
        graph[u].append((v, w))
        graph[v].append((u, w))

    visited = [False] * n
    min_heap = [(0, -1, 0)]  # (weight, parent, current)
    mst_weight = 0
    mst_edges = []

    while min_heap:
        w, u, v = heapq.heappop(min_heap)
        if visited[v]:
            continue
        visited[v] = True
        mst_weight += w
        if u != -1:
            mst_edges.append((u, v, w))  # skip the initial dummy edge

        for to, weight in graph[v]:
            if not visited[to]:
                heapq.heappush(min_heap, (weight, v, to))

    return mst_weight, mst_edges
