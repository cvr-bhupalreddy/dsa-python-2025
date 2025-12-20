# Problem Statement
# You are given N meetings with their start and end times.
#
# Goal: Schedule the maximum number of meetings in one room such that:
#     No two meetings overlap.
#     Each meeting occupies the room for its full duration.


# Core Idea (Greedy Approach)
#
# Sort the meetings by their end times (earliest ending meeting first).
# Initialize last_end = 0 (end time of last scheduled meeting).
#
# Iterate through meetings:
#     If the meeting's start time ≥ last_end, schedule it.
#     Update last_end = meeting's end time.
#     Count the number of scheduled meetings → this is the maximum possible.
#
# Greedy choice works because choosing the meeting that finishes earliest leaves the most room for future meetings.

def max_meetings(start, end):
    """
    start: list of start times
    end: list of end times
    Returns the maximum number of non-overlapping meetings
    """
    n = len(start)
    # Step 1: Combine start and end times and sort by end time
    meetings = sorted(zip(start, end), key=lambda x: x[1])

    count = 0
    last_end = 0

    # Step 2: Schedule meetings greedily
    for s, e in meetings:
        if s >= last_end:
            count += 1
            last_end = e

    return count


def max_meetings_with_ids(start, end):
    n = len(start)

    # (start, end, id)
    meetings = [(start[i], end[i], i) for i in range(n)]

    # Sort by end time
    meetings.sort(key=lambda x: x[1])

    result_ids = []   # To store selected meeting IDs
    last_end = 0

    for s, e, mid in meetings:
        if s >= last_end:
            result_ids.append(mid)
            last_end = e

    return result_ids
