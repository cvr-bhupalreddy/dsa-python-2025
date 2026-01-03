# To maximize XOR, we want two numbers that differ as much as possible in their binary representation,
# especially at higher bits.

# ✅ Approach (Binary Trie)
# Key Observations
#     XOR is maximized when bits differ (1 ^ 0 = 1)
#     Check bits from most significant bit (31) to least significant bit (0)
#     While traversing the trie, always try to take the opposite bit


# 🏗️ Data Structure
#     Each trie node has:
#         left → bit 0
#         right → bit 1


class TrieNode:
    def __init__(self):
        self.left = None  # represents bit 0
        self.right = None  # represents bit 1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    # Insert number into trie
    def insert(self, num: int):
        node = self.root
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if not node.left:
                    node.left = TrieNode()
                node = node.left
            else:
                if not node.right:
                    node.right = TrieNode()
                node = node.right

    # Get maximum XOR with num
    def getMaxXor(self, num: int) -> int:
        node = self.root
        max_xor = 0
        for i in range(31, -1, -1):
            bit = (num >> i) & 1
            if bit == 0:
                if node.right:
                    max_xor |= (1 << i)
                    node = node.right
                else:
                    node = node.left
            else:
                if node.left:
                    max_xor |= (1 << i)
                    node = node.left
                else:
                    node = node.right
        return max_xor


def findMaximumXOR(nums):
    trie = Trie()
    max_result = 0

    # Insert first number
    trie.insert(nums[0])

    # Insert numbers one by one and compute max XOR
    for i in range(1, len(nums)):
        max_result = max(max_result, trie.getMaxXor(nums[i]))
        trie.insert(nums[i])

    return max_result

# Insert(Num)
# What this method does
#     Inserts the 32-bit binary representation of a number into the trie
#     Builds a path from MSB (31st bit) to LSB (0th bit)
#
# Why it is needed
#
#     Stores numbers in a structure that allows fast bitwise comparison
#     Enables greedy XOR matching later
#
# How it works
#
#     For each bit:
#         Go left for 0
#         Go right for 1
#     Create node if missing


# getMaxXor(num)
# What this method does
#     Finds the maximum XOR value achievable with num using numbers already in the trie
#
# Why it is needed
#     For each bit, we want the opposite bit if possible (1 ^ 0 = 1)
#     Greedy choice at higher bits gives maximum result
#
# How it works
# Traverse from MSB → LSB
# For each bit:
#     If bit is 0, try to go to 1
#     If bit is 1, try to go to 0
#
# If opposite bit exists:
#     Set that bit in XOR result
# Else:
#     Follow same bit path
