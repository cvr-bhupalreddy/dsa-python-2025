# ✅ Problem Definition
#
# You are given a linked list where:
#     Each node has a next pointer (horizontal)
#     Each node may have a child pointer (vertical) pointing to another sorted linked list.
#     All vertical lists are sorted.
#     Flatten the list so that all nodes appear in a single sorted linked list.
#
# The flattened list should use the next pointer only (or some variations keep bottom pointer).

#  This is Converting Skip List to Sorted Linked List


# Method 1: Merge Like Merge Sort
#     1. Start from the head of the main list.
#     2. Recursively flatten the 'next' list.
#     3. Merge current list (using 'child' or 'bottom') with flattened 'next' list.
#     4. Return merged sorted list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.child = None  # or bottom


# Helper function to merge two sorted linked lists
def merge(a, b):
    if not a:
        return b
    if not b:
        return a

    if a.val < b.val:
        result = a
        result.child = merge(a.child, b)
    else:
        result = b
        result.child = merge(a, b.child)
    result.next = None  # flattening removes horizontal links
    return result


# Recursive flatten function
def flatten_recursive(head):
    if not head or not head.next:
        return head

    # Flatten next list
    head.next = flatten_recursive(head.next)

    # Merge current list with flattened next list
    head = merge(head, head.next)

    return head


# Iterative merge of two sorted lists
def merge_iterative(a, b):
    dummy = Node(0)
    tail = dummy

    while a and b:
        if a.val < b.val:
            tail.child = a
            a = a.child
        else:
            tail.child = b
            b = b.child
        tail = tail.child

    # Attach remaining nodes
    if a:
        tail.child = a
    if b:
        tail.child = b

    return dummy.child


# Iterative flatten function
def flatten_iterative(head):
    if not head:
        return None

    curr = head

    while curr and curr.next:
        # Merge curr list with next list
        curr.child = merge_iterative(curr, curr.next)
        curr.next = curr.child.next  # move to next horizontal node
        curr = curr.child

    return head


# Usage:
# flattened_head = flatten_recursive(head)


#
# Method 2: Using Min Heap
#     1. Push all top-level nodes into a min-heap.
#     2. Pop the smallest node, push its child if exists.
#     3. Continue until heap is empty.
#     4. Build the sorted flattened list as you pop nodes.


# | **Method**                            | **Time Complexity**   | **Space Complexity**
# | **Recursive Merge (like merge sort)** | O(N × M)              | O(1) extra (O(N) recursion stack)
# | **Min Heap / Priority Queue**         | O(T × log N)          | O(N) for heap
#
# N = number of top-level nodes, M = average child list length
# T = total nodes, N = top-level nodes


import heapq


def flatten_heap(head):
    if not head:
        return None

    min_heap = []

    # Push all top-level nodes into heap
    curr = head
    while curr:
        heapq.heappush(min_heap, curr)
        curr = curr.next

    dummy = Node(0)
    tail = dummy

    while min_heap:
        node = heapq.heappop(min_heap)
        tail.child = node  # using child as next in flattened list
        tail = tail.child

        # If node has child list, push head of that list
        if node.child:
            heapq.heappush(min_heap, node.child)

        node.next = None
        node.child = None

    return dummy.child

# Usage:
# flattened_head = flatten_heap(head)
