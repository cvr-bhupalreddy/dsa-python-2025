# 📌 Summary Table (Easy to Remember)
# | Stack Top | Incoming | Direction | Will They Collide? | Why                      |
# | --------- | -------- | --------- | ------------------ | ------------------------ |
# | +         | -        | → ←       | YES                | Moving toward each other |
# | -         | +        | ← →       | NO                 | Moving away              |
# | +         | +        | → →       | NO                 | Same direction           |
# | -         | -        | ← ←       | NO                 | Same direction           |


def asteroid_collision_bruteforce(asteroids):
    # Create a separate list so original is untouched
    remaining = asteroids[:]  # readable and clear

    changed = True
    while changed:
        changed = False
        i = 0

        # Check every adjacent pair for possible collision
        while i < len(remaining) - 1:
            left = remaining[i]
            right = remaining[i + 1]

            # Collision occurs only when left → and right ←
            if left > 0 > right:
                changed = True

                if abs(left) > abs(right):
                    # Right asteroid explodes
                    remaining.pop(i + 1)
                elif abs(left) < abs(right):
                    # Left asteroid explodes
                    remaining.pop(i)
                else:
                    # Both explode
                    remaining.pop(i + 1)
                    remaining.pop(i)

                # After removal, continue without incrementing i
            else:
                i += 1

    return remaining


def asteroid_collision(arr):
    stack = []

    for a in arr:

        # Try to process collision only when:
        #   stack top is moving RIGHT  (top > 0)
        #   current asteroid is moving LEFT (a < 0)
        # Only this combination produces a collision.
        while stack and stack[-1] > 0 > a:
            # while stack and stack[-1] > 0 and a < 0:

            top = stack[-1]

            # CASE 1: Incoming asteroid is bigger (abs(a) > abs(top))
            # → Top one explodes; continue checking deeper into stack.
            if abs(top) < abs(a):
                stack.pop()
                continue

            # CASE 2: Equal size → both explode → stop processing and do NOT push a
            elif abs(top) == abs(a):
                stack.pop()
                break

            # CASE 3: Top is bigger → incoming asteroid (a) explodes → do NOT push a
            else:
                break

        else:
            # IMPORTANT:
            # This else executes ONLY if the while loop did NOT break.
            #
            # Means:
            #   1. No collision happened, OR
            #   2. Incoming asteroid survived all collisions
            #
            # So we safely push it.
            stack.append(a)

    return stack

# | Approach            | Time  | Space | Notes                                    |
# | ------------------- | ----- | ----- | ---------------------------------------- |
# | **Bruteforce**      | O(n²) | O(1)  | repeated rescans, repeated deletions     |
# | **Stack (Optimal)** | O(n)  | O(n)  | each asteroid pushed/popped at most once |
