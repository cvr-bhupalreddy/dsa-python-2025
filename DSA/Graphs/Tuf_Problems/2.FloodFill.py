def flood_fill(image, sr, sc, newColor):
    rows, cols = len(image), len(image[0])
    original_color = image[sr][sc]

    # If starting pixel already has newColor, no need to process
    if original_color == newColor:
        return image

    # 4-directional movement
    directions = [
        (-1, 0),  # up
        (1, 0),   # down
        (0, -1),  # left
        (0, 1)    # right
    ]

    def dfs(r, c):
        # Boundary check and color match
        if r < 0 or r >= rows or c < 0 or c >= cols:
            return
        if image[r][c] != original_color:
            return

        # Change color
        image[r][c] = newColor

        # Visit neighbors
        for dr, dc in directions:
            dfs(r + dr, c + dc)

    dfs(sr, sc)
    return image


def main():
    image = [
        [1, 1, 1],
        [1, 1, 0],
        [1, 0, 1]
    ]

    sr, sc = 1, 1
    newColor = 2

    result = flood_fill(image, sr, sc, newColor)
    print("Flood Filled Image:")
    for row in result:
        print(row)


if __name__ == "__main__":
    main()
