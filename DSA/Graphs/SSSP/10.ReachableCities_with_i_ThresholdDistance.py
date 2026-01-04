# 1. We need shortest distances between all pairs of cities.
# 2. Floyd-Warshall algorithm is perfect for dense graphs or small n (n ≤ 200).
# 3. Initialize distance matrix:
#     - dist[i][j] = 0 if i==j, else INF
#     - Set direct edge weights
# 4. Run Floyd-Warshall:
#     - dist[i][j] = min(dist[i][j], dist[i][k] + dist[k][j]) for all i,j,k
# 5. After computing all-pairs shortest distances:
#     - For each city i, count number of cities j (i≠j) with dist[i][j] ≤ distanceThreshold
# 6. Select the city with:
#     - Smallest reachable count
#     - If tie → largest city index


def findTheCity(n, edges, distanceThreshold):
    """
    Find the city with the smallest number of reachable cities within a given distance threshold.

    Parameters:
        n (int) : number of cities (0 to n-1)
        edges (List[List[int]]) : edges[i] = [u, v, weight]
        distanceThreshold (int) : maximum allowed distance

    Returns:
        int : city index with smallest number of reachable cities (largest index if tie)
    """

    # ------------------------------
    # Step 1: Initialize distance matrix
    # ------------------------------
    INF = float('inf')
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0  # Distance to self is 0

    # ------------------------------
    # Step 2: Set direct edge distances
    # ------------------------------
    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w  # undirected graph

    # ------------------------------
    # Step 3: Floyd-Warshall Algorithm
    # ------------------------------
    for k in range(n):
        for i in range(n):
            for j in range(n):
                # Check if path via k is shorter
                if dist[i][k] + dist[k][j] < dist[i][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    # ------------------------------
    # Step 4: Count reachable cities within threshold
    # ------------------------------
    min_count = n + 1       # start with a value larger than max possible
    city_ans = -1

    for i in range(n):
        count = 0
        for j in range(n):
            if i != j and dist[i][j] <= distanceThreshold:
                count += 1

        # Update answer based on smallest count and largest index in tie
        if count < min_count or (count == min_count and i > city_ans):
            min_count = count
            city_ans = i

    return city_ans


# | Approach    | Core Idea                | Time Complexity  | Space Complexity | Suitable For
# | ----------- | ------------------------ | ---------------- | ---------------- | -----------------------------------
# | Brute Force | Floyd-Warshall all pairs | O(n³)            | O(n²)            | Small n ≤ 200, dense graph
# | Better      | Dijkstra from each city  | O(n * (E log n)) | O(n + E)         | Sparse graph, moderate n
# | Optimal     | Dijkstra + early pruning | O(n * (E log n)) | O(n + E)         | Sparse graph, large n, threshold
