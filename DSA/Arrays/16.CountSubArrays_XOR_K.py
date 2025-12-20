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
#     2. map = {0: 1}   # empty prefix
#     3. For each element:
#         prefix_xor ^= element
#         count += map.get(prefix_xor XOR k, 0)
#         map[prefix_xor] += 1
#     4. Return count
