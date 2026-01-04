from collections import deque, defaultdict


class AhoCorasickDFA:
    """
    Aho–Corasick as a DFA (Deterministic Finite Automaton)

    States = trie nodes
    Transitions = character edges
    Failure links = DFA fallback transitions
    Output links = matched patterns
    """

    def __init__(self):
        self.next = []          # transitions: state -> {char: next_state}
        self.fail = []          # failure links
        self.output = []        # patterns ending at this state

        # Create root state (state 0)
        self.next.append({})
        self.fail.append(0)
        self.output.append([])

    # ==========================================================
    # STEP 1: BUILD TRIE (GOTO FUNCTION)
    # ==========================================================
    def add_word(self, word):
        """
        Insert a pattern into the trie
        """
        state = 0
        for ch in word:
            if ch not in self.next[state]:
                self.next[state][ch] = len(self.next)
                self.next.append({})
                self.fail.append(0)
                self.output.append([])
            state = self.next[state][ch]
        self.output[state].append(word)

    # ==========================================================
    # STEP 2: BUILD FAILURE LINKS (DFA FALLBACKS)
    # ==========================================================
    def build_failure_links(self):
        """
        Build failure links using BFS
        """
        queue = deque()

        # Initialize failure links for depth-1 states
        for ch, nxt in self.next[0].items():
            queue.append(nxt)
            self.fail[nxt] = 0

        # BFS over trie
        while queue:
            current = queue.popleft()

            for ch, nxt in self.next[current].items():
                queue.append(nxt)

                # Fallback from current state
                f = self.fail[current]

                # Follow failure links until match found or root reached
                while f > 0 and ch not in self.next[f]:
                    f = self.fail[f]

                # If transition exists, use it
                if ch in self.next[f]:
                    self.fail[nxt] = self.next[f][ch]
                else:
                    self.fail[nxt] = 0

                # Merge output patterns
                self.output[nxt].extend(self.output[self.fail[nxt]])

    # ==========================================================
    # STEP 3: SEARCH TEXT USING DFA
    # ==========================================================
    def search(self, text):
        """
        Search all patterns in the given text
        Returns list of (end_index, matched_pattern)
        """
        state = 0
        results = []

        for i, ch in enumerate(text):

            # Follow failure links on mismatch
            while state > 0 and ch not in self.next[state]:
                state = self.fail[state]

            # Move forward if possible
            if ch in self.next[state]:
                state = self.next[state][ch]

            # If this state has output, record matches
            for word in self.output[state]:
                results.append((i, word))

        return results
