# Cutting Stick Problem (DP) – Definition
#
# You are given:
#
# A stick of length L
#
# A set of positions along the stick where you must make cuts
# (e.g., {x1, x2, x3, …})
#
# Every time you cut the stick, the cost of that cut is equal to the current length of the stick being cut.
#
# Your task is:
#
# ✅ Find the minimum total cost to perform all required cuts.


# We solve the Minimum Cost to Cut a Stick problem using interval DP.
#
# Let the original stick length be n and the cuts array contain C cut positions.
# We first sort the cuts and then extend the array by inserting:
# cuts[0] = 0
# cuts[C+1] = n
# Thus cuts has size C+2 and valid cut positions are cuts[1..C].
#
# We define solve(i, j) as the minimum cost to perform all cuts from i to j (inclusive),
# where the stick boundaries of this segment are cuts[i-1] on the left and cuts[j+1] on the right.
#
# Base Case:
#   If i > j:
#       return 0
#   (No cuts to perform in this interval.)
#
# Recurrence:
# For every possible first cut k in the interval [i..j],
# total cost = cost of cutting this whole segment + cost of left part + cost of right part.
#
# cost = (cuts[j+1] - cuts[i-1]) + solve(i, k-1) + solve(k+1, j)
#
# solve(i, j) = minimum over all k from i to j of the above cost.
#
# The initial call is:
# sort(cuts)
# extend cuts as [0] + cuts + [n]
# return solve(1, C)
#
# The term (cuts[j+1] - cuts[i-1]) represents the length of the current stick segment,
# because its left boundary is cuts[i-1] and its right boundary is cuts[j+1].
# Every cut inside this interval costs the length of this whole segment.


class MinCostCutStick:

    # -------------------------------------------------------
    # 1. MEMOIZATION (TOP-DOWN)
    # -------------------------------------------------------
    def min_cost_memo(self, n, cuts):
        # Prepare cuts with boundaries
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        C = len(cuts) - 2  # number of real cuts

        # dp[i][j] stores result for solve(i,j)
        dp = [[-1] * (C + 2) for _ in range(C + 2)]

        def solve(i, j):
            # Base case
            if i > j:
                return 0

            if dp[i][j] != -1:
                return dp[i][j]

            best = float('inf')

            # try each possible first cut k
            for k in range(i, j + 1):
                cost = (cuts[j + 1] - cuts[i - 1]) \
                       + solve(i, k - 1) \
                       + solve(k + 1, j)

                best = min(best, cost)

            dp[i][j] = best
            return best

        return solve(1, C)

    # -------------------------------------------------------
    # 2. TABULATION (BOTTOM-UP INTERVAL DP)
    # -------------------------------------------------------
    def min_cost_tab(self, n, cuts):
        # Prepare cuts with boundaries
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        C = len(cuts) - 2  # number of actual cuts

        # dp[i][j] = solve(i,j)
        dp = [[0] * (C + 2) for _ in range(C + 2)]

        # length = size of interval (number of cuts)
        for length in range(1, C + 1):
            for i in range(1, C - length + 2):
                j = i + length - 1

                best = float('inf')

                for k in range(i, j + 1):
                    cost = (cuts[j + 1] - cuts[i - 1]) \
                           + dp[i][k - 1] \
                           + dp[k + 1][j]

                    best = min(best, cost)

                dp[i][j] = best

        return dp[1][C]


class MinCostCutStick_1:

    def min_cost_tab_no_length(self, n, cuts):
        # Prepare cuts with boundaries
        cuts = sorted(cuts)
        cuts = [0] + cuts + [n]
        C = len(cuts) - 2

        dp = [[0] * (C + 2) for _ in range(C + 2)]

        # i goes from C down to 1   (smaller intervals → bigger)
        for i in range(C, 0, -1):
            # j goes from i up to C
            for j in range(i, C + 1):

                if i > j:
                    dp[i][j] = 0
                    continue

                best = float('inf')

                # Try all possible first cut k in interval [i..j]
                for k in range(i, j + 1):
                    cost = (cuts[j + 1] - cuts[i - 1]) \
                           + dp[i][k - 1] \
                           + dp[k + 1][j]

                    best = min(best, cost)

                dp[i][j] = best

        return dp[1][C]
