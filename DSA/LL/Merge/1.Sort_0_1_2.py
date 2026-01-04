class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

def sort_012_brute(head):
    """
    Brute-force approach: extract values, sort, rebuild
    """
    if not head:
        return None

    # Step 1: Extract values into list
    arr = []
    curr = head
    while curr:
        arr.append(curr.val)
        curr = curr.next

    # Step 2: Sort the array
    arr.sort()  # or use count of 0,1,2

    # Step 3: Rebuild linked list
    curr = head
    for val in arr:
        curr.val = val
        curr = curr.next

    return head


def sort_012_count(head):
    """
    Count-based approach: two passes, no extra nodes
    """
    if not head:
        return None

    count = [0, 0, 0]  # count[0]=zeros, count[1]=ones, count[2]=twos

    # First pass: count
    curr = head
    while curr:
        count[curr.val] += 1
        curr = curr.next

    # Second pass: overwrite values
    curr = head
    for i in range(3):
        for _ in range(count[i]):
            curr.val = i
            curr = curr.next

    return head


def sort_012_optimal(head):
    """
    Optimal one-pass approach using three lists
    """
    if not head or not head.next:
        return head

    # Dummy heads for 0s, 1s, and 2s
    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)

    zero = zeroD  # pointers to build lists
    one = oneD
    two = twoD

    curr = head
    while curr:
        if curr.val == 0:
            zero.next = curr
            zero = zero.next
        elif curr.val == 1:
            one.next = curr
            one = one.next
        else:
            two.next = curr
            two = two.next
        curr = curr.next

    # Connect three lists
    zero.next = oneD.next if oneD.next else twoD.next
    one.next = twoD.next
    two.next = None  # end of final list

    # Return head of merged list
    return zeroD.next
