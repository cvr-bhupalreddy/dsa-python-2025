# You are given:
#     - An array `books[]` where books[i] represents number of pages in the i-th book.
#     - An integer `students` representing the number of students.
#
# Constraints / Rules:
#     1. Each student must get **at least one book**.
#     2. Each student is assigned **continuous books** only.
#     3. Goal: Allocate all books to students such that the **maximum pages assigned to a student is minimized**.


# Allocate Minimum Pages — Detailed Core Idea (Copy-Ready)


def min_max_bruteforce(arr, k):
    """
    Brute-force solution:
    Try every possible maximum sum from max(arr) to sum(arr)
    """
    low = max(arr)
    high = sum(arr)

    for candidate in range(low, high + 1):
        if is_feasible(arr, k, candidate):
            return candidate  # first feasible value
    return high  # fallback (should not reach here)


def is_feasible(books, students, max_pages):
    count = 1
    curr_sum = 0
    for pages in books:
        if pages > max_pages:
            return False  # single book exceeds max_pages
        if curr_sum + pages > max_pages:
            count += 1
            curr_sum = pages
            if count > students:
                return False
        else:
            curr_sum += pages
    return True


def allocate_books(books, students):
    low, high = max(books), sum(books)
    result = high

    while low <= high:
        mid = (low + high) // 2
        if is_feasible(books, students, mid):
            result = mid  # feasible, try smaller
            high = mid - 1
        else:
            low = mid + 1  # not feasible, try larger
    return result
