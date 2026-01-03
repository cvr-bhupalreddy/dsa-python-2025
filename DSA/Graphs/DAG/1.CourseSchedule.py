from collections import defaultdict, deque


def can_finish(N, arr):
    graph = defaultdict(list)
    # graph = {i: [] for i in range(N)}

    indegree = [0] * N

    for a, b in arr:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque()
    for i in range(N):
        if indegree[i] == 0:
            queue.append(i)

    completed = 0

    while queue:
        node = queue.popleft()
        completed += 1

        for neighbor in graph[node]:  # safe even if node not in graph
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return completed == N


def finish_order(N, arr):
    graph = defaultdict(list)
    indegree = [0] * N

    for a, b in arr:
        graph[b].append(a)
        indegree[a] += 1

    queue = deque()
    for i in range(N):
        if indegree[i] == 0:
            queue.append(i)

    result = []

    while queue:
        node = queue.popleft()
        result.append(node)

        for neighbor in graph[node]:  # safe even if node not in graph
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)

    return result if len(result) == N else []
