# Heapify for max-heap
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)


# Heapify for min-heap
def min_heapify(arr, n, i):
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        min_heapify(arr, n, smallest)


# Convert Min-Heap to Max-Heap
def min_to_max_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        max_heapify(arr, n, i)


# Convert Max-Heap to Min-Heap
def max_to_min_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2, -1, -1):
        min_heapify(arr, n, i)
