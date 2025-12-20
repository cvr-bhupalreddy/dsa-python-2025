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
