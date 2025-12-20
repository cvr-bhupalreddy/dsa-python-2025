# You are given:
#  A list of non-overlapping intervals sorted by their start times
#  A new interval to insert
#
# Your task:
# 👉 Insert the new interval into the list so that the final list is still:
#
# Sorted
#  Non-overlapping
#  If inserting the new interval overlaps multiple intervals, you must merge them into one.
#
#
#
# 1. Initialize output list.
# 2. Traverse all intervals:
#     • If interval ends < new.start → add interval to output.
#     • If interval starts > new.end → break loop (no more overlap).
#     • Otherwise → merge interval with newInterval.
# 3. Append merged newInterval.
# 4. Append remaining intervals.
# 5. Return result.


# ✅ Definition of Overlap
# Two intervals [a, b] and [c, d] overlap if their ranges intersect:
#
# They overlap when:
#     c ≤ b   AND   a ≤ d
#
# Meaning:
# • The start of one interval is before the end of the other AND
# • The end of one interval is after the start of the other


# ✅ When Intervals DO NOT Overlap
#
# Two intervals do NOT overlap when one is completely before the other:
#
# [b < c]   → first ends before second starts
# or
# [d < a]   → second ends before first starts


def insert(intervals, newInterval):
    result = []
    i = 0
    n = len(intervals)

    new_start, new_end = newInterval

    # 1. Add all intervals ending before newInterval starts
    while i < n and intervals[i][1] < new_start:
        result.append(intervals[i])
        i += 1

    # 2. Merge all overlapping intervals
    while i < n and intervals[i][0] <= new_end:
        new_start = min(new_start, intervals[i][0])
        new_end = max(new_end, intervals[i][1])
        i += 1

    # Add merged interval
    result.append([new_start, new_end])

    # 3. Add remaining intervals
    while i < n:
        result.append(intervals[i])
        i += 1

    return result
