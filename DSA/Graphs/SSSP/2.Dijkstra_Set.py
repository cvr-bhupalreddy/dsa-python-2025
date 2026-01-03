# Using a Set Instead of Priority Queue
#
# A set maintains sorted order, so the smallest distance is always at the beginning.
#
# Store:
#     (dist, node)


# Operations
#
# | Operation        | Set          | Priority Queue  |
# | ---------------- | ------------ | --------------- |
# | Extract min      | O(1) (begin) | O(log V)        |
# | Insert           | O(log V)     | O(log V)        |
# | Delete arbitrary | O(log V)     | ❌ Not supported |
# | Decrease key     | O(log V)     | ❌ Not directly  |

# Key advantage: Set allows delete + insert (true decrease-key).


#
# “Yes, Dijkstra can be implemented using a set instead of a priority queue.
# In C++, a set supports ordered elements and efficient decrease-key via erase + insert.
# In Python, since sets are unordered, priority queues are preferred.”


# Priority Queue vs Set (Conceptual Difference)
# | Feature           | Priority Queue | Set |
# | ----------------- | -------------- | --- |
# | Decrease-key      | ❌              | ✅   |
# | Duplicate entries | ✅              | ❌   |
# | Simplicity        | ✅              | ⚠️  |
# | Python-friendly   | ✅              | ❌   |
