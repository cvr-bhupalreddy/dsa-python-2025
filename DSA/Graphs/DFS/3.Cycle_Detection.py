from collections import deque, defaultdict


def dfs_cycle_timer_directed(graph):
    start = {}
    finish = {}
    timer = 0
    cycle_found = False

    def dfs(u):
        nonlocal timer, cycle_found
        if cycle_found:
            return
        timer += 1
        start[u] = timer

        for v in graph.get(u, []):
            if v not in start:
                dfs(v)
            elif v not in finish:
                # back edge → cycle
                cycle_found = True
                return

        timer += 1
        finish[u] = timer

    for u in graph:
        if u not in start:
            dfs(u)

    return cycle_found, start, finish


def dfs_cycle_timer_undirected(graph):
    start = {}
    finish = {}
    timer = 0
    cycle_found = False

    def dfs(u, parent):
        nonlocal timer, cycle_found
        if cycle_found:
            return
        timer += 1
        start[u] = timer

        for v in graph.get(u, []):
            if v not in start:
                dfs(v, u)
            elif v != parent and v not in finish:
                cycle_found = True
                return

        timer += 1
        finish[u] = timer

    for u in graph:
        if u not in start:
            dfs(u, None)

    return cycle_found, start, finish


def dfs_cycle_color_directed(graph):
    color = {u: "white" for u in graph}
    cycle_found = False

    def dfs(u):
        nonlocal cycle_found
        if cycle_found:
            return
        color[u] = "grey"
        for v in graph.get(u, []):
            if color[v] == "grey":
                cycle_found = True
                return
            elif color[v] == "white":
                dfs(v)
        color[u] = "black"

    for u in graph:
        if color[u] == "white":
            dfs(u)

    return cycle_found, color


def dfs_cycle_color_undirected(graph):
    color = {u: "white" for u in graph}
    cycle_found = False

    def dfs(u, parent):
        nonlocal cycle_found
        if cycle_found:
            return
        color[u] = "grey"
        for v in graph.get(u, []):
            if color[v] == "white":
                dfs(v, u)
            elif v != parent:
                cycle_found = True
                return
        color[u] = "black"

    for u in graph:
        if color[u] == "white":
            dfs(u, None)

    return cycle_found, color


# 3️⃣ Kahn’s Algorithm (Directed Graph)

def cycle_kahn(graph):
    indegree = defaultdict(int)
    for u in graph:
        for v in graph[u]:
            indegree[v] += 1

    queue = deque([u for u in graph if indegree[u] == 0])
    count = 0

    while queue:
        u = queue.popleft()
        count += 1
        for v in graph.get(u, []):
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # If all nodes not processed → cycle exists
    return count != len(graph)

# | Approach         | Graph Type     | Uses Timer? | Uses Color? | Key Idea                              |
# | ---------------- | -------------- | ----------- | ----------- | ------------------------------------- |
# | DFS (Timer)      | Directed/Undir | ✅           | ❌           | Start/finish times, back edge → cycle |
# | DFS (Color)      | Directed/Undir | ❌           | ✅           | Grey node → back edge → cycle         |
# | Kahn’s Algorithm | Directed       | ❌           | ❌           | Topological sort fails → cycle        |
