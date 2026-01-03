# What is the Word Ladder Problem?
#
# You are given:
#     beginWord
#     endWord
#     wordList
#
# Rule
#     You can transform one word into another by changing exactly one character,
#     and every intermediate word must exist in wordList.


# Word Ladder I (Shortest Length)
#     Return the length of the shortest transformation sequence from beginWord to endWord.

# beginWord = "hit"
# endWord   = "cog"
# wordList  = ["hot","dot","dog","lot","log","cog"]
#
# hit → hot → dot → dog → cog
# Answer = 5


# 🔹 Word Ladder II (All Shortest Paths)
# Return all shortest transformation sequences.
#
# Output
# [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
# ]


# 🔹 Core Graph Idea
# Key Observations
#
# Each word is a node
# Edge exists if two words differ by exactly one letter
# All edges have equal weight (1)
# ➡ This is a Shortest Path in Unweighted Graph problem.
#
# 👉 Therefore: BFS is the correct algorithm.


# 🔹 Better Solution (Standard BFS)
# Idea
#
# Start BFS from beginWord
# At each step, change one character (a → z)
# If new word exists in dictionary → push to queue
# Key Optimization
# Remove word from dictionary as soon as it is visited.
#
# O(N × L × 26)


# 🔹 Optimal Solution (Pattern-Based BFS)
# Preprocessing Trick
#
# Convert words into generic patterns:
#
# hot → *ot, h*t, ho*
#
# Build mapping
#     *ot → hot, dot, lot
#     h*t → hot


# BFS becomes fast neighbor lookup.
# Complexity
# Preprocessing: O(N × L)
# BFS: O(N × L)
# Total: O(N × L)


# queue = (word, level)
# while queue:
#     word, level = pop
#     if word == endWord: return level
#     for each valid 1-letter transformation:
#         if exists in dictionary:
#             push with level+1
#                 remove from dictionary


from collections import deque, defaultdict


def ladderLength(beginWord, endWord, wordList):
    wordSet = set(wordList)

    if endWord not in wordSet:
        return 0

    queue = deque()
    queue.append((beginWord, 1))  # (current_word, level)

    # remove beginWord if present to avoid revisiting
    if beginWord in wordSet:
        wordSet.remove(beginWord)

    while queue:
        word, level = queue.popleft()

        for i in range(len(word)):
            original_char = word[i]

            for ch in 'abcdefghijklmnopqrstuvwxyz':
                if ch == original_char:
                    continue

                new_word = word[:i] + ch + word[i + 1:]

                if new_word == endWord:
                    return level + 1

                if new_word in wordSet:
                    queue.append((new_word, level + 1))
                    wordSet.remove(new_word)  # mark visited

    return 0


def ladderLength_optimal(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return 0

    L = len(beginWord)

    # ---------------------------------
    # STEP 1: Build pattern → words map
    # ---------------------------------
    pattern_map = defaultdict(list)

    for word in wordSet:
        for i in range(L):
            pattern = word[:i] + '*' + word[i + 1:]
            pattern_map[pattern].append(word)

    # ---------------------------------
    # STEP 2: BFS
    # ---------------------------------
    queue = deque()
    queue.append((beginWord, 1))

    # remove beginWord if present
    if beginWord in wordSet:
        wordSet.remove(beginWord)

    while queue:
        word, level = queue.popleft()

        for i in range(L):
            pattern = word[:i] + '*' + word[i + 1:]

            for next_word in pattern_map[pattern]:
                if next_word == endWord:
                    return level + 1

                if next_word in wordSet:
                    queue.append((next_word, level + 1))
                    wordSet.remove(next_word)  # mark visited

            # critical optimization: avoid reusing same pattern
            pattern_map[pattern] = []

    return 0
