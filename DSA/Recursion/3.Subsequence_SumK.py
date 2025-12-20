def print_subsequences_sum_k(arr, k, index=0, curr=None, curr_sum=0):
    if curr is None:
        curr = []

    # base case
    if index == len(arr):
        if curr_sum == k:
            print(curr)
        return

    # pick element
    curr.append(arr[index])
    print_subsequences_sum_k(arr, k, index + 1, curr, curr_sum + arr[index])

    # not pick element
    curr.pop()
    print_subsequences_sum_k(arr, k, index + 1, curr, curr_sum)


def print_subsequences_sum_k_backward(arr, k, index=None, curr=None, curr_sum=0):
    if curr is None:
        curr = []
    if index is None:
        index = len(arr) - 1

    # base case
    if index < 0:
        if curr_sum == k:
            print(curr[::-1])  # reverse because we append from back
        return

    # pick arr[index]
    curr.append(arr[index])
    print_subsequences_sum_k_backward(arr, k, index - 1, curr, curr_sum + arr[index])

    # not pick arr[index]
    curr.pop()
    print_subsequences_sum_k_backward(arr, k, index - 1, curr, curr_sum)


def print_any_subsequence_sum_k(arr, k, index=0, curr=None, curr_sum=0):
    if curr is None:
        curr = []

    # base case
    if index == len(arr):
        if curr_sum == k:
            print(curr)
            return True  # found one
        return False

    # pick element
    curr.append(arr[index])
    if print_any_subsequence_sum_k_1(arr, k, index + 1, curr, curr_sum + arr[index]):
        return True  # stop recursion if found
    curr.pop()

    # not pick element
    if print_any_subsequence_sum_k_1(arr, k, index + 1, curr, curr_sum):
        return True

    return False  # no subsequence found in this path


def print_any_subsequence_sum_k_1(arr, k):
    n = len(arr)

    def helper(index, curr, curr_sum):
        # base case
        if index == n:
            if curr_sum == k:
                print(curr)
                return True  # stop recursion once one subsequence is found
            return False

        # pick element
        curr.append(arr[index])
        if helper(index + 1, curr, curr_sum + arr[index]):
            return True
        curr.pop()  # backtrack

        # not pick element
        if helper(index + 1, curr, curr_sum):
            return True

        return False

    helper(0, [], 0)


def count_subseq_sum_forward(arr, K):
    n = len(arr)

    def solve(i, k):
        if k == 0:
            return 1
        if i == n:
            return 0

        if arr[i] <= k:
            return solve(i + 1, k - arr[i]) + solve(i + 1, k)
        else:
            return solve(i + 1, k)

    return solve(0, K)


def count_subseq_sum_backward(arr, K):
    def solve(i, k):
        if k == 0:
            return 1
        if i < 0:
            return 0

        if arr[i] <= k:
            return solve(i - 1, k - arr[i]) + solve(i - 1, k)
        else:
            return solve(i - 1, k)

    return solve(len(arr) - 1, K)


def count_subsequences_sum_k_backward(arr, k):
    def helper(index, curr_sum):
        # base case
        if index < 0:
            return 1 if curr_sum == k else 0

        # pick element
        pick = helper(index - 1, curr_sum + arr[index])

        # not pick element
        not_pick = helper(index - 1, curr_sum)

        return pick + not_pick

    return helper(len(arr) - 1, 0)


def count_subsequences_sum_k_forward(arr, k):
    def helper(index, curr_sum):
        # base case
        if index == len(arr):
            return 1 if curr_sum == k else 0

        # pick element
        pick = helper(index + 1, curr_sum + arr[index])

        # not pick element
        not_pick = helper(index + 1, curr_sum)

        return pick + not_pick

    return helper(0, 0)
