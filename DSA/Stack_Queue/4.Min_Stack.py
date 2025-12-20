# Problem:
# Design a stack that supports push, pop, top, and getMin in O(1) time.
# Store only one stack instead of two.
#
# Idea:
# Each stack entry stores:
# (value, minimum up to this point)
#
# So every element keeps track of the minimum when it was pushed.
# This avoids duplicating entries like the two-stack approach.


class MinStack:
    def __init__(self):
        self.stack = []  # each element = (value, minSoFar)

    def push(self, x):
        if not self.stack:
            self.stack.append((x, x))
        else:
            currentMin = self.stack[-1][1]
            self.stack.append((x, min(x, currentMin)))

    def pop(self):
        if self.stack:
            self.stack.pop()

    def top(self):
        return self.stack[-1][0] if self.stack else None

    def getMin(self):
        return self.stack[-1][1] if self.stack else None

# MIN STACK – ENCODED SINGLE STACK VERSION
# Idea:
# - Maintain a variable minSoFar to track the minimum.
# - Store elements in stack normally, but if a new value x < minSoFar:
# Encode it as: 2*x - minSoFar
# Push encoded value.
# Update minSoFar = x
# - When popping:
# If popped value < minSoFar → it was an encoded value
# Retrieve previous min: prevMin = 2*minSoFar - poppedValue
# Update minSoFar = prevMin
# - If value >= minSoFar → normal pop.
# - getMin() → return minSoFar directly.


class MinStack_Optimal:
    def __init__(self):
        self.stack = []
        self.minSoFar = None

    def push(self, x):
        if not self.stack:
            self.stack.append(x)
            self.minSoFar = x
        elif x < self.minSoFar:
            encoded = 2*x - self.minSoFar
            self.stack.append(encoded)
            self.minSoFar = x
        else:
            self.stack.append(x)

    def pop(self):
        if not self.stack:
            return
        top = self.stack.pop()
        if top < self.minSoFar:
            self.minSoFar = 2*self.minSoFar - top

    def top(self):
        if not self.stack:
            return None
        top = self.stack[-1]
        if top < self.minSoFar:
            return self.minSoFar
        else:
            return top

    def getMin(self):
        return self.minSoFar
