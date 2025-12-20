# ✅ Meeting Rooms II — Sweep Line / Greedy Strategy
# Problem Statement
#
# You are given a list of meeting time intervals represented as pairs:
# intervals = [[start1, end1], [start2, end2], ...]
#
# Each interval represents a meeting's start and end time.
#
# Goal:
# Determine the minimum number of meeting rooms required to host all meetings without overlap.


# Core Idea (Sweep Line / Greedy)
#
# Separate start and end times
#
# starts = sorted([interval[0] for interval in intervals])
# ends = sorted([interval[1] for interval in intervals])
#
# Use two pointers to simulate time flow
#     i for start times
#     j for end times
# Iterate over all meetings
# If next meeting starts before the earliest ending meeting → need a new room
# Else → a meeting ended → reuse room
#
# Keep track of current rooms and update max rooms needed


def minMeetingRooms(intervals):
    if not intervals:
        return 0

    # Step 1: Separate start and end times
    starts = sorted([i[0] for i in intervals])
    ends = sorted([i[1] for i in intervals])

    # Step 2: Initialize pointers and counters
    s_ptr = 0  # start pointer
    e_ptr = 0  # end pointer
    rooms = 0
    max_rooms = 0

    # Step 3: Sweep line
    while s_ptr < len(intervals):
        if starts[s_ptr] < ends[e_ptr]:
            # New meeting starts before earliest ends → need new room
            rooms += 1
            max_rooms = max(max_rooms, rooms)
            s_ptr += 1
        else:
            # Meeting ended → free room
            rooms -= 1
            e_ptr += 1

    return max_rooms
