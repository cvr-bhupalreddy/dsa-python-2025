# Core Idea:
#
# Binary search on the smaller array to partition both arrays.
# Partition ensures:
#     Left partitions contain half of total elements
#     Max of left ≤ Min of right for both arrays
#
#
# Steps:
#     Let arr1 be smaller.
#     Partition arr1 at i, arr2 at j = (m + n + 1)//2 - i.
#     Check if arr1[i-1] ≤ arr2[j] and arr2[j-1] ≤ arr1[i].
#     If true → correct partition found.
#     Else adjust i using binary search.
#
# Median:
# If total odd: max(arr1[i-1], arr2[j-1])
# If total even: (max(arr1[i-1], arr2[j-1]) + min(arr1[i], arr2[j])) / 2
# Calculate l1, l2, r1, and r2: Generally,
# l1 = arr1[mid1-1]
# l2 = arr2[mid2-1]
# r1 = arr1[mid1]
# r2 = arr2[mid2]

class Solution:
    # Function to find the median of two sorted arrays.
    def median(self, arr1, arr2):
        # Size of two given arrays
        n1, n2 = len(arr1), len(arr2)

        """ Ensure arr1 is not larger than 
        arr2 to simplify implementation"""
        if n1 > n2:
            return self.median(arr2, arr1)

        n = n1 + n2
        # Length of left half
        left = (n1 + n2 + 1) // 2

        # Apply binary search
        low, high = 0, n1
        while low <= high:
            # Calculate mid index for arr1
            mid1 = (low + high) // 2

            # Calculate mid index for arr2
            mid2 = left - mid1

            # Calculate l1, l2, r1, and r2
            l1 = arr1[mid1 - 1] if mid1 > 0 else float('-inf')
            r1 = arr1[mid1] if mid1 < n1 else float('inf')
            l2 = arr2[mid2 - 1] if mid2 > 0 else float('-inf')
            r2 = arr2[mid2] if mid2 < n2 else float('inf')

            if l1 <= r2 and l2 <= r1:
                # If condition for finding median is satisfied
                if n % 2 == 1:
                    return max(l1, l2)
                else:
                    return (max(l1, l2) + min(r1, r2)) / 2.0
            elif l1 > r2:
                # Eliminate the right half of arr1
                high = mid1 - 1
            else:
                # Eliminate the left half of arr1
                low = mid1 + 1
        # Dummy statement
        return 0


if __name__ == "__main__":
    arr1 = [1, 4, 7, 10, 12]
    arr2 = [2, 3, 6, 15]

    # Create an instance of the Solution class
    sol = Solution()

    # Print the median of the two sorted arrays
    print(f"The median of two sorted arrays is {sol.median(arr1, arr2)}")


def median_optimal(arr1, arr2):
    if len(arr1) > len(arr2):
        arr1, arr2 = arr2, arr1  # arr1 is smaller
    m, n = len(arr1), len(arr2)
    low, high = 0, m

    while low <= high:
        mid1 = (low + high) // 2
        mid2 = (m + n + 1) // 2 - mid1

        max_left1 = float('-inf') if mid1 == 0 else arr1[mid1 - 1]
        min_right1 = float('inf') if mid1 == m else arr1[mid1]
        max_left2 = float('-inf') if mid2 == 0 else arr2[mid2 - 1]
        min_right2 = float('inf') if mid2 == n else arr2[mid2]

        if max_left1 <= min_right2 and max_left2 <= min_right1:
            if (m + n) % 2 == 0:
                return (max(max_left1, max_left2) + min(min_right1, min_right2)) / 2
            else:
                return max(max_left1, max_left2)
        elif max_left1 > min_right2:
            high = mid1 - 1
        else:
            low = mid1 + 1


def median_merge_extra_space(arr1, arr2):
    merged = []
    i = j = 0
    m, n = len(arr1), len(arr2)

    # Merge arrays
    while i < m and j < n:
        if arr1[i] < arr2[j]:
            merged.append(arr1[i])
            i += 1
        else:
            merged.append(arr2[j])
            j += 1

    while i < m:
        merged.append(arr1[i])
        i += 1

    while j < n:
        merged.append(arr2[j])
        j += 1

    total_len = m + n
    mid = total_len // 2
    if total_len % 2 == 0:
        return (merged[mid - 1] + merged[mid]) / 2
    else:
        return merged[mid]


# Example
arr1 = [1, 3, 5]
arr2 = [2, 4, 6]
print(median_merge_extra_space(arr1, arr2))  # Output: 3.5


def median_merge_no_extra_space(arr1, arr2):
    m, n = len(arr1), len(arr2)
    total_len = m + n
    mid1 = mid2 = 0
    i = j = count = 0
    prev = curr = 0

    while count <= total_len // 2:
        prev = curr
        if i < m and (j >= n or arr1[i] < arr2[j]):
            curr = arr1[i]
            i += 1
        else:
            curr = arr2[j]
            j += 1
        count += 1

    if total_len % 2 == 0:
        return (prev + curr) / 2
    else:
        return curr


# Example
print(median_merge_no_extra_space(arr1, arr2))  # Output: 3.5
