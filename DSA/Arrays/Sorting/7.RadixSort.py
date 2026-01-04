# Radix Sort sorts numbers digit by digit from least significant digit (LSD) to most significant digit (MSD)
# (or vice versa), using a stable sort (like counting sort) at each digit.
#
# Steps:
# 1. Find the maximum number to know the number of digits.
# 2. Start from least significant digit to most significant digit:
# - Sort numbers according to current digit using stable sort
# 3. After the last digit, the array is fully sorted.
#
# Properties:
#     - Stable
#     - Non-comparative
#     - Best for integers or fixed length strings


def counting_sort_for_radix(arr, exp):
    """
    Stable counting sort according to digit at exp (10^exp)
    """
    n = len(arr)
    output = [0] * n
    count = [0] * 10  # digits 0-9

    # Count occurrences of each digit
    for i in range(n):
        index = (arr[i] // exp) % 10
        count[index] += 1

    # Convert count to positions
    for i in range(1, 10):
        count[i] += count[i - 1]

    # Build output array (stable)
    for i in range(n - 1, -1, -1):
        index = (arr[i] // exp) % 10
        output[count[index] - 1] = arr[i]
        count[index] -= 1

    # Copy back to original array
    for i in range(n):
        arr[i] = output[i]


def radix_sort(arr):
    """
    Radix Sort main function
    """
    if not arr:
        return

    max_num = max(arr)
    exp = 1  # Start with least significant digit
    while max_num // exp > 0:
        counting_sort_for_radix(arr, exp)
        exp *= 10
