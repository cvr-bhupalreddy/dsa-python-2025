# | Method                             | Time Complexity   | Space Complexity |
# | ---------------------------------- | ----------------- | ---------------- |
# | Convert to integer → Multiply → LL | O(M × N) (digits) | O(M + N + P)     |

# Limitation:
#
# For very large numbers, integer storage can be huge
# → use the optimal method with O(M×N) time and O(M+N) space which avoids big integers.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# -------------------------
# Helper: Convert linked list to integer
# -------------------------
def linked_list_to_number(head):
    num = 0
    while head:
        num = num * 10 + head.val
        head = head.next
    return num


# -------------------------
# Helper: Convert number to linked list
# -------------------------
def number_to_linked_list(num):
    if num == 0:
        return Node(0)

    digits = []
    while num > 0:
        digits.append(num % 10)
        num //= 10

    # reverse to MSB first
    digits = digits[::-1]
    head = Node(digits[0])
    curr = head
    for d in digits[1:]:
        curr.next = Node(d)
        curr = curr.next
    return head


# -------------------------
# Multiply two linked lists
# -------------------------
def multiply_linked_lists(l1, l2):
    num1 = linked_list_to_number(l1)
    num2 = linked_list_to_number(l2)
    product = num1 * num2
    return number_to_linked_list(product)


#
# ✅ Core Idea (Optimal, O(M×N) time, O(M+N) space):
# Reverse both linked lists to make LSB first (makes multiplication easier).
# Multiply each digit of l2 with all digits of l1 → create partial product linked list.
# Shift partial product according to digit position (like adding zeros in manual multiplication).
# Add partial product to cumulative result using linked list addition.
# Reverse the final result to MSB first.
# Remove leading zeros if any.
# This works for very large numbers, no integer conversion, and is efficient for linked lists.


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


# -------------------------
# Helper: Reverse linked list
# -------------------------
def reverse(head):
    prev, curr = None, head
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    return prev


# -------------------------
# Helper: Add two linked lists (reverse order)
# -------------------------
def add_lists(l1, l2):
    carry = 0
    head = None
    curr = None
    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0
        total = val1 + val2 + carry
        carry = total // 10
        node = Node(total % 10)
        if not head:
            head = node
            curr = node
        else:
            curr.next = node
            curr = curr.next
        if l1: l1 = l1.next
        if l2: l2 = l2.next
    return head


# -------------------------
# Multiply two linked lists
# -------------------------
def multiply_linked_lists_1(l1, l2):
    # Reverse lists to make LSB first
    l1 = reverse(l1)
    l2 = reverse(l2)

    result = Node(0)  # Initial result = 0
    l2_ptr = l2
    zeros = 0  # to shift for each digit in l2

    while l2_ptr:
        carry = 0
        temp_head = None
        temp_curr = None

        # Add leading zeros for current digit
        for _ in range(zeros):
            node = Node(0)
            if not temp_head:
                temp_head = temp_curr = node
            else:
                temp_curr.next = node
                temp_curr = temp_curr.next

        l1_ptr = l1
        while l1_ptr:
            mul = l1_ptr.val * l2_ptr.val + carry
            carry = mul // 10
            node = Node(mul % 10)
            if not temp_head:
                temp_head = temp_curr = node
            else:
                temp_curr.next = node
                temp_curr = temp_curr.next
            l1_ptr = l1_ptr.next

        if carry:
            temp_curr.next = Node(carry)

        # Add this partial product to result
        result = add_lists(result, temp_head)
        zeros += 1
        l2_ptr = l2_ptr.next

    # Reverse final result to MSB first
    result = reverse(result)

    # Remove leading zeros
    while result and result.val == 0 and result.next:
        result = result.next

    return result
