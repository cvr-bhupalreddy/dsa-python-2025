# • Terminal nodes (out-degree = 0) are always safe
# • Nodes that eventually reach only safe nodes are themselves safe
# • Unsafe nodes are part of or reach a cycle


# Idea: Reverse the graph and remove edges like Kahn’s topological sort:
#
# 1. Reverse edges: u → v becomes v → u
# 2. Count original out-degree for each node
# 3. Push terminal nodes (out-degree=0) into queue
# 4. While queue not empty:
#     - Pop node u (safe)
#     - For each predecessor v in reversed graph:
#         - Decrease out-degree[v] by 1
#         - If out-degree[v] == 0 → push v (safe)
# 5. All nodes processed = safe nodes
#
# Why This Works
# • Terminal nodes are obviously safe
# • Reverse edges allow us to propagate safety backward
# • Nodes whose out-degree reduces to 0 in reversed graph → eventually reach terminal
# • Nodes stuck in cycles never reach out-degree 0 → unsafe


from collections import deque


def eventual_safe_nodes_bfs(graph):
    n = len(graph)

    # -------------------------------
    # Step 1: Prepare reverse graph
    # -------------------------------
    # For each node u, rev_graph[v] contains all nodes u that point to v in original graph
    # This helps to propagate "safeness" backwards from terminal nodes
    rev_graph = [[] for _ in range(n)]

    # Store out-degree of each node (number of outgoing edges)
    out_degree = [0] * n

    for u in range(n):
        # Original out-degree
        out_degree[u] = len(graph[u])
        for v in graph[u]:
            # Reverse the edge: u -> v becomes v -> u
            rev_graph[v].append(u)

    # -------------------------------
    # Step 2: Initialize BFS queue
    # -------------------------------
    # Terminal nodes (out-degree 0) are immediately safe
    queue = deque([i for i in range(n) if out_degree[i] == 0])

    # Boolean array to mark safe nodes
    safe = [False] * n

    # -------------------------------
    # Step 3: BFS to propagate safeness
    # -------------------------------
    while queue:
        u = queue.popleft()
        safe[u] = True  # Node u is safe
        for v in rev_graph[u]:
            # Remove the edge u -> v (reduce out-degree)
            out_degree[v] -= 1
            # If all outgoing edges are removed → node becomes safe
            if out_degree[v] == 0:
                queue.append(v)

    # -------------------------------
    # Step 4: Collect all safe nodes
    # -------------------------------
    return [i for i in range(n) if safe[i]]


# • Terminal nodes always safe
# • Reverse edges + Kahn’s topological idea propagates safety
# • Nodes that cannot reach out-degree 0 are unsafe (cycle)
# • BFS approach avoids recursion and is intuitive for cycle-heavy graphs


# Use Kahn's algorithm on reversed graph

def eventual_safe_nodes(graph):
    n = len(graph)

    # -------------------------------------------------
    # Step 1: Build reversed graph & indegree array
    # -------------------------------------------------

    # reversed_graph[v] = list of nodes that point to v
    reversed_graph = [[] for _ in range(n)]

    # indegree[i] = number of outgoing edges of i (original graph)
    # This becomes "indegree" in the reversed graph
    indegree = [0] * n

    for u in range(n):
        indegree[u] = len(graph[u])  # count outgoing edges
        for v in graph[u]:
            reversed_graph[v].append(u)

    # -------------------------------------------------
    # Step 2: Initialize queue with terminal nodes
    # -------------------------------------------------

    # Nodes with indegree 0 → terminal nodes → safe
    queue = deque()
    for i in range(n):
        if indegree[i] == 0:
            queue.append(i)

    # -------------------------------------------------
    # Step 3: Kahn’s BFS
    # -------------------------------------------------

    safe = [False] * n

    while queue:
        node = queue.popleft()
        safe[node] = True  # confirmed safe

        # Remove edges pointing to this node
        for parent in reversed_graph[node]:
            indegree[parent] -= 1
            # If all outgoing edges removed → safe
            if indegree[parent] == 0:
                queue.append(parent)

    # -------------------------------------------------
    # Step 4: Collect safe nodes
    # -------------------------------------------------

    return [i for i in range(n) if safe[i]]
