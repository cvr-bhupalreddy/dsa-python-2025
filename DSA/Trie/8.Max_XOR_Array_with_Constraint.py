# Maximum XOR With an Element From Array (with constraint ≤ m)
#
# Problem:
#
# For each query [xi, mi]:
# Choose a number num from nums
# Such that num ≤ mi
# Maximize xi XOR num
#
# If no such num exists → return -1


# Key Observations ✅
#     XOR is maximized when bits differ
#     Higher bits matter more
#     Query has a constraint (num ≤ mi) → dynamic eligible set
#     Binary Trie can maximize XOR if only valid numbers are inserted


# Offline Queries + Binary Trie
#     Instead of answering queries one by one,
#     sort everything and process incrementally


# 1. Sort nums in ascending order.
# 2. Convert queries into (mi, xi, original_index).
# 3. Sort queries by mi.
# 4. Maintain a pointer on nums.
# 5. Insert nums into a binary trie ONLY while nums[i] ≤ mi.
# 6. For each query:
#     - If trie is empty → answer = -1
#     - Else → find max XOR of xi using trie.


# Example Walkthrough (Intuition)
# nums = [0,1,2,4,5,9]
# queries sorted by m
#
# | Query (x,m) | Trie contains | Best XOR |
# | ----------- | ------------- | -------- |
# | (3,0)       | {0}           | 3        |
# | (7,5)       | {0,1,2,4,5}   | 7        |
# | (7,9)       | {0,1,2,4,5,9} | 14       |


# ----------------------------------------
# Helper functions for bit operations
# ----------------------------------------

def get_bit(num: int, i: int) -> int:
    """
    Returns the ith bit (0 or 1) of num.
    """
    return (num >> i) & 1


def set_bit(value: int, i: int) -> int:
    """
    Sets the ith bit of value to 1.
    """
    return value | (1 << i)


# ----------------------------------------
# Trie Node for Binary Trie
# ----------------------------------------

class TrieNode:
    def __init__(self):
        self.left = None   # represents bit 0
        self.right = None  # represents bit 1


# ----------------------------------------
# Binary Trie for XOR operations
# ----------------------------------------

class BinaryTrie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        """
        Inserts the 32-bit representation of num into the trie.
        """
        node = self.root
        for i in range(31, -1, -1):
            bit = get_bit(num, i)

            if bit == 0:
                if not node.left:
                    node.left = TrieNode()
                node = node.left
            else:
                if not node.right:
                    node.right = TrieNode()
                node = node.right

    def get_max_xor(self, num: int) -> int:
        """
        Returns the maximum XOR of num with any number
        currently stored in the trie.
        """
        node = self.root
        max_xor = 0

        for i in range(31, -1, -1):
            bit = get_bit(num, i)

            # Prefer opposite bit for maximizing XOR
            if bit == 0:
                if node.right:
                    max_xor = set_bit(max_xor, i)
                    node = node.right
                else:
                    node = node.left
            else:
                if node.left:
                    max_xor = set_bit(max_xor, i)
                    node = node.left
                else:
                    node = node.right

        return max_xor


# ----------------------------------------
# Main Function: Maximum XOR with constraint
# ----------------------------------------

def maximizeXor(nums, queries):
    """
    nums: List[int]
    queries: List[List[int]] where each query = [xi, mi]

    Returns:
    List[int] where each element is the answer for the query.
    """

    # Sort nums so we can insert only valid numbers (<= mi)
    nums.sort()

    # Store queries as (mi, xi, original_index)
    offline_queries = []
    for idx, (x, m) in enumerate(queries):
        offline_queries.append((m, x, idx))

    # Sort queries by mi
    offline_queries.sort()

    trie = BinaryTrie()
    answers = [-1] * len(queries)

    nums_idx = 0
    n = len(nums)

    # Process queries in increasing order of mi
    for m, x, q_idx in offline_queries:

        # Insert all nums <= m into the trie
        while nums_idx < n and nums[nums_idx] <= m:
            trie.insert(nums[nums_idx])
            nums_idx += 1

        # If no valid numbers were inserted
        if nums_idx == 0:
            answers[q_idx] = -1
        else:
            answers[q_idx] = trie.get_max_xor(x)

    return answers


# ----------------------------------------
# Example Usage
# ----------------------------------------

nums = [4, 9, 2, 5, 0, 1]
queries = [[3, 0], [3, 10], [7, 5], [7, 9]]

print(maximizeXor(nums, queries))
# Output: [3, 10, 7, 14]
