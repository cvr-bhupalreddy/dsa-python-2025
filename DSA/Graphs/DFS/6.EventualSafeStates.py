# What is the “Eventual Safe States” Problem?
#
# A node in a directed graph is called SAFE
# if every possible path starting from that node
# eventually ends at a terminal node (node with no outgoing edges).
#
# If there exists ANY path from that node that leads to a cycle,
# then the node is NOT safe.


# A node with no outgoing edges.
# (out-degree = 0)
#
#
# Intuition
#     • Cycles are dangerous
#     • Any node that can reach a cycle is unsafe
#     • Nodes that eventually reach only terminal nodes are safe

#
# • Use DFS to detect cycles
# • Track node states:
#     0 → unvisited
#     1 → visiting (in recursion stack)
#     2 → safe (processed, no cycle reachable)
#
# • If during DFS we revisit a "visiting" node → cycle
# • Any node leading to cycle is unsafe
# • Nodes finishing DFS without cycles are safe


def eventual_safe_nodes(graph):
    n = len(graph)

    # state meanings:
    # 0 = unvisited
    # 1 = visiting (in recursion stack)
    # 2 = safe (no cycle reachable)
    state = [0] * n

    def dfs(u):
        # If node is already visited:
        # - state == 1 → cycle found → unsafe
        # - state == 2 → already known safe
        if state[u] != 0:
            return state[u] == 2

        # Mark node as visiting (enter recursion stack)
        state[u] = 1

        # Explore all outgoing edges
        for v in graph[u]:
            # If any neighbor leads to cycle → this node unsafe
            if not dfs(v):
                return False

        # All neighbors are safe → this node is safe
        state[u] = 2
        return True

    # Run DFS for every node (graph may be disconnected)
    safe_nodes = []
    for i in range(n):
        if dfs(i):
            safe_nodes.append(i)

    return safe_nodes


def eventual_safe_nodes_1(graph):
    n = len(graph)
    state = [0] * n  # 0=unvisited, 1=visiting, 2=safe

    def dfs(u):
        if state[u] != 0:
            return state[u] == 2

        state[u] = 1  # visiting
        for v in graph[u]:
            if not dfs(v):
                return False

        state[u] = 2  # safe
        return True

    # Run DFS only on unvisited nodes
    for i in range(n):
        if state[i] == 0:
            dfs(i)

    # Collect safe nodes
    return [i for i in range(n) if state[i] == 2]


# • visiting nodes tracked by recursion stack
# • if DFS reaches a node already in recursion stack → cycle
# • if DFS finishes node without detecting cycle → safe
# • memoize safe nodes to avoid reprocessing


# DFS with visited + path

def eventual_safe_nodes_dfs_alt(graph):
    n = len(graph)

    visited = set()  # nodes fully processed
    safe = set()  # nodes determined to be safe
    path = set()  # nodes in current recursion stack

    def dfs(u):
        if u in safe:
            return True  # already known safe
        if u in path:
            return False  # cycle detected
        if u in visited:
            return False  # visited but unsafe

        path.add(u)
        for v in graph[u]:
            if not dfs(v):
                return False
        path.remove(u)

        visited.add(u)
        safe.add(u)
        return True

    result = []
    for i in range(n):
        if dfs(i):
            result.append(i)

    return result


# Using DFS Times
# start[u]  → when DFS enters node u
# finish[u] → when DFS exits node u
#
#
# During DFS from node u, if you encounter a neighbor v:
#     • If start[v] exists but finish[v] is not yet assigned → back edge → cycle
#
# Nodes that never lead to back edges are safe.
# You can also store parent info if needed for path tracking.

def eventual_safe_nodes_dfs_timer(graph):
    n = len(graph)
    start = {}
    finish = {}
    safe_nodes = []
    timer = 0  # nonlocal counter

    def dfs(u):
        nonlocal timer
        if u in start:  # node already entered DFS
            if u not in finish:  # back edge → cycle
                return False
            else:  # finished → safe
                return True

        timer += 1
        start[u] = timer

        for v in graph[u]:
            if not dfs(v):
                return False

        timer += 1
        finish[u] = timer  # mark safe
        return True

    for u in range(n):
        if u not in start:
            dfs(u)

    # nodes with finish time assigned are safe
    safe_nodes = [u for u in range(n) if u in finish]
    return safe_nodes
