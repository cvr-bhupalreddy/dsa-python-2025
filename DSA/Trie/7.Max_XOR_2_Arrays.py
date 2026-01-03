class TrieNode:
    def __init__(self):
        self.left = None  # bit 0
        self.right = None  # bit 1


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num: int):
        """
        Inserts the 32-bit binary representation of num into the trie.
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

    def getMaxXorWithPair(self, num: int):
        """
        Finds:
        1. Maximum XOR value with num
        2. The number from the trie that produces this XOR
        """
        node = self.root
        max_xor = 0
        partner = 0  # number from array1 that gives max XOR

        for i in range(31, -1, -1):
            bit = get_bit(num, i)

            # Prefer opposite bit
            if bit == 0:
                if node.right:
                    max_xor = set_bit(max_xor, i)
                    partner = set_bit(partner, i)
                    node = node.right
                else:
                    node = node.left
            else:
                if node.left:
                    max_xor = set_bit(max_xor, i)
                    node = node.left
                else:
                    partner = set_bit(partner, i)
                    node = node.right

        return max_xor, partner


def get_bit(num: int, i: int) -> int:
    """
    Returns the bit (0 or 1) at position i in num.
    Equivalent to: (num >> i) & 1
    """
    return (num >> i) & 1


def set_bit(value: int, i: int) -> int:
    """
    Sets the ith bit in value to 1.
    Used when building the XOR result.
    """
    return value | (1 << i)


def maxXorBetweenTwoArrays(arr1, arr2):
    """
    Returns:
    - Maximum XOR value
    - Pair (x from arr1, y from arr2) producing that XOR
    """
    trie = Trie()

    # Insert all elements of arr1
    for num in arr1:
        trie.insert(num)

    max_xor = 0
    best_pair = (None, None)

    # Try all elements from arr2
    for num in arr2:
        curr_xor, partner = trie.getMaxXorWithPair(num)

        if curr_xor > max_xor:
            max_xor = curr_xor
            best_pair = (partner, num)

    return max_xor, best_pair
