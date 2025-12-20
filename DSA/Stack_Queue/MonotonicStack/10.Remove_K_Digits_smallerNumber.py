# Algorithm (Steps)
#
# Initialize empty stack.
#
# Iterate over digits in num:
#     While stack is not empty, k > 0, and stack[-1] > digit:
#         Pop stack and decrement k.
#     Push digit onto stack.
#     If k > 0, remove last k digits from stack.
#     Convert stack to string and strip leading zeros.
#
# Return "0" if string is empty.


def removeKdigits(num, k):
    stack = []

    for digit in num:
        while stack and k > 0 and stack[-1] > digit:
            stack.pop()
            k -= 1
        stack.append(digit)

    # If k > 0, remove from end
    while k > 0:
        stack.pop()
        k -= 1

    # Build final number and remove leading zeros
    result = ''.join(stack).lstrip('0')

    return result if result else "0"


