def is_balanced(s):
    stack = []
    match = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in "([{":
            stack.append(ch)
        else:
            if not stack or stack[-1] != match[ch]:
                return False
            stack.pop()

    return len(stack) == 0


def is_balanced_simple(s):
    count = 0
    for ch in s:
        if ch == '(':
            count += 1
        else:
            count -= 1
            if count < 0:  # more closing than opening
                return False
    return count == 0
