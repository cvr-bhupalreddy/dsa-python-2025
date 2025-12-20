import heapq
from collections import defaultdict


def findCheapestPrice(n, flights, src, dst, K):
    # Build adjacency list
    adj = defaultdict(list)
    for u, v, w in flights:
        adj[u].append((v, w))

    # Min-heap: (cost, city, stops)
    heap = [(0, src, 0)]

    # Best cost to a city with stops used
    best = dict()  # (city, stops) -> cost

    while heap:
        cost, city, stops = heapq.heappop(heap)

        # If reached destination, return cost
        if city == dst:
            return cost

        # If stops exceed K, skip
        if stops > K:
            continue

        for nei, price in adj[city]:
            new_cost = cost + price
            if (nei, stops) not in best or new_cost < best[(nei, stops)]:
                best[(nei, stops)] = new_cost
                heapq.heappush(heap, (new_cost, nei, stops + 1))

    return -1



from collections import deque
from typing import List

class Solution:

    # Function to find cheapest price from
    # src to dst with at most k stops
    def CheapestFlight(self, n: int, flights: List[List[int]],
                       src: int, dst: int, k: int) -> int:

        # To store the graph
        adj = [[] for _ in range(n)]

        # Adding edges to the graph
        for it in flights:
            adj[it[0]].append((it[1], it[2]))

        # To store minimum distance
        minDist = [float('inf')] * n
        minDist[src] = 0
        # Queue storing the elements of
        # the form {stops, {node, dist}}
        q = deque([(0, src, 0)])

        # Until the queue is empty
        while q:

            # Get the element from queue
            stops, node, dist = q.popleft()

            # If the number of stops taken exceed k,
            # skip and move to the next element
            if stops > k:
                continue

            # Traverse all the neighbors
            for adjNode, edgeWt in adj[node]:

                # If the tentative distance to reach adjacent
                # node is smaller than the known distance
                # and number of stops doesn't exceed k
                if (dist + edgeWt < minDist[adjNode] and
                        stops <= k):

                    # Update the known distance
                    minDist[adjNode] = dist + edgeWt

                    # Add the new element to queue
                    q.append((stops + 1, adjNode, dist + edgeWt))

        # If the destination is unreachable, return -1
        if minDist[dst] == float('inf'):
            return -1

        # Otherwise return the result
        return minDist[dst]

if __name__ == "__main__":
    n = 4
    flights = [
        [0, 1, 100],
        [1, 2, 100],
        [2, 0, 100],
        [1, 3, 600],
        [2, 3, 200]
    ]

    src, dst, k = 0, 3, 1

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to determine cheapest flight from source to destination within K stops
    ans = sol.CheapestFLight(n, flights, src, dst, k)

    # Output
    print("The cheapest flight from source to destination within K stops is:", ans)
