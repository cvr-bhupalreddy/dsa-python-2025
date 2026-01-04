# | Approach    | Description                      | Time             | Space |
# | ----------- | -------------------------------- | ---------------- | ----- |
# | **Brute**   | Double loop over A and B         | **O(n₁·n₂)**     | O(1)  |
# | **Better**  | Binary search in B for each A[i] | **O(n₁ log n₂)** | O(1)  |
# | **Optimal** | Two pointers, both sorted        | **O(n₁ + n₂)**   | O(1)  |

# ✅ What Is an Inversion?
#
# Given an array A,
# an inversion is a pair of indices (i, j) such that:
# i < j   AND   A[i] > A[j]
# Inversions measure how far the array is from being sorted.

# The count inversions problem is:
#
# Given an array, identify all pairs (i, j) such that i < j and A[i] > A[j].
#
# So yes, the goal is to count how many elements are “out of order” in the original array.
#
# You are not just comparing sorted halves,
# you are using merge-sort to efficiently track these original-index relationships.
#
# During the merge step, when a right-half element is smaller than a left-half element,
# it forms inversions with all remaining elements in the left-half — because in the original array,
# those left-half elements were before this right-half element.


# Why i < j is implicit
#
# i < j means left element comes before right element in original array.
# Since left = arr[l..m] and right = arr[m+1..r], all elements in left are before elements in right.
# So whenever arr[i] > arr[j], all remaining elements from i to m form inversions with arr[j].
# Hence inv_count += (m - i + 1) accounts for all pairs (i', j) where i' ≥ i.
# You never explicitly write i<j, because the indices in left and right already satisfy that condition.

def upper_bound(arr, x):
    low, high = 0, len(arr)

    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= x:
            low = mid + 1
        else:
            high = mid
    return low


def count_inversions_better(A, B):
    count = 0
    for x in A:
        pos = upper_bound(B, x)  # elements < x
        count += pos
    return count


def count_inversions_optimal(A, B):
    i = j = 0
    count = 0
    n1, n2 = len(A), len(B)

    while i < n1 and j < n2:
        if B[j] < A[i]:
            j += 1
        else:
            count += j
            i += 1

    # If A still has elements left, all B elements seen so far are valid
    while i < n1:
        count += j
        i += 1

    return count


class Solution:

    # Merge function to count
    # inversions and merge sorted halves
    def merge(self, arr, low, mid, high):

        # Temporary array for merging
        temp = []

        # Starting indices of left and right halves
        left = low
        right = mid + 1

        # Count variable to count the pairs
        cnt = 0

        # Merge sorted halves into temp array
        while left <= mid and right <= high:
            if arr[left] <= arr[right]:

                temp.append(arr[left])
                left += 1

            else:
                temp.append(arr[right])

                # Count inversions
                cnt += (mid - left + 1)

                right += 1

        # Copy remaining elements of left half
        while left <= mid:
            temp.append(arr[left])
            left += 1

        # Copy remaining elements of right half
        while right <= high:
            temp.append(arr[right])
            right += 1

        # Copy elements from temp
        # array back to original array
        for i in range(low, high + 1):
            arr[i] = temp[i - low]

        # Return the count of inversions
        return cnt

    # Merge sort function to recursively sort and count inversions
    def mergeSort(self, arr, low, high):
        cnt = 0
        if low < high:
            mid = low + (high - low) // 2

            # Sort left half
            cnt += self.mergeSort(arr, low, mid)

            # Sort right half
            cnt += self.mergeSort(arr, mid + 1, high)

            # Merge and count inversions
            cnt += self.merge(arr, low, mid, high)
        return cnt

    # Function to find number of inversions in an array
    def numberOfInversions(self, nums):

        # Size of the array
        n = len(nums)

        # Count the number of pairs
        return self.mergeSort(nums, 0, n - 1)


if __name__ == "__main__":
    nums = [5, 4, 3, 2, 1]

    # Create an instance of Solution class
    sol = Solution()

    result = sol.numberOfInversions(nums)

    # Print the number of inversions found
    print(f"The number of inversions are: {result}")


# Given an array arr, an inversion is a pair (i, j) such that:
# i < j and arr[i] > arr[j]
#     Task: Count total number of inversions in the array.


# Brute Force:
# - Check every pair (i, j) → O(n^2)
#
# Optimal Approach (Merge Sort):
# 1. During merge step of merge sort, whenever an element from right subarray is placed before left subarray element,
# it forms inversions with all remaining elements in left subarray.
# 2. Count these inversions while merging.
# 3. Recur for left and right halves, sum inversions.
#
# Time Complexity: O(n log n)
# Space Complexity: O(n) (temporary arrays for merge)
