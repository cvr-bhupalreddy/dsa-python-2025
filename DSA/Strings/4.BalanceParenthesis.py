# 1. Check string length:
#     - If odd → impossible to balance → return -1
# 2. Initialize an empty stack (or counter for optimal approach)
# 3. Traverse the string:
#     - If char is '(' → push to stack
#     - If char is ')':
#         - If stack top is '(' → pop (balanced pair)
#         - Else → push ')' (unbalanced closing)
#
# 4. After traversal:
#     - Stack contains unbalanced brackets only
#     - Count:
#         - open_count = number of '('
#         - close_count = number of ')'
# 5. Minimum reversals formula:
# reversals = ceil(open_count / 2) + ceil(close_count / 2)
# # Or equivalently: (open_count + 1)//2 + (close_count + 1)//2
# 6. Return reversals


def minimumReversals(s: str) -> int:
    n = len(s)

    # If odd length, impossible to balance
    if n % 2 != 0:
        return -1

    stack = []

    # Step 1: Remove balanced pairs
    for bracket in s:
        if bracket == '(':
            stack.append(bracket)
        else:  # bracket == ')'
            if stack and stack[-1] == '(':
                stack.pop()  # balanced pair found
            else:
                stack.append(')')  # unbalanced closing

    # Step 2: Count remaining unbalanced brackets
    open_count = close_count = 0
    while stack:
        if stack.pop() == '(':
            open_count += 1
        else:
            close_count += 1

    # Step 3: Minimum reversals formula
    reversals = (open_count + 1) // 2 + (close_count + 1) // 2
    return reversals

# ✅ Example
s = ")(())("
print(minimumReversals(s))  # Output: 2
