# Since rows are sorted, for any guessed value mid:
#     Count how many numbers ≤ mid across all rows
# If count > half of elements → median is smaller or equal
# Else → median is larger
#
# Binary search on the value range:
# low = min element of matrix [first elements of all rows]
# high = max element of matrix [ last element of all rows ]


def median_matrix(mat):
    n, m = len(mat), len(mat[0])

    # Helper: count of elements <= x using binary search in each row
    def count_le(row, x):  # This function cost is N LogM
        low, high = 0, len(row) - 1
        while low <= high:
            mid = (low + high) // 2
            if row[mid] <= x:
                low = mid + 1
            else:
                high = mid - 1
        return low

    low = min(row[0] for row in mat)
    high = max(row[-1] for row in mat)

    target = (n * m) // 2  # median index

    while low < high: # this is called log(Max_Element) = it's constant max = 10^9 then 9 times
        mid = (low + high) // 2

        # count how many numbers <= mid
        count = 0
        for row in mat:
            count += count_le(row, mid)

        # If count > target, median is smaller
        if count > target:
            high = mid
        else:
            low = mid + 1

    return low


# | Approach                               | Time          | Space | When to Use                         |
# | -------------------------------------- | ------------- | ----- | ----------------------------------- |
# | **Brute: flatten + sort**              | O(NM log(NM)) | O(NM) | Easiest, but slow                   |
# | **Better: K-way merge**                | O(NM)         | O(N)  | Moderate matrices                   |
# | ⭐ **Optimal (binary search on value)** | O(N log MAX)  | O(1)  | Large matrices, best for interviews |
