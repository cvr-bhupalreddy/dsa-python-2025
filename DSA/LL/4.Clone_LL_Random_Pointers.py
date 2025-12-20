# ⭐ Problem Definition
#
# You are given a singly linked list, where each node has:
#     next pointer → points to the next node in the list
#     random pointer → points to any node in the list (can be None)
# Task: Create a deep copy (clone) of this list — the cloned list should have exactly the same structure
# with its own nodes (no shared nodes with original list).


# Approach 1 — Using Hash Map (O(n) time, O(n) space)
# Core Idea
#
# Traverse original list, create a clone node for each original node, and store in a map:
#     original_node → cloned_node
#
# Traverse again and set:
#     cloned_node.next = map[original_node.next]
#     cloned_node.random = map[original_node.random]
#
# Return the head of cloned list.

class Node:
    def __init__(self, val):
        self.val = val
        self.next = None
        self.random = None


def clone_linked_list_hashmap(head):
    if not head:
        return None

    # Step 1: Create mapping from original to clone nodes
    node_map = {}
    curr = head
    while curr:
        node_map[curr] = Node(curr.val)
        curr = curr.next

    # Step 2: Assign next and random pointers
    curr = head
    while curr:
        node_map[curr].next = node_map.get(curr.next)
        node_map[curr].random = node_map.get(curr.random)
        curr = curr.next

    return node_map[head]

# Approach 2 — Optimal In-Place (O(n) time, O(1) extra space)
# Core Idea
#     Interleave cloned nodes with original nodes:
#     Assign random pointers for cloned nodes:
#     Separate cloned list from original:


def clone_linked_list_inplace(head):
    if not head:
        return None

    # Step 1: Interleave clone nodes
    curr = head
    while curr:
        new_node = Node(curr.val)
        new_node.next = curr.next
        curr.next = new_node
        curr = new_node.next

    # Step 2: Assign random pointers
    curr = head
    while curr:
        if curr.random:
            curr.next.random = curr.random.next
        curr = curr.next.next

    # Step 3: Separate original and cloned list
    curr = head
    clone_head = head.next
    while curr:
        clone = curr.next
        curr.next = clone.next
        if clone.next:
            clone.next = clone.next.next
        curr = curr.next

    return clone_head
