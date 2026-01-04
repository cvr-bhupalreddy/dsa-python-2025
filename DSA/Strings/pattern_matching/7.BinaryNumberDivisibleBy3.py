def is_binary_divisible_by_3(binary: str) -> bool:
    """
    DFA to check if a binary string represents
    a number divisible by 3.

    States represent remainder mod 3.
    Accepting state: remainder == 0
    """

    # DFA states = remainder mod 3
    # state 0 → divisible by 3
    # state 1 → remainder 1
    # state 2 → remainder 2

    # Transition table:
    # new_remainder = (old_remainder * 2 + bit) % 3
    transition = {
        0: {'0': 0, '1': 1},
        1: {'0': 2, '1': 0},
        2: {'0': 1, '1': 2}
    }

    state = 0  # start state (value = 0)

    for bit in binary:
        if bit not in ('0', '1'):
            return False  # invalid binary string
        state = transition[state][bit]

    return state == 0
