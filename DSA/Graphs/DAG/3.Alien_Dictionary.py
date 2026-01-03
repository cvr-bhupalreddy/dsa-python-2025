# 🧠 Problem Restated
#
# You are given:
#     A sorted list of words in an unknown (alien) language
#     The alphabet size is K (characters are among first K letters)
#
# Your task:
# 👉 Deduce a valid order of characters that makes the dictionary sorted.
#
# This is a graph + topological sort problem.


# Sorted dictionary
# ↓
# First mismatch between adjacent words
# ↓
# Directed edge (ordering constraint)
# ↓
# Build DAG
# ↓
# Topological Sort
# ↓
# Valid character order


from collections import defaultdict, deque


def findOrder(words, N, K):
    """
    words : list of sorted alien words
    N     : number of words
    K     : number of unique characters (first K letters)
    """

    # -----------------------------
    # STEP 1: Graph Initialization
    # -----------------------------
    # adjacency list for graph
    graph = defaultdict(list)

    # indegree count for each character
    indegree = [0] * K

    # -----------------------------
    # STEP 2: Build the DAG
    # -----------------------------
    for i in range(N - 1):
        w1 = words[i]
        w2 = words[i + 1]

        # invalid case:
        # longer word comes before its prefix
        if len(w1) > len(w2) and w1.startswith(w2):
            return ""

        # find first differing character
        for j in range(min(len(w1), len(w2))):
            if w1[j] != w2[j]:
                u = ord(w1[j]) - ord('a')
                v = ord(w2[j]) - ord('a')

                # add edge u -> v if not already added
                if v not in graph[u]:
                    graph[u].append(v)
                    indegree[v] += 1
                break  # only first mismatch matters

    # -----------------------------
    # STEP 3: Topological Sort (Kahn)
    # -----------------------------
    queue = deque()

    # push all characters with indegree 0
    for i in range(K):
        if indegree[i] == 0:
            queue.append(i)

    topo = []

    while queue:
        u = queue.popleft()
        topo.append(u)

        for v in graph[u]:
            indegree[v] -= 1
            if indegree[v] == 0:
                queue.append(v)

    # -----------------------------
    # STEP 4: Cycle Detection
    # -----------------------------
    # if topo sort does not include all characters
    if len(topo) != K:
        return ""

    # -----------------------------
    # STEP 5: Convert to string
    # -----------------------------
    result = ""
    for ch in topo:
        result += chr(ch + ord('a'))

    return result
