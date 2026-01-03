# Core Insight (Very Important)
# 🔑 This is a shortest path problem on a graph where:
# Nodes = numbers from 0 to 99999
# Edges = multiplying by an element of arr
# Each edge cost = 1


# All edges have equal weight (1)
# We need minimum steps
# 👉 Use BFS, not Dijkstra.


from collections import deque


def minimumMultiplications(arr, start, end):
    MOD = 100000

    # Edge case
    if start == end:
        return 0

    # Distance array (acts as visited + distance)
    dist = [-1] * MOD
    dist[start] = 0

    q = deque([start])

    while q:
        curr = q.popleft()

        for mul in arr:
            nxt = (curr * mul) % MOD

            # If not visited
            if dist[nxt] == -1:
                dist[nxt] = dist[curr] + 1

                # If reached target
                if nxt == end:
                    return dist[nxt]

                q.append(nxt)

    return -1
