#
# Core Idea:
# Precompute Z-array where Z[i] = length of substring starting at i that matches the prefix.
#
# Trick:
#     Concatenate pattern + '$' + text
#
# Steps:
# 1. Build Z-array in linear time
# 2. Wherever Z[i] == pattern length → match found
#
# When to use:
#     - Pattern matching
#     - Prefix-based problems
#     - Competitive programming
#
# Time Complexity:
#     - O(n + m)
#
# Space Complexity:
#     - O(n + m)


# ============================================================
# Z ALGORITHM
# ============================================================


# ============================================================
# Z-ALGORITHM — HIGH-LEVEL REUSE AND EXTENSION SUMMARY
# ============================================================

# Concept:
# ----------
# Z[i] = length of the longest substring starting at i
# that matches the prefix of the string.
#
# We maintain a Z-box [L, R] such that s[L..R] matches s[0..R-L].
# At each index i, we decide whether we can reuse previously computed Z values.
#
# ---
#
# CASE 1: i > R  (Outside Z-box)
# --------------------------------
#     - No previous information applies
#     - Must start fresh comparisons
#     - Action:
#         * Compare characters explicitly from i
#         * Build new Z-box [L, R] starting at i
#         * Compute Z[i] directly
#     - Safe: ✔
#
# ---
#
# CASE 2: i <= R  (Inside Z-box)
# --------------------------------
# Define:
# k = i - L  # mirror index in prefix
#
# Subcase 2A: Safe Copy
# -----------------------
# Condition:
# Z[k] < (R - i + 1)
# Meaning:
# - The match at k fully fits inside the Z-box
# - No chance of exceeding known matches
# Action:
#     * Copy Z[k] directly
#     * Z[i] = Z[k]
# Safe: ✔
#
# Subcase 2B: Careful Copy / Extension
# --------------------------------------
# Condition:
# Z[k] >= (R - i + 1)
# Meaning:
#     - Z[k] reaches or exceeds right boundary R
#     - Beyond R, characters are unknown
#     Action:
#         * Copy guaranteed part
#         * Then explicitly compare characters beyond R
#         * Update Z[i] = extended match length
#         * Update L = i and R = new right boundary
#     Safe: ⚠️ (must verify manually)
#
# ---
#
# Handling Z-values > pattern length
# -----------------------------------
# - When using pattern + "$" + text:
#     * "$" is a unique delimiter
#     * Matching cannot cross "$"
# - Therefore, Z[i] is naturally capped at len(pattern)
# - False positives are avoided
#
# ---
#
# Summary Table (Interview-ready)
# --------------------------------
# | Case       | Condition                   | Action                           | Safe? |
# |------------|-----------------------------|---------------------------------|-------|
# | 1          | i > R                       | Recompute from scratch           | ✔     |
# | 2A         | i ≤ R & Z[k] < R-i+1        | Copy Z[k]                        | ✔     |
# | 2B         | i ≤ R & Z[k] ≥ R-i+1        | Copy + extend via explicit match | ⚠️     |
#
# ---
#
# One-line Core Idea:
# --------------------
# Reuse Z-values **only when fully inside the current Z-box**; if they touch the boundary, extend manually.

def z_algorithm(s):
    """
    Computes the Z-array for string s

    Z[i] = length of the longest substring starting at i
           that matches the prefix of s

    Time Complexity: O(n)
    Space Complexity: O(n)
    """

    n = len(s)
    Z = [0] * n

    # [L, R] is the window where s[L:R+1] matches prefix s[0:R-L+1]
    L = 0
    R = 0

    # Start from index 1 (Z[0] is always 0)
    for i in range(1, n):

        # ------------------------------------------------
        # CASE 1: i is outside the current [L, R] window
        # ------------------------------------------------
        if i > R:
            L = R = i

            # Match characters explicitly
            while R < n and s[R] == s[R - L]:
                R += 1

            Z[i] = R - L
            R -= 1

        # ------------------------------------------------
        # CASE 2: i is inside the [L, R] window
        # ------------------------------------------------
        else:
            k = i - L  # Mirror index in prefix

            # If value does not exceed window
            if Z[k] < R - i + 1:
                Z[i] = Z[k]

            # Need to extend beyond R
            else:
                L = i
                while R < n and s[R] == s[R - L]:
                    R += 1

                Z[i] = R - L
                R -= 1

    return Z


# ============================================================
# PATTERN MATCHING USING Z ALGORITHM
# ============================================================

def z_pattern_match(text, pattern):
    """
    Returns all starting indices where pattern occurs in text

    Approach:
    - Create string: pattern + "$" + text
    - Compute Z-array
    - If Z[i] == len(pattern), pattern found
    """

    if not pattern or not text:
        return []

    combined = pattern + "$" + text
    Z = z_algorithm(combined)

    result = []
    p_len = len(pattern)

    for i in range(len(Z)):
        if Z[i] == p_len:
            # Convert combined index → text index
            result.append(i - p_len - 1)

    return result


# ============================================================
# DRIVER CODE
# ============================================================

if __name__ == "__main__":
    text = "abacaba"
    pattern = "aba"

    matches = z_pattern_match(text, pattern)

    print("Text    :", text)
    print("Pattern :", pattern)
    print("Matches at indices:", matches)
