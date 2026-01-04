
# 1. Normalize k:
#     - k = k % len(s)  # handle k > n
#
# 2. For right rotation:
#     - Last k characters move to the front
#     - Remaining characters shift right
#
# 3. For left rotation:
#     - First k characters move to the end
#     - Remaining characters shift left
#
# 4. Python string slicing makes this easy and efficient

def rotate_string_right(s: str, k: int) -> str:
    n = len(s)
    if n == 0:
        return s
    k = k % n  # normalize k

    # Last k characters + first n-k characters
    return s[-k:] + s[:-k]


# ✅ Example
s = "abcdef"
k = 2
print(rotate_string_right(s, k))  # Output: "efabcd"


def rotate_string_left(s: str, k: int) -> str:
    n = len(s)
    if n == 0:
        return s
    k = k % n  # normalize k

    # First k characters to the end
    return s[k:] + s[:k]


# ✅ Example
s = "abcdef"
k = 2
print(rotate_string_left(s, k))  # Output: "cdefab"


# 1. Reverse entire string
# 2. Reverse first k characters
# 3. Reverse remaining n-k characters

def rotate_string_right_reverse(s: str, k: int) -> str:
    s = list(s)
    n = len(s)
    k %= n

    def reverse(arr, l, r):
        while l < r:
            arr[l], arr[r] = arr[r], arr[l]
            l += 1
            r -= 1

    reverse(s, 0, n- 1)
    reverse(s, 0, k - 1)
    reverse(s, k, n - 1)

    return "".join(s)


s = "abcdef"
k = 2
print(rotate_string_right_reverse(s, k))  # Output: "efabcd"
