# Check if array represents a Min-Heap
def is_min_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):  # only non-leaf nodes
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] > arr[left]:
            return False
        if right < n and arr[i] > arr[right]:
            return False
    return True


# Check if array represents a Max-Heap
def is_max_heap(arr):
    n = len(arr)
    for i in range((n - 2) // 2 + 1):  # only non-leaf nodes
        left = 2 * i + 1
        right = 2 * i + 2
        if left < n and arr[i] < arr[left]:
            return False
        if right < n and arr[i] < arr[right]:
            return False
    return True
