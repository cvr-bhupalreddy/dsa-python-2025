# 🔹 Insertion Sort
#     Build a sorted portion of the array one element at a time
#     by inserting each new element into its correct position.


# 1️⃣ Insertion Sort – Ascending (Standard)

def insertion_sort_ascending(arr):
    n = len(arr)

    # Start from second element
    for i in range(1, n):
        key = arr[i]  # element to be inserted
        j = i - 1

        # Shift elements to the right
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # Insert key at correct position
        arr[j + 1] = key


# 2️⃣ Insertion Sort – Descending


def insertion_sort_descending(arr):
    n = len(arr)

    for i in range(1, n):
        key = arr[i]
        j = i - 1

        # Shift smaller elements right
        while j >= 0 and arr[j] < key:
            arr[j + 1] = arr[j]
            j -= 1

        arr[j + 1] = key


# 📊 Bubble vs Insertion – Quick Comparison
# | Property   | Bubble Sort | Insertion Sort     |
# | ---------- | ----------- | ------------------ |
# | Best Case  | O(n)        | O(n)               |
# | Worst Case | O(n²)       | O(n²)              |
# | Stable     | ✅           | ✅                  |
# | Adaptive   | ❌           | ✅                  |
# | Swaps      | High        | Low                |
# | Use Case   | Educational | Nearly sorted data |
