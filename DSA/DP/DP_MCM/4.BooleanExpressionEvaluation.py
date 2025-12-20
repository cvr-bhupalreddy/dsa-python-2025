# CORE IDEA:
#
# We treat each operator position k as the point where the final parenthesis split happens.
# This means the operator at index k is applied last for the substring s[i..j].
#
# So for every interval (i, j):
#     We try all k where s[k] is an operator (i < k < j, step by 2).
#     This splits the expression into:
#     Left  part: s[i .. k-1]
#     Right part: s[k+1 .. j]
#
# For each side, we need:
# - number of ways it becomes True
# - number of ways it becomes False
#
# Let:
# LT = ways left is True
# LF = ways left is False
# RT = ways right is True
# RF = ways right is False
#
# We combine these based on the operator:
#
# If operator is '&':
#   True  = LT * RT
#   False = LF*RT + LT*RF + LF*RF
#
# If operator is '|':
#      True  = LT*RT + LT*RF + LF*RT
#      False = LF * RF
#
# If operator is '^':
#   True  = LT*RF + LF*RT
#   False = LT*RT + LF*RF
#
# Total ways for s[i..j] is sum of ways over all possible k.
#
# This is identical to Matrix Chain Multiplication:
# Choose a partition k → solve left → solve right → combine.
# Only the combination logic differs.

# When we choose an operator k as the last operator in the subexpression (i..j),
# we split the expression into two independent parts: (i..k-1) and (k+1..j).
#
# Every possible True/False result of the left part can be combined with
#     every possible True/False result of the right part to form a valid
# parenthesize.
#
# Therefore, if the left side can produce True in LT ways and False in LF ways,
# and the right side can produce True in RT ways and False in RF ways, then the
# total number of ways to form the whole expression is computed by multiplying
# these counts:
# LT*RT, LT*RF, LF*RT, LF*RF
# depending on the operator.
#
# Multiplication is used because each left-way is compatible with each
#     right-way, producing unique full expressions.



class BooleanExpressionDP:

    # ---------------------------------------------------------
    # 1) MEMOIZATION
    # ---------------------------------------------------------
    def count_ways_memo(self, s: str) -> int:
        n = len(s)
        dp = [[[-1 for _ in range(2)] for _ in range(n)] for __ in range(n)]

        def solve(i, j, wantTrue):
            if i == j:
                if wantTrue:
                    return 1 if s[i] == 'T' else 0
                else:
                    return 1 if s[i] == 'F' else 0

            if dp[i][j][1 if wantTrue else 0] != -1:
                return dp[i][j][1 if wantTrue else 0]

            ways = 0

            for k in range(i+1, j, 2):  # k is operator
                LT = solve(i, k-1, True)
                LF = solve(i, k-1, False)
                RT = solve(k+1, j, True)
                RF = solve(k+1, j, False)

                op = s[k]

                if wantTrue:
                    if op == '&':
                        ways += LT * RT
                    elif op == '|':
                        ways += LT*RT + LT*RF + LF*RT
                    elif op == '^':
                        ways += LT*RF + LF*RT
                else:
                    if op == '&':
                        ways += LF*RT + LT*RF + LF*RF
                    elif op == '|':
                        ways += LF * RF
                    elif op == '^':
                        ways += LT*RT + LF*RF

            dp[i][j][1 if wantTrue else 0] = ways
            return ways

        return solve(0, n-1, True)

    # ---------------------------------------------------------
    # 2) TABULATION (GENERAL i → j NESTED LOOPS)
    # ---------------------------------------------------------
    def count_ways_tabulation(self, s: str) -> int:
        n = len(s)
        dpT = [[0]*n for _ in range(n)]
        dpF = [[0]*n for _ in range(n)]

        # Base: single symbol
        for i in range(n):
            if s[i] == 'T':
                dpT[i][i] = 1
            elif s[i] == 'F':
                dpF[i][i] = 1

        # General: i from n-1 to 0, j from i+2 to n-1
        for i in range(n-1, -1, -1):
            for j in range(i+2, n, 2):

                Tways, Fways = 0, 0

                for k in range(i+1, j, 2):
                    LT = dpT[i][k-1]
                    LF = dpF[i][k-1]
                    RT = dpT[k+1][j]
                    RF = dpF[k+1][j]

                    op = s[k]

                    if op == '&':
                        Tways += LT * RT
                        Fways += LF*RT + LT*RF + LF*RF

                    elif op == '|':
                        Tways += LT*RT + LT*RF + LF*RT
                        Fways += LF * RF

                    elif op == '^':
                        Tways += LT*RF + LF*RT
                        Fways += LT*RT + LF*RF

                dpT[i][j] = Tways
                dpF[i][j] = Fways

        return dpT[0][n-1]

    # ---------------------------------------------------------
    # 3) TABULATION USING DIAGONAL METHOD (LENGTHS)
    # ---------------------------------------------------------
    def count_ways_tab_length(self, s: str) -> int:
        n = len(s)
        dpT = [[0]*n for _ in range(n)]
        dpF = [[0]*n for _ in range(n)]

        # Base case
        for i in range(n):
            if s[i] == 'T':
                dpT[i][i] = 1
            elif s[i] == 'F':
                dpF[i][i] = 1

        # Only odd lengths are valid (symbols + operators)
        for length in range(3, n+1, 2):  # 3,5,7,...
            for i in range(0, n-length+1):
                j = i + length - 1

                Tways, Fways = 0, 0

                for k in range(i+1, j, 2):
                    LT = dpT[i][k-1]
                    LF = dpF[i][k-1]
                    RT = dpT[k+1][j]
                    RF = dpF[k+1][j]

                    op = s[k]

                    if op == '&':
                        Tways += LT * RT
                        Fways += LF*RT + LT*RF + LF*RF

                    elif op == '|':
                        Tways += LT*RT + LT*RF + LF*RT
                        Fways += LF * RF

                    elif op == '^':
                        Tways += LT*RF + LF*RT
                        Fways += LT*RT + LF*RF

                dpT[i][j] = Tways
                dpF[i][j] = Fways

        return dpT[0][n-1]
