# 🔹 Comparison Table
#
# | Version        | Goal               | Algorithm       | Key Trick       |
# | -------------- | ------------------ | --------------- | --------------- |
# | Word Ladder I  | Shortest length    | BFS             | Remove visited  |
# | Word Ladder II | All shortest paths | BFS + DFS       | Parent tracking |
# | Optimal        | Speed              | Pattern mapping | `*` wildcard    |


# 🔹 Word Ladder II
# Goal
# Return ALL shortest transformation sequences from beginWord to endWord.
#
# Rules
# Change one character at a time
# Each intermediate word must exist in wordList
# All returned paths must be shortest length

#
# begin = "hit"
# end   = "cog"
#
# Output:
# [
#     ["hit","hot","dot","dog","cog"],
#     ["hit","hot","lot","log","cog"]
# ]


# 🟡 BETTER SOLUTION — BFS + Parent Tracking
# Core Idea
#     BFS → find shortest distance
#     Track parents (multiple allowed)
#     DFS backtracking → build paths
#
# Key Insight
# A word can have multiple parents at the same shortest level.


# ⚠️ Critical Rule (VERY IMPORTANT)
#
# ❌ Remove words immediately → breaks multiple paths
# ✅ Remove words level by level


from collections import defaultdict, deque


def findLadders(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    parents = defaultdict(list)
    level = {beginWord}
    found = False

    while level and not found:
        next_level = set()
        for word in level:
            wordSet.discard(word)

        for word in level:
            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    new_word = word[:i] + ch + word[i + 1:]
                    if new_word in wordSet:
                        parents[new_word].append(word)
                        if new_word == endWord:
                            found = True
                        next_level.add(new_word)

        level = next_level

    # DFS to build paths
    res = []

    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        for p in parents[word]:
            dfs(p, path + [p])

    if found:
        dfs(endWord, [endWord])

    return res


# 🟢 OPTIMAL SOLUTION — Pattern BFS + Parent Graph
# Optimization Over Better
# Instead of generating 26 letters each time, use wildcard patterns.
#
# Example
# hot → *ot, h*t, ho*

def findLadders_optimal_bfs_pattern(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    L = len(beginWord)
    pattern_map = defaultdict(list)

    for word in wordSet:
        for i in range(L):
            pattern_map[word[:i] + '*' + word[i + 1:]].append(word)

    parents = defaultdict(list)
    queue = deque([beginWord])
    visited = set([beginWord])
    found = False

    while queue and not found:
        level_visited = set()
        for _ in range(len(queue)):
            word = queue.popleft()

            for i in range(L):
                pattern = word[:i] + '*' + word[i + 1:]
                for next_word in pattern_map[pattern]:
                    if next_word not in visited:
                        if next_word == endWord:
                            found = True
                        parents[next_word].append(word)
                        if next_word not in level_visited:
                            level_visited.add(next_word)
                            queue.append(next_word)
        visited |= level_visited

    # DFS backtracking
    res = []

    def dfs(word, path):
        if word == beginWord:
            res.append(path[::-1])
            return
        for p in parents[word]:
            dfs(p, path + [p])

    if found:
        dfs(endWord, [endWord])

    return res

# You do:
# BFS where each queue entry contains the entire path
# Once you reach endWord, all paths found at that level are shortest
# Stop BFS after that level
#
# This is level-order BFS on paths


def findLadders_bfs_only(beginWord, endWord, wordList):
    wordSet = set(wordList)
    if endWord not in wordSet:
        return []

    res = []
    queue = deque([[beginWord]])
    found = False

    while queue and not found:
        level_size = len(queue)
        used_words = set()

        for _ in range(level_size):
            path = queue.popleft()
            word = path[-1]

            for i in range(len(word)):
                for ch in 'abcdefghijklmnopqrstuvwxyz':
                    if ch == word[i]:
                        continue

                    new_word = word[:i] + ch + word[i+1:]

                    if new_word in wordSet:
                        new_path = path + [new_word]

                        if new_word == endWord:
                            res.append(new_path)
                            found = True
                        else:
                            queue.append(new_path)

                        used_words.add(new_word)

        # remove words AFTER finishing this BFS level
        wordSet -= used_words

    return res

# Comparison With Optimal Approach
# | Method                   | Simplicity | Memory | Speed    |
# | ------------------------ | ---------- | ------ | -------- |
# | BFS with full paths      | ⭐⭐⭐⭐ | ❌ High | ❌ Slower |
# | BFS + parent graph + DFS | ⭐⭐      | ✅ Low  | ✅ Fast   |
