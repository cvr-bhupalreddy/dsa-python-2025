# Algorithm (for any k)
#
#     Normalize k to avoid extra rotations: k = k % n.
#     Reverse the entire array.
#     Reverse the first k elements.
#     Reverse the remaining n-k elements.
#
# Core Idea:
#     Rotating right by k is equivalent to moving the last k elements to the front.
#     Using reversals avoids extra space and works in-place.


def rotate_array(arr, k):
    n = len(arr)
    if n == 0:
        return arr

    k = k % n  # handle k > n

    # Helper to reverse subarray
    def reverse(subarr, start, end):
        while start < end:
            subarr[start], subarr[end] = subarr[end], subarr[start]
            start += 1
            end -= 1

    # Step 1: Reverse entire array
    reverse(arr, 0, n - 1)
    # Step 2: Reverse first k elements
    reverse(arr, 0, k - 1)
    # Step 3: Reverse remaining elements
    reverse(arr, k, n - 1)

    return arr


# Example usage:
arr = [1, 2, 3, 4, 5]
k = 1
rotated = rotate_array(arr, k)
print(rotated)  # Output: [5,1,2,3,4]
