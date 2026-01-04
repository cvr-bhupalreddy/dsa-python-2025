# Repeatedly compare adjacent elements and swap them if they are in
# the wrong order. After each pass, the largest (or smallest) element
# moves to its correct position.


# 1️⃣ Bubble Sort – Ascending (Standard, j → right)

def bubble_sort_ascending(arr):
    n = len(arr)

    for i in range(n):
        swapped = False  # optimization flag

        # Last i elements are already in place
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                # Swap adjacent elements
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        # If no swap occurred, array is already sorted
        if not swapped:
            break


# 2️⃣ Bubble Sort – Descending

def bubble_sort_descending(arr):
    n = len(arr)

    for i in range(n):
        swapped = False

        for j in range(0, n - i - 1):
            if arr[j] < arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True

        if not swapped:
            break


# 3️⃣ Bubble Sort – Ascending (j from right → left)

def bubble_sort_ascending_reverse(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]


# 4️⃣ Bubble Sort – Descending (j from right → left)

def bubble_sort_descending_reverse(arr):
    n = len(arr)

    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] > arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
