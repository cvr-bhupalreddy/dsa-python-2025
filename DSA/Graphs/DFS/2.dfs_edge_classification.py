# ✅ How it Works
#
# Tree edge: (u, v) where v is first visited (v not in visited)
# Back edge: (u, v) where v is discovered but not finished (finish[v] == 0) → points to ancestor
# Forward edge: (u, v) where v is already finished, but start[u] < start[v] → points to descendant
# Cross edge: (u, v) where v is already finished, and start[u] > start[v] → points to non-descendant
# Parent tracking is used only for tree edges, not for classification.

def dfs_times_parents(graph):
    start = {}
    finish = {}
    parent = {u: None for u in graph}
    visited = set()
    edges = []

    timer = 0  # nonlocal counter

    def dfs(u):
        nonlocal timer
        visited.add(u)
        timer += 1
        start[u] = timer

        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                edges.append((u, v, "tree"))
                dfs(v)
            else:
                edges.append((u, v, "back_or_cross"))

        timer += 1
        finish[u] = timer

    for u in graph:
        if u not in visited:
            dfs(u)

    return start, finish, parent, edges


def dfs_edge_classification_timer(graph):
    start = {}
    finish = {}
    parent = {u: None for u in graph}
    visited = set()
    edges = []

    timer = 0

    def dfs(u):
        nonlocal timer
        visited.add(u)
        timer += 1
        start[u] = timer

        for v in graph.get(u, []):
            if v not in visited:
                parent[v] = u
                edges.append((u, v, "tree"))
                dfs(v)
            else:
                # Edge already visited, classify using start/finish times
                if finish.get(v, 0) == 0:  # I can write as V not in finish
                    # v discovered but not finished → back edge
                    edges.append((u, v, "back"))
                elif start[u] < start[v]:
                    # u discovered before v finished → forward edge
                    edges.append((u, v, "forward"))
                else:
                    # u discovered after v finished → cross edge
                    edges.append((u, v, "cross"))

        timer += 1
        finish[u] = timer

    for u in graph:
        if u not in visited:
            dfs(u)

    return start, finish, parent, edges


def dfs_coloring_parents(graph):
    color = {u: "white" for u in graph}
    parent = {u: None for u in graph}
    edges = []

    def dfs(u):
        color[u] = "grey"
        for v in graph.get(u, []):
            if color[v] == "white":
                parent[v] = u
                edges.append((u, v, "tree"))
                dfs(v)
            elif color[v] == "grey":
                edges.append((u, v, "back"))
            elif color[v] == "black":
                edges.append((u, v, "forward_or_cross"))
        color[u] = "black"

    for u in graph:
        if color[u] == "white":
            dfs(u)

    return color, parent, edges
