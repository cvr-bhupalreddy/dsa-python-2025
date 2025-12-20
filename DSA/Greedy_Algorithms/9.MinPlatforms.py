# 🚉 Minimum Number of Platforms – Problem Explanation
#
# You are given:
#     Arrival times of trains
#     Departure times of trains
#
# You must find:
# 👉 Minimum number of platforms required so that no train waits.
# A platform is needed whenever multiple trains overlap in time.


# Sort arrival times.
# Sort departure times.
#
# Use two pointers:
#     i → arrival index
#     j → departure index
#
# Track:
#     platforms_needed  -> current trains at station
#     max_platforms     -> answer
#
# If arrival[i] <= departure[j]:
#     A train arrives before the next train departs
#         → need a new platform
#         platforms_needed += 1
#         i += 1
# Else:
#     A train departs before the next arrival
#         → free a platform
#         platforms_needed -= 1
#         j += 1


def min_platforms(arr, dep):
    arr.sort()
    dep.sort()

    n = len(arr)
    i = j = 0
    platforms_needed = 0
    max_platforms = 0

    while i < n and j < n:
        if arr[i] <= dep[j]:   # train arrives before one departs
            platforms_needed += 1
            max_platforms = max(max_platforms, platforms_needed)
            i += 1
        else:                 # train departs before next arrival
            platforms_needed -= 1
            j += 1

    return max_platforms



