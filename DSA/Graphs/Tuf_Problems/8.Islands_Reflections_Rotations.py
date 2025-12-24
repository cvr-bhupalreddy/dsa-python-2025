# VISUAL TIPS
#
# Draw the island on paper/grid
# Label coordinates relative to (0,0)
#
# Apply rotations:
#     90°: (x, y) → (y, -x)
#     180°: (x, y) → (-x, -y)
#     270°: (x, y) → (-y, x)
#
# Apply flips:
#     Horizontal: (x, y) → (-x, y)
#     Vertical: (x, y) → (x, -y)
#
# Normalize coordinates so top-left = (0,0) after each transformation


def num_distinct_islands_all_transforms(grid):
    if not grid or not grid[0]:
        return 0

    n, m = len(grid), len(grid[0])
    visited = [[False] * m for _ in range(n)]
    shapes = set()

    directions = [
        (-1, 0), (1, 0), (0, -1), (0, 1)
    ]

    def dfs(r, c, r0, c0, shape):
        visited[r][c] = True
        shape.append((r - r0, c - c0))
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < n and 0 <= nc < m:
                if grid[nr][nc] == 1 and not visited[nr][nc]:
                    dfs(nr, nc, r0, c0, shape)

    def canonical(shape):
        transformations = []

        for flip_x in [1, -1]:
            for flip_y in [1, -1]:
                for rotate in [0, 1, 2, 3]:  # 0°, 90°, 180°, 270°
                    temp = []
                    for x, y in shape:
                        # Apply flip
                        x1, y1 = x * flip_x, y * flip_y
                        # Apply rotation
                        for _ in range(rotate):
                            x1, y1 = y1, -x1
                        temp.append((x1, y1))
                    # Normalize coordinates
                    min_x = min(x for x, y in temp)
                    min_y = min(y for x, y in temp)
                    normalized = sorted((x - min_x, y - min_y) for x, y in temp)
                    transformations.append(tuple(normalized))
        return min(transformations)

    for i in range(n):
        for j in range(m):
            if grid[i][j] == 1 and not visited[i][j]:
                shape = []
                dfs(i, j, i, j, shape)
                shapes.add(canonical(shape))

    return len(shapes)


def main():
    grid = [
        [1,1,0,0,0],
        [1,0,0,0,0],
        [0,0,0,1,1],
        [0,0,0,0,1]
    ]

    print("Number of distinct islands (with rotations/reflections):",
          num_distinct_islands_all_transforms(grid))


if __name__ == "__main__":
    main()
