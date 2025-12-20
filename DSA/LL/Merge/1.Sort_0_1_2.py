class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


def segregate_012_bruteforce(head):
    count = [0, 0, 0]  # count[0], count[1], count[2]
    curr = head
    while curr:
        count[curr.val] += 1
        curr = curr.next

    curr = head
    for i in range(3):
        while count[i] > 0:
            curr.val = i
            curr = curr.next
            count[i] -= 1
    return head


def segregate_012_better(head):
    zeroD = Node(0)
    oneD = Node(0)
    twoD = Node(0)
    zero = zeroD
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

    # Connect lists
    zero.next = oneD.next if oneD.next else twoD.next
    one.next = twoD.next
    two.next = None

    return zeroD.next
