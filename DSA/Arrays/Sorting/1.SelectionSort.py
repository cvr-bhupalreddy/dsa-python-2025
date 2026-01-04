# 📌 1️⃣ Selection Sort – Ascending (j from left → right)

def selection_sort_ascending(arr):
    n = len(arr)

    # One by one move boundary of unsorted subarray
    for i in range(n):
        min_idx = i  # assume current position has minimum

        # Find minimum in remaining unsorted array
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Place minimum at correct position
        arr[i], arr[min_idx] = arr[min_idx], arr[i]


# 📌 2️⃣ Selection Sort – Descending (j from left → right)

def selection_sort_descending(arr):
    n = len(arr)

    for i in range(n):
        max_idx = i  # assume current position has maximum

        # Find maximum element
        for j in range(i + 1, n):
            if arr[j] > arr[max_idx]:
                max_idx = j

        # Place maximum at front
        arr[i], arr[max_idx] = arr[max_idx], arr[i]


# 📌 3️⃣ Selection Sort – Ascending (j from right → left)

def selection_sort_ascending_from_end(arr):
    n = len(arr)

    # Reduce unsorted region from right
    for i in range(n - 1, -1, -1):
        max_idx = i  # assume last is maximum

        # Scan backwards
        for j in range(i - 1, -1, -1):
            if arr[j] > arr[max_idx]:
                max_idx = j

        # Place maximum at end
        arr[i], arr[max_idx] = arr[max_idx], arr[i]


# 📌 4️⃣ Selection Sort – Descending (j from right → left)

def selection_sort_descending_from_end(arr):
    n = len(arr)

    for i in range(n - 1, -1, -1):
        min_idx = i  # assume last is minimum

        # Find minimum by scanning backward
        for j in range(i - 1, -1, -1):
            if arr[j] < arr[min_idx]:
                min_idx = j

        # Place minimum at end
        arr[i], arr[min_idx] = arr[min_idx], arr[i]

# 📊 Comparison Summary
# | Variant | Order      | Inner Loop Direction | Element Selected |
# | ------- | ---------- | -------------------- | ---------------- |
# | #1      | Ascending  | Left → Right         | Minimum          |
# | #2      | Descending | Left → Right         | Maximum          |
# | #3      | Ascending  | Right → Left         | Maximum          |
# | #4      | Descending | Right → Left         | Minimum          |
#
# ⏱️ Complexity (Same for All)
# | Metric   | Value |
# | -------- | ----- |
# | Time     | O(n²) |
# | Swaps    | O(n)  |
# | Space    | O(1)  |
# | Stable   | ❌     |
# | In-Place | ✅     |

