def dfs_recursive(graph, start):
    visited = set()
    result = []

    def dfs(v):
        visited.add(v)
        result.append(v)
        for neighbor in graph.get(v, []):
            if neighbor not in visited:
                dfs(neighbor)

    dfs(start)
    return result


def dfs_iterative(graph, start):
    visited = set()
    result = []
    stack = [start]

    while stack:
        v = stack.pop()
        if v not in visited:
            visited.add(v)
            result.append(v)
            # Push neighbors in reverse order for same order as recursive
            for neighbor in reversed(graph.get(v, [])):
                if neighbor not in visited:
                    stack.append(neighbor)
    return result
