def print_all_subsequences(arr):
    n = len(arr)

    def dfs(i, current):
        if i == n:
            print(current)
            return

        # include arr[i]
        current.append(arr[i])
        dfs(i + 1, current)

        # exclude arr[i]
        current.pop()
        dfs(i + 1, current)

    dfs(0, [])


def print_all_subsequences_backward(arr):
    n = len(arr)

    def dfs(i, current):
        if i < 0:
            print(current)
            return

        # include arr[i]
        current.append(arr[i])
        dfs(i - 1, current)

        # exclude arr[i]
        current.pop()
        dfs(i - 1, current)

    dfs(n - 1, [])


def subsequences_backward(arr, i, current):
    if i < 0:
        print(current)
        return

    # PICK arr[i]
    current.append(arr[i])
    subsequences_backward(arr, i - 1, current)

    # NOT PICK arr[i]
    current.pop()
    subsequences_backward(arr, i - 1, current)


# --- call the function ---
arr = [1, 2, 3]
subsequences_backward(arr, len(arr) - 1, [])


def subsequences_forward(arr, i, current):
    n = len(arr)
    if i == n:
        print(current)
        return

    # PICK arr[i]
    current.append(arr[i])
    subsequences_forward(arr, i + 1, current)

    # NOT PICK arr[i]
    current.pop()
    subsequences_forward(arr, i + 1, current)


# call
arr = [1, 2, 3]
subsequences_forward(arr, 0, [])


# Definition:
# f(i, subseq) = prints all subsequences using elements arr[0 : i]
#
# Backward Recurrence:
# f(i, subseq):
# if i < 0:
#     print subseq
#     return
#
# # choice 1: pick arr[i]
# append arr[i] to subseq
# f(i - 1, subseq)
#
# # choice 2: not pick arr[i]
# remove last element from subseq
# f(i - 1, subseq)
