import bisect


def lis_binary_search(arr):
    sub = []  # stores the smallest possible tail for subsequences of each length

    for num in arr:
        # Find location where num can be placed (first element >= num)
        idx = bisect.bisect_left(sub, num)

        # If num is greater than all elements, append it → extend LIS
        if idx == len(sub):
            sub.append(num)
        else:
            # Replace existing element to maintain smallest tail
            sub[idx] = num

    return len(sub)


def lengthOfLIS(nums):
    if not nums:
        return 0

    tails = []   # stores smallest tail of all LIS of each length

    def lower_bound(arr, target):
        """Return first index where arr[i] >= target."""
        l, r = 0, len(arr) - 1
        ans = len(arr)
        while l <= r:
            mid = (l + r) // 2
            if arr[mid] >= target:
                ans = mid
                r = mid - 1
            else:
                l = mid + 1
        return ans

    for x in nums:
        pos = lower_bound(tails, x)
        if pos == len(tails):
            tails.append(x)
        else:
            tails[pos] = x

    return len(tails)
