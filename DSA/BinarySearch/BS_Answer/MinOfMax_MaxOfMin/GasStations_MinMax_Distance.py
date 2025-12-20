# You are given:
# - An array `stations[]` representing positions of gas stations along a highway (sorted in increasing order).
# - An integer `k` representing the number of additional gas stations you can build.
#
# Goal:
# - Place k additional gas stations such that the **maximum distance between adjacent gas stations** is minimized.
#
# Constraints / Rules:
# 1. You can place gas stations anywhere along the highway (not necessarily at integer positions).
# 2. Distance between stations is measured along the highway.
# 3. Find the minimum possible value of the **maximum distance** between adjacent stations after adding k stations.


# 1. Compute all initial gaps: gap[i] = stations[i+1] – stations[i]
# 2. For each gap create a record:
#     (current_segment_length = gap[i] / 1,
#     gap_index = i,
#     stations_added = 0)
# 3. Push all segments into a max-heap (largest segment on top).
#
# 4. Repeat K times:
#     - Extract the largest segment S
#     - Increase its station count: stations_added += 1
#     - Recompute new segment length:
#     new_len = gap[i] / (stations_added + 1)
#     - Push it back into heap
#
# 5. After K operations,
# the answer is max segment length in heap.

def minimize_max_distance_bruteforce(stations, K):
    n = len(stations)

    # Step 1: Compute initial gaps
    gaps = [stations[i+1] - stations[i] for i in range(n - 1)]

    # Step 2: Count how many new stations are inserted in each gap
    count = [0] * (n - 1)

    # Step 3: For each new gas station, pick the worst (largest effective gap)
    for _ in range(K):
        best_index = 0
        best_value = -1

        # Find gap with maximum effective length
        for i in range(n - 1):
            effective = gaps[i] / (count[i] + 1)
            if effective > best_value:
                best_value = effective
                best_index = i

        # Place a station in that gap
        count[best_index] += 1

    # Step 4: Result = maximum effective gap after all splits
    ans = 0
    for i in range(n - 1):
        effective = gaps[i] / (count[i] + 1)
        ans = max(ans, effective)

    return ans



import heapq


def brute_minmax_distance(stations, k):
    n = len(stations)
    gaps = []

    # Build initial gaps
    for i in range(n - 1):
        gap = stations[i + 1] - stations[i]
        # Heap stores negative length (max-heap behavior)
        gaps.append((-gap, i, 0))  # (neg_length, section_id, stations_added)

    heapq.heapify(gaps)

    # Repeat K times — always split the largest segment
    for _ in range(k):
        neg_len, idx, added = heapq.heappop(gaps)
        original_gap = stations[idx + 1] - stations[idx]

        added += 1  # we place one more station in this segment

        new_len = original_gap / (added + 1)

        heapq.heappush(gaps, (-new_len, idx, added))

    # The answer is the max segment length after splits
    final_len = -gaps[0][0]
    return final_len


def minimize_max_distance(stations, K):
    """
    stations: sorted list of gas station positions
    K       : number of new stations we can add

    Goal: minimize the maximum distance between adjacent stations.
    """

    # -------------------------------
    # STEP 1: Compute all current gaps
    # -------------------------------
    gaps = []
    for i in range(1, len(stations)):
        gaps.append(stations[i] - stations[i - 1])

    # -------------------------------------------------
    # Binary search on the answer (maximum allowed gap)
    # -------------------------------------------------
    low, high = 0, max(gaps)  # search space = [0, max existing gap]
    eps = 1e-6                 # precision threshold

    def required_stations(max_gap):
        """
        Feasibility check:
        Given allowed maximum gap = max_gap,
        how many stations must be added to ensure
        no interval > max_gap ?

        For each gap g:
            - if g <= max_gap → no stations needed
            - else we need floor(g / max_gap) extra stations

        ⚠ Exact division case (g % max_gap == 0):
            floor(g/max_gap) adds *one extra* station unnecessarily.
            But mathematically:
                number needed = ceil(g / max_gap) - 1

        But floor(g/max_gap) works **because**:
            ceil(g/x) - 1 == floor(g/x)
        EXCEPT for floating precision cases.

        So we use:
            needed = int(g / max_gap)
        But if division is exact (within EPS), decrease by 1.
        """
        total = 0
        for g in gaps:
            if g <= max_gap:
                continue

            # integer count of segments required
            add = int(g / max_gap)

            # ----------------------------------------
            # 🔥 IMPORTANT:
            # Handle exact division (g % max_gap == 0)
            # Example: g = 9, max_gap = 3
            # g/max_gap = 3, but needed = 2
            # ----------------------------------------
            if abs(add * max_gap - g) < 1e-12:
                add -= 1

            total += add

        return total

    # --------------------------------------
    # Binary Search for minimum max distance
    # --------------------------------------
    while high - low > eps:
        mid = (low + high) / 2

        # stations needed to make max gap ≤ mid
        needed = required_stations(mid)

        if needed > K:
            # mid is too small → need too many stations → increase mid
            low = mid
        else:
            # mid is feasible → try smaller maximum distance
            high = mid

    return high
