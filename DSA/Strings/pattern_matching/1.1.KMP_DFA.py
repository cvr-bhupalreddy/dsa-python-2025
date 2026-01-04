# 🔹 Summary Table
# | Algorithm                | DFA Based      | Use Case              |
# | ------------------------ | -------------- | --------------------- |
# | KMP                      | ✅ Conceptually | Single pattern        |
# | Finite Automaton Matcher | ✅ Pure DFA     | Fixed alphabet        |
# | Aho–Corasick             | ✅              | Multiple patterns     |
# | Regex DFA                | ✅              | Complex pattern rules |
# | Rabin–Karp               | ❌              | Hash-based            |
# | Z Algorithm              | ❌              | Prefix matching       |


def build_kmp_dfa(pattern):
    """
    Build DFA (Deterministic Finite Automaton) for KMP pattern matching

    DFA[state][char] -> next_state

    State = how many characters of the pattern have been matched so far
    States range from 0 .. M
    """
    M = len(pattern)

    # Alphabet of characters we care about
    # (can be extended to full ASCII if needed)
    alphabet = set(pattern)

    # ==========================================================
    # STEP 1: COMPUTE LPS ARRAY
    # ==========================================================
    # lps[i] = length of longest proper prefix of pattern[0..i]
    #          which is also a suffix of pattern[0..i]
    #
    # LPS defines the fallback transitions of the DFA
    # ==========================================================

    lps = [0] * M
    j = 0  # length of previous longest prefix suffix

    for i in range(1, M):
        # Fallback until we find a matching prefix or reach 0
        while j > 0 and pattern[i] != pattern[j]:
            j = lps[j - 1]

        # If characters match, extend prefix
        if pattern[i] == pattern[j]:
            j += 1

        lps[i] = j

    # ==========================================================
    # STEP 2: BUILD DFA TRANSITION TABLE
    # ==========================================================
    # dfa[state][char] = next state
    #
    # Total states = M + 1
    # State M = accepting state (full pattern matched)
    # ==========================================================

    dfa = [{} for _ in range(M + 1)]

    for state in range(M + 1):
        for ch in alphabet:

            # -------------------------------
            # CASE 1: MATCH TRANSITION
            # -------------------------------
            # If we are in state 'state'
            # and next char matches pattern[state]
            # → move forward
            if state < M and ch == pattern[state]:
                dfa[state][ch] = state + 1

            # -------------------------------
            # CASE 2: MISMATCH TRANSITION
            # -------------------------------
            else:
                if state == 0:
                    # No prefix matched, stay in state 0
                    dfa[state][ch] = 0
                else:
                    # Fallback using LPS
                    # Equivalent to: while mismatch → j = lps[j-1]
                    dfa[state][ch] = dfa[lps[state - 1]][ch]

    return dfa, lps


def kmp_match(text, pattern):
    """
    Match pattern in text using DFA-based KMP
    Returns list of starting indices
    """

    # Build DFA and LPS
    dfa, _ = build_kmp_dfa(pattern)

    state = 0        # current DFA state (prefix matched)
    M = len(pattern)
    result = []

    # ==========================================================
    # PROCESS TEXT USING DFA
    # ==========================================================
    for i, ch in enumerate(text):

        # DFA transition:
        # Given current state and input character,
        # move deterministically to next state
        state = dfa[state].get(ch, 0)

        # If we reached accepting state → match found
        if state == M:
            # Match ends at i
            # Starting index = i - M + 1
            result.append(i - M + 1)

    return result
