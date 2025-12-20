# ✅ Valid Parenthesis String — Problem Explanation
# Problem Statement
#
# Given a string s containing only the characters '(', ')', '{', '}', '[', ']', determine if the input string is valid.
#
# A string is valid if:
#     Every opening bracket has a corresponding closing bracket of the same type.
#     Brackets are closed in the correct order.
#     Every closing bracket matches the most recent unclosed opening bracket.


# 1. Initialize an empty stack.
# 2. Traverse the string from left to right:
#     a. If character is an opening bracket → push to stack
#     b. If character is a closing bracket:
#         i. If stack is empty → invalid
#         ii. Else pop top of stack and check if it matches the closing bracket
# 3. After traversal:
#     - If stack is empty → string is valid
#     - If stack not empty → string is invalid


def isValid(s):
    stack = []
    mapping = {')': '(', '}': '{', ']': '['}

    for char in s:
        if char in mapping.values():  # opening bracket
            stack.append(char)
        else:  # closing bracket
            if not stack or stack[-1] != mapping[char]:
                return False
            stack.pop()

    return len(stack) == 0


#
# ✅ Valid Parenthesis String with *
#     Problem Statement
#
# Given a string s containing:
#
# '(', ')', '*'
# Determine if the string is valid, where:
#     '*' can represent either:
#
#     '('
#
#     ')'
#
#     '' (empty string)
# Every opening bracket has a corresponding closing bracket in the correct order.
# Return True if valid, otherwise False.


# ✅ Key Points
#     Multiple * are allowed.
#     Each * counts only once, but you decide its interpretation for balancing.
#     Not the same as regex * (which means zero or more repetitions of the previous character).

def checkValidString(s):  # [for high valid range is 0 to 1]
    low = high = 0

    for char in s:
        if char == '(':
            low += 1
            high += 1
        elif char == ')':
            low = max(low - 1, 0)
            high -= 1
        else:  # char == '*'
            low = max(low - 1, 0)  # '*' as ')'
            high += 1  # '*' as '('

        if high < 0:  # too many ')'
            return False

    return low == 0
