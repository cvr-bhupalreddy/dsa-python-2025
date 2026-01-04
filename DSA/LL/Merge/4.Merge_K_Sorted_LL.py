import heapq

# ------------------------------
# Node class for linked list
# ------------------------------
class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # Required for heapq to compare Node objects
    def __lt__(self, other):
        return self.val < other.val


# ------------------------------
# Method 1: Merge K sorted linked lists using min-heap
# ------------------------------
def merge_k_lists(lists):
    """
    Merge k sorted linked lists using a min-heap (priority queue)
    Time: O(N log k) where N = total nodes, k = number of lists
    Space: O(k) for the heap
    """
    min_heap = []

    # Step 1: Push the head of each linked list into the min-heap
    for node in lists:
        if node:  # ignore empty lists
            heapq.heappush(min_heap, node)

    # Dummy node to simplify merged list creation
    dummy = Node(0)
    curr = dummy

    # Step 2: Repeatedly extract the smallest node and push its next
    while min_heap:
        node = heapq.heappop(min_heap)  # get the min node
        curr.next = node                # append to result
        curr = curr.next

        # If this node has a next node, push it into the heap
        if node.next:
            heapq.heappush(min_heap, node.next)

    return dummy.next


# ------------------------------
# Helper: Merge two sorted linked lists (used in divide and conquer)
# ------------------------------
def merge_two(l1, l2):
    """
    Merge two sorted linked lists using dummy node
    """
    dummy = Node(0)
    curr = dummy

    while l1 and l2:
        if l1.val <= l2.val:
            curr.next = l1
            l1 = l1.next
        else:
            curr.next = l2
            l2 = l2.next
        curr = curr.next

    # Attach remaining nodes from non-empty list
    curr.next = l1 if l1 else l2
    return dummy.next


# ------------------------------
# Method 2: Merge K sorted linked lists using divide & conquer
# ------------------------------
def merge_k_lists_divide_and_conquer(lists):
    """
    Merge k sorted linked lists using divide & conquer approach
    Time: O(N log k), Space: O(1) extra space
    """
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    # Keep merging pairs of lists until only one list remains
    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            # Handle odd number of lists
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two(l1, l2))

        lists = merged  # Update lists to the merged results

    return lists[0]


# ------------------------------
# Method 3: Merge K sorted arrays using min-heap
# ------------------------------
def merge_k_arrays_heap(arrays):
    """
    Merge k sorted arrays using a min-heap
    Time: O(N log k), Space: O(k)
    """
    min_heap = []

    # Step 1: Push first element of each array into the heap
    # Each heap element: (value, array_index, element_index)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    result = []

    # Step 2: Extract min and push the next element from the same array
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # If next element exists in the same array, push to heap
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_tuple = (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return result

#
# | Method                 | Data Type   | Time Complexity | Space Complexity                | Notes / Key Points                                                                     |
# | ---------------------- | ----------- | --------------- | ------------------------------- | -------------------------------------------------------------------------------------- |
# | Min-Heap Approach      | Linked List | O(N log k)      | O(k)                            | Push heads of all k lists into heap; extract min repeatedly; handles dynamic lists     |
# | Divide & Conquer Merge | Linked List | O(N log k)      | O(log k) recursion + O(1) extra | Merge pairs of lists repeatedly until one remains; uses merge-two helper               |
# | Min-Heap Approach      | Array       | O(N log k)      | O(k)                            | Heap stores (value, array_idx, element_idx); extract min and push next from same array |
