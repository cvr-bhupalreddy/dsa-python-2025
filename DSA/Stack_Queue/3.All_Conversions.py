# ============================================================
#  Expression Conversion & Evaluation Utilities
#  Includes:
#  1. Infix → Postfix
#  2. Infix → Prefix
#  3. Prefix → Infix
#  4. Prefix → Postfix
#  5. Postfix → Infix
#  6. Postfix → Prefix
#  7. Evaluate Postfix
#  8. Evaluate Prefix
# ============================================================

# -----------------------------
# Operator precedence
# -----------------------------
def precedence(op):
    if op in ["+", "-"]:
        return 1
    if op in ["*", "/"]:
        return 2
    if op == "^":
        return 3
    return 0

# ----------------------------------------------------------
# 1) INFIX → POSTFIX
# ----------------------------------------------------------
def infix_to_postfix(expr):
    stack = []
    output = []

    for ch in expr:
        if ch.isalnum():
            output.append(ch)

        elif ch == "(":
            stack.append(ch)

        elif ch == ")":
            while stack and stack[-1] != "(":
                output.append(stack.pop())
            stack.pop()

        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(ch):
                output.append(stack.pop())
            stack.append(ch)

    while stack:
        output.append(stack.pop())

    return "".join(output)

# ----------------------------------------------------------
# 2) INFIX → PREFIX (reverse + postfix)
# ----------------------------------------------------------
def infix_to_prefix(expr):
    expr = expr[::-1]
    expr = [")" if c == "(" else "(" if c == ")" else c for c in expr]
    postfix = infix_to_postfix(expr)
    return postfix[::-1]

# ----------------------------------------------------------
# 3) PREFIX → INFIX
# ----------------------------------------------------------
def prefix_to_infix(expr):
    stack = []
    for ch in reversed(expr):
        if ch.isalnum():
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append("(" + a + ch + b + ")")
    return stack[-1]

# ----------------------------------------------------------
# 4) PREFIX → POSTFIX
# ----------------------------------------------------------
def prefix_to_postfix(expr):
    stack = []
    for ch in reversed(expr):
        if ch.isalnum():
            stack.append(ch)
        else:
            a = stack.pop()
            b = stack.pop()
            stack.append(a + b + ch)
    return stack[-1]

# ----------------------------------------------------------
# 5) POSTFIX → INFIX
# ----------------------------------------------------------
def postfix_to_infix(expr):
    stack = []
    for ch in expr:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append("(" + a + ch + b + ")")
    return stack[-1]

# ----------------------------------------------------------
# 6) POSTFIX → PREFIX
# ----------------------------------------------------------
def postfix_to_prefix(expr):
    stack = []
    for ch in expr:
        if ch.isalnum():
            stack.append(ch)
        else:
            b = stack.pop()
            a = stack.pop()
            stack.append(ch + a + b)
    return stack[-1]

# ----------------------------------------------------------
# 7) POSTFIX EVALUATION
# ----------------------------------------------------------
def eval_postfix(expr):
    stack = []
    for ch in expr:
        if ch.isdigit():
            stack.append(int(ch))
        else:
            b = stack.pop()
            a = stack.pop()
            if ch == "+": stack.append(a + b)
            elif ch == "-": stack.append(a - b)
            elif ch == "*": stack.append(a * b)
            elif ch == "/": stack.append(a // b)
            elif ch == "^": stack.append(a ** b)
    return stack[-1]

# ----------------------------------------------------------
# 8) PREFIX EVALUATION
# ----------------------------------------------------------
def eval_prefix(expr):
    stack = []
    for ch in reversed(expr):
        if ch.isdigit():
            stack.append(int(ch))
        else:
            a = stack.pop()
            b = stack.pop()
            if ch == "+": stack.append(a + b)
            elif ch == "-": stack.append(a - b)
            elif ch == "*": stack.append(a * b)
            elif ch == "/": stack.append(a // b)
            elif ch == "^": stack.append(a ** b)
    return stack[-1]


# ============================================================
# Example calls
# ============================================================
if __name__ == "__main__":
    exp = "A+(B*C)"
    print("Infix → Postfix:", infix_to_postfix(exp))
    print("Infix → Prefix :", infix_to_prefix(exp))

    pre = "+A*BC"
    print("Prefix → Infix :", prefix_to_infix(pre))
    print("Prefix → Postfix:", prefix_to_postfix(pre))

    post = "ABC*+"
    print("Postfix → Infix :", postfix_to_infix(post))
    print("Postfix → Prefix:", postfix_to_prefix(post))
