# ✅ Problem: Koko Eating Bananas
#
# Statement (simplified):
#     Koko has piles of bananas.
#     piles[i] = number of bananas in the i-th pile.
#     Koko can eat K bananas per hour.
#     Each hour, she chooses one pile and eats up to K bananas from it.
#     If pile has less than K bananas, she finishes that pile in that hour.
#     Given H hours, find the minimum integer K such that Koko can eat all bananas in H hours.

# Key Points:
#     One pile per hour rule
#     hour += 1 for each pile she chooses
#
# Speed limit K
#
#     If pile size > K → she eats K bananas, remaining stays for next hour.
#     If pile size ≤ K → she finishes the pile in that hour.
#
# Why this matters for solution
#
# The hours_needed(K) formula works because it counts hours as:
#     hours_needed = sum(ceil(p / K) for p in piles)
#
# Each pile contributes ceil(p / K) hours independently.


# - Eating speed K is unknown.
# - Faster K → fewer hours needed.
# - Slower K → more hours needed.
# - Hours needed = sum(ceil(pile / K) for each pile)
#
# We want the minimum K such that total_hours <= H.
#
# Observation:
#     - Hours_needed(K) is a monotonic function:
#         increasing K → decreasing hours_needed
#     - Monotonicity → can apply Binary Search on K

import math


def min_eating_speed_bruteforce(piles, H):
    for K in range(1, max(piles) + 1):
        hours = sum(math.ceil(p / K) for p in piles)
        if hours <= H:
            return K


# ✅ 2️⃣ Better Approach (Binary Search on K — Optimal)
# Idea
#     Minimum possible K = 1
#     Maximum possible K = max(piles)
#     Use binary search in this range to find smallest K such that total hours ≤ H.
#
# Binary Search Pattern:
#
#     Search Space: integer K (eating speed)
#     Monotonic Property: hours_needed(K) is decreasing → feasible(K) is True/False
#     Pattern is called "Binary Search on Answer"
#
# Time Complexity: O(n * log(max(piles)))
# Space Complexity: O(1)


import math


def min_eating_speed(piles, H):
    low, high = 1, max(piles)

    def hours_needed(K):
        return sum(math.ceil(p / K) for p in piles)

    while low < high:
        mid = (low + high) // 2
        if hours_needed(mid) <= H:
            high = mid  # mid may be the answer, search left
        else:
            low = mid + 1  # mid too slow, search right

    return low
