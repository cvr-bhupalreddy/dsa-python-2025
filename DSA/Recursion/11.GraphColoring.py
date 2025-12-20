# Graph Coloring – Core Idea (Copy-Ready)
#
# Problem: Assign colors to all vertices of a graph such that no two adjacent vertices share the same color,
# using at most M colors.
#
# Core Idea (Backtracking / Recursion):
#
# 1. Start from vertex 0.
# 2. For each vertex, try assigning every color from 1 to M.
# 3. Before assigning a color, check if it is safe:
#     - A color is safe if none of the adjacent vertices already have that color.
# 4. If safe:
# - Assign the color.
# - Move to the next vertex recursively.
# 5. If no color works, backtrack by removing the color and return to the previous vertex.
# 6. If all vertices are colored successfully, record the solution.
#
# Safety Check Rule:
# For a vertex v, color c is valid only if:
# No neighbor u of v has color c.
#
# Base Case:
# If vertex == n (all vertices colored), record/add the solution.
#
# Recurrence:
# For each color c in 1..M:
# If safe(v, c):
# assign c
# recurse on v+1
# backtrack
from typing import List


def graph_coloring(graph: List[List[int]], M: int) -> List[List[int]]:
    """
    graph: adjacency matrix of size n x n
    M: number of colors
    returns: list of all valid colorings
    """
    n = len(graph)
    res = []

    def is_safe(vertex, color, coloring):
        for neighbor in range(n):
            if graph[vertex][neighbor] == 1 and coloring[neighbor] == color:
                return False
        return True

    def helper(vertex, coloring):
        if vertex == n:
            res.append(coloring.copy())
            return

        for color in range(1, M+1):
            if is_safe(vertex, color, coloring):
                coloring[vertex] = color
                helper(vertex + 1, coloring)
                coloring[vertex] = 0  # backtrack

    coloring = [0] * n
    helper(0, coloring)
    return res
