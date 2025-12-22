from collections import deque, defaultdict


def topological_sort_kahn(graph):
    indegree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([u for u in graph if indegree[u] == 0])
    result = []

    while queue:
        u = queue.popleft()
        result.append(u)
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    if len(result) != len(graph):
        raise ValueError("Graph has a cycle, topological order not possible")
    return result


def topological_sort_dfs(graph):
    visited = set()
    result = []

    def dfs(u):
        visited.add(u)
        for v in graph.get(u, []):
            if v not in visited:
                dfs(v)
        result.append(u)  # add after visiting neighbors

    for u in graph:
        if u not in visited:
            dfs(u)

    result.reverse()  # reverse to get topological order
    return result


def topological_sort_dfs_timer(graph):
    start = {}  # discovery time
    finish = {}  # finish time
    result = []
    timer = 0
    cycle_found = False

    def dfs(u):
        nonlocal timer, cycle_found
        if cycle_found:  # stop if cycle detected
            return

        timer += 1
        start[u] = timer

        for v in graph.get(u, []):
            if v not in start:
                dfs(v)
            elif v not in finish:
                # back edge detected → cycle
                cycle_found = True
                return

        timer += 1
        finish[u] = timer
        result.append(u)  # add after visiting neighbors

    for u in graph:
        if u not in start:
            dfs(u)

    if cycle_found:
        return None, True  # cycle exists, topo order not possible

    result.reverse()
    return result, False


def topological_sort_dfs_cycle(graph):
    color = {u: "white" for u in graph}  # white=unvisited, grey=visiting, black=finished
    result = []
    cycle_found = False

    def dfs(u):
        nonlocal cycle_found
        if cycle_found:  # stop recursion if cycle detected
            return
        color[u] = "grey"
        for v in graph.get(u, []):
            if color[v] == "white":
                dfs(v)
            elif color[v] == "grey":
                # back edge detected → cycle
                cycle_found = True
                return
        color[u] = "black"
        result.append(u)  # add after visiting neighbors

    for u in graph:
        if color[u] == "white":
            dfs(u)

    if cycle_found:
        return None, True  # cycle exists, topological order not possible

    result.reverse()
    return result, False

# ✅ Notes & Complexity
# | Method     | Time Complexity | Space Complexity | Key Idea                                   |
# | ---------- | --------------- | ---------------- | ------------------------------------------ |
# | DFS        | O(V+E)          | O(V) recursion   | Append after DFS, reverse result           |
# | Kahn (BFS) | O(V+E)          | O(V)             | Indegree 0 nodes first, remove iteratively |
