funcs = []

for i in range(3):
    def f():
        return i


    funcs.append(f)

print([f() for f in funcs])  # [2, 2, 2] ❌

# Closures capture VARIABLES, not VALUES
# i is evaluated when function is called


funcs = []

for i in range(3):
    def f(i=i):
        return i


    funcs.append(f)

print([f() for f in funcs])  # [0, 1, 2] ✅


#
# ➡️ Default args are evaluated once per function creation


# def counter():
#     count = 0
#     def inc():
#         count += 1   # ❌ UnboundLocalError
#     return inc


def counter():
    count = 0

    def inc():
        nonlocal count
        count += 1
        return count

    return inc


c = counter()
print(c())  # 1
print(c())  # 2


class Counter:
    def __init__(self):
        self.count = 0

    def inc(self):
        self.count += 1
        return self.count


# Closure → lightweight, private state
# Class → complex behavior, multiple methods


import sys

print(sys.getsizeof(10))  # ~28 bytes (CPython)
