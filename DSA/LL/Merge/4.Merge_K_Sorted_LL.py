import heapq


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    # required for heapq to compare Node objects
    def __lt__(self, other):
        return self.val < other.val


def merge_k_lists(lists):
    min_heap = []

    # Step 1: Push head of each list into heap
    for node in lists:
        if node:
            heapq.heappush(min_heap, node)

    dummy = Node(0)
    curr = dummy

    # Step 2: Repeatedly extract min
    while min_heap:
        node = heapq.heappop(min_heap)
        curr.next = node
        curr = curr.next

        if node.next:  # this step is taking linked list to next elements , in arrays we need to do it explicitly
            heapq.heappush(min_heap, node.next)

    return dummy.next


def merge_two(l1, l2):
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

    curr.next = l1 if l1 else l2
    return dummy.next


def merge_k_lists_divide_and_conquer(lists):
    if not lists:
        return None
    if len(lists) == 1:
        return lists[0]

    while len(lists) > 1:
        merged = []

        for i in range(0, len(lists), 2):
            l1 = lists[i]
            l2 = lists[i + 1] if i + 1 < len(lists) else None
            merged.append(merge_two(l1, l2))

        lists = merged

    return lists[0]


# for arrays managing explicitly


def merge_k_arrays_heap(arrays):
    min_heap = []

    # Step 1: Push (value, array_index, element_index)
    for i, arr in enumerate(arrays):
        if arr:
            heapq.heappush(min_heap, (arr[0], i, 0))

    result = []

    # Step 2: Extract min and push next from the same array
    while min_heap:
        val, arr_idx, elem_idx = heapq.heappop(min_heap)
        result.append(val)

        # If next element exists in same array, push to heap
        if elem_idx + 1 < len(arrays[arr_idx]):
            next_tuple = (arrays[arr_idx][elem_idx + 1], arr_idx, elem_idx + 1)
            heapq.heappush(min_heap, next_tuple)

    return result
