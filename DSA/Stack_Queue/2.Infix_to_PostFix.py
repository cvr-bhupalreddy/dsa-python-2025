# 1️⃣ Pushing Operators onto Stack (Infix → Postfix/Prefix)
#
# Rules for operator precedence:
#     1. If stack is empty → push current operator.
# 2. If current operator has higher precedence than top of stack → push current operator.
# 3. If current operator has lower or equal precedence than top of stack → pop operators from stack to output
#    until stack is empty or top has lower precedence → then push current operator.
# 4. Associativity:
# - Left-associative (+ - * /) → pop if equal precedence.
# - Right-associative (^) → do not pop if equal precedence.
# 5. '(' → always push onto stack.
# 6. ')' → pop all operators to output until '(' is found, then discard '('.
#
# Example: Infix "A + B * C ^ D"
# Stack/Output trace:
# Symbol | Stack      | Output   | Action
# A      | []         | A        | Operand → output
# +      | [+]        | A        | Stack empty → push +
# B      | [+]        | A B      | Operand → output
# *      | [+,*]      | A B      | * > + → push *
# C      | [+,*]      | A B C    | Operand → output
# ^      | [+,*,^]    | A B C    | ^ > * → push ^
# D      | [+,*,^]    | A B C D  | Operand → output
# End    | []         | A B C D ^ * + | Pop all operators → postfix
#
# ---
#
# 2️⃣ Operand Order in Postfix Evaluation
#
# - Scan left to right.
# - Operand → push onto stack.
# - Operator → pop **two operands**:
# - First popped = **right operand**
# - Second popped = **left operand**
# - Compute left op right, push result.
#
# Example: Postfix "2 3 4 * +"
# Stack operations:
# Push 2 → [2]
# Push 3 → [2,3]
# Push 4 → [2,3,4]
# Operator * → pop 4(right), 3(left) → 3*4=12 → push [2,12]
# Operator + → pop 12(right), 2(left) → 2+12=14 → push [14]
# Result = 14
#
# ---
#
# 3️⃣ Operand Order in Prefix Evaluation
#
# - Scan right to left.
# - Operand → push onto stack.
# - Operator → pop **two operands**:
# - First popped = **left operand**
# - Second popped = **right operand**
# - Compute left op right, push result.
#
# Example: Prefix "+ 2 * 3 4"
# Scan right→left: 4 3 * 2 +
# Push 4 → [4]
# Push 3 → [4,3]
# Operator * → pop 3(left), 4(right) → 3*4=12 → push [12]
# Push 2 → [12,2]
# Operator + → pop 2(left), 12(right) → 2+12=14 → push [14]
# Result = 14
#
# ---
#
# 4️⃣ Summary Table
#
# Conversion / Eval        | Stack Rule / Scan                         | Operand Order for Operator
#     ---------------------| ----------------------------              | --------------------------
# Infix → Postfix          | Push higher precedence, pop lower/equal   | Not applicable
# Infix → Prefix           | Reverse infix + use postfix logic         | Not applicable
# Postfix Evaluation       | Scan L→R, push operands, pop for operator | First pop = right, Second pop = left
# Prefix Evaluation        | Scan R→L, push operands, pop for operator | First pop = left, Second pop = right


# Helper functions
def precedence(op):
    if op == '^':
        return 3
    if op in ('*', '/'):
        return 2
    if op in ('+', '-'):
        return 1
    return 0


def is_operator(c):
    return c in "+-*/^"


# ---------------- Infix to Postfix ----------------
def infix_to_postfix(expr):
    stack = []
    output = []

    for c in expr:
        if c.isalnum():
            output.append(c)
        elif c == '(':
            stack.append(c)
        elif c == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()  # Remove '(' , we are discarding ')'
        else:  # operator
            while stack and precedence(stack[-1]) >= precedence(c):
                output.append(stack.pop())
            stack.append(c)

    while stack:  # after completing expression pop entire stack
        output.append(stack.pop())

    return ''.join(output)


# When converting infix to prefix, we reverse the string and swap '(' with ')'.
#     However, operator precedence and associativity rules DO NOT change.
#
# The precedence of ^, *, /, +, - remains exactly the same.
# Associativity rules also remain the same (^ is right associative, others are left associative).
#
# The only reason we reverse and swap parentheses is that reversing the string flips the direction of scanning.
# Parentheses must be swapped to preserve their meaning, but the operator rules stay the same.
#
# So: precedence does NOT change, associativity does NOT change. Only the scanning direction and parentheses are adjusted.


# ---------------- Infix to Prefix ----------------
def infix_to_prefix(expr):
    expr = expr[::-1]
    expr = ['(' if c == ')' else ')' if c == '(' else c for c in expr]
    # expr = ['(' if c == ')' else (')' if c == '(' else c) for c in expr]

    postfix = infix_to_postfix(expr)
    return postfix[::-1]


# But here you have nested ternary operators.
# Python evaluates it from left to right and uses this structure:
# A if cond1 else (B if cond2 else C)

# ---------------- Postfix Evaluation ----------------
def eval_postfix(expr):
    stack = []
    for c in expr:
        if c.isdigit():
            stack.append(int(c))
        else:
            b = stack.pop()
            a = stack.pop()
            if c == '+':
                stack.append(a + b)
            elif c == '-':
                stack.append(a - b)
            elif c == '*':
                stack.append(a * b)
            elif c == '/':
                stack.append(a // b)
            elif c == '^':
                stack.append(a ** b)
    return stack[0]


# ---------------- Prefix Evaluation ----------------
def eval_prefix(expr):
    stack = []
    for c in expr[::-1]:
        if c.isdigit():
            stack.append(int(c))
        else:
            a = stack.pop()
            b = stack.pop()
            if c == '+':
                stack.append(a + b)
            elif c == '-':
                stack.append(a - b)
            elif c == '*':
                stack.append(a * b)
            elif c == '/':
                stack.append(a // b)
            elif c == '^':
                stack.append(a ** b)
    return stack[0]


# ---------------- Example ----------------
if __name__ == "__main__":
    infix = "3+(2*4)^2-5"
    postfix = infix_to_postfix(infix)
    prefix = infix_to_prefix(infix)

    print("Infix:", infix)
    print("Postfix:", postfix)
    print("Prefix:", prefix)
    print("Postfix Eval:", eval_postfix(postfix))
    print("Prefix Eval:", eval_prefix(prefix))
