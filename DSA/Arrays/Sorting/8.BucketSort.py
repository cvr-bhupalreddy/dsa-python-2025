# Bucket Sort distributes elements into buckets (intervals), sorts each bucket, and concatenates results.
#
# Steps:
# 1. Create n buckets for array range
# 2. Distribute elements into buckets based on value
# 3. Sort each bucket (can use any sorting method)
# 4. Concatenate all buckets to get sorted array
#
# Properties:
#     - Best when input is uniformly distributed
#     - Stable if stable sort used in each bucket


def bucket_sort(arr):
    if not arr:
        return

    n = len(arr)
    # Create buckets
    max_val = max(arr)
    min_val = min(arr)
    bucket_range = (max_val - min_val) / n + 1
    buckets = [[] for _ in range(n)]

    # Distribute elements into buckets
    for num in arr:
        index = int((num - min_val) // bucket_range)
        buckets[index].append(num)

    # Sort each bucket and concatenate
    arr.clear()
    for bucket in buckets:
        arr.extend(sorted(bucket))  # can use insertion sort for small buckets
