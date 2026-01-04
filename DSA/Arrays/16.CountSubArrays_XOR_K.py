# Use prefix XOR + hashmap.
#
# Let prefix_xor = XOR of all elements from nums[0] to nums[i].
# For a subarray (l..r) to have xor = k:
# prefix_xor[r] XOR prefix_xor[l-1] = k
# →  prefix_xor[l-1] = prefix_xor[r] XOR k
#
# So at each index r:
# count += how many prefix_xor values equal (prefix_xor[r] XOR k)
#
# We keep a hashmap to store frequencies of all prefix_xor seen so far.
#
# Algorithm:
#     1. prefix_xor = 0
#     2. map = {0: 1}   # empty prefix [there exist a empty sub array with XOR O]
#     3. For each element:
#         prefix_xor ^= element
#         count += map.get(prefix_xor XOR k, 0)
#         map[prefix_xor] += 1
#     4. Return count


# 1️⃣ Use Prefix XOR:
#     - Let prefix_xor[i] = arr[0] ^ arr[1] ^ ... ^ arr[i]
#
# 2️⃣ Subarray XOR formula:
#     - XOR of subarray arr[l..r] = prefix_xor[r] ^ prefix_xor[l-1]  (for l > 0)
#     - If l = 0, subarray XOR = prefix_xor[r]
#
# 3️⃣ Solve using HashMap:
#     - Keep a hashmap 'count' to store frequency of prefix_xor values seen so far
#     - For each prefix_xor[i]:
#     - Check if prefix_xor[i] ^ K exists in map
#     - If yes, add count[prefix_xor[i] ^ K] to answer
#     - If prefix_xor[i] == K, increment answer by 1
#     - Increment count[prefix_xor[i]] in map

from collections import defaultdict


def count_subarrays_xor_k_simple(arr, K):
    """
    Count subarrays with XOR equal to K using prefix XOR and hashmap.
    Case where prefix XOR itself equals K is handled by initializing count_map[0] = 1
    """
    prefix_xor = 0
    count_map = defaultdict(int)
    count_map[0] = 1  # Handle subarrays starting from index 0
    total_subarrays = 0

    for num in arr:
        prefix_xor ^= num  # update prefix XOR

        # Count subarrays ending here with XOR = K
        total_subarrays += count_map[prefix_xor ^ K]

        # Update the count of current prefix XOR
        count_map[prefix_xor] += 1

    return total_subarrays


def count_subarrays_xor_k(arr, K):
    """
    Count subarrays with XOR equal to K using prefix XOR and hashmap
    """
    prefix_xor = 0
    count_map = defaultdict(int)
    total_subarrays = 0

    for num in arr:
        prefix_xor ^= num  # update prefix XOR

        # Case 1: Prefix XOR itself equals K
        if prefix_xor == K:
            total_subarrays += 1

        # Case 2: Check if there is any previous prefix XOR that can form K
        if (prefix_xor ^ K) in count_map:
            total_subarrays += count_map[prefix_xor ^ K]

        # Update the count of current prefix XOR
        count_map[prefix_xor] += 1

    return total_subarrays

# 🔹 Summary Table
# | Aspect                  | Complexity                                             |
# | ----------------------- | ------------------------------------------------------ |
# | Time                    | O(n)                                                   |
# | Space                   | O(n)                                                   |
# | Method                  | Prefix XOR + Hashmap                                   |
# | Extra Space Saved Trick | count_map[0] = 1 handles subarrays starting at index 0 |
