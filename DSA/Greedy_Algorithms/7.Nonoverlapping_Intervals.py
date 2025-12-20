# this problem you can solve using same N meeting rooms , ans =( N - max Meeting)

# 🎯 Problem: Non-Overlapping Intervals
#
# You are given an array of intervals [[s1,e1], [s2,e2], ...].
# Return the minimum number of intervals you must remove so that the rest become non-overlapping.
#
# This is also known as:
#     “Erase Overlap Intervals”.


# 1. Sort intervals by their ending time (smallest end first).
# 2. Keep track of the end of the last selected interval.
# 3. Traverse all intervals:
#     - If current interval does NOT overlap → select it and update end.
#     - If it overlaps → remove it (increase removal count).
# 4. The greedy choice of earliest finishing interval
# always leaves maximum space for future intervals.


# ✅ Definition of Overlap
#
# Two intervals [s1, e1] and [s2, e2] overlap
# IF and ONLY IF their ranges intersect in time.
#
# Formally:
#     They overlap when s2 < e1 AND s1 < e2.
#
# For sorted-by-end greedy solution:
#     When processing intervals sorted by end time:
#     Overlap occurs if current.start < last_selected.end


def eraseOverlapIntervals(intervals):
    if not intervals:
        return 0

    # Step 1: Sort intervals by their end time
    intervals.sort(key=lambda x: x[1])

    # Step 2: Greedily select non-overlapping intervals
    count_non_overlap = 1
    last_end = intervals[0][1]

    for start, end in intervals[1:]:
        # If no overlap, we choose this interval
        if start >= last_end:
            count_non_overlap += 1
            last_end = end

    # Total intervals - number of non-overlapping intervals
    return len(intervals) - count_non_overlap
