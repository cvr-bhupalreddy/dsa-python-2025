def countAndSay(n: int) -> str:
    # Base case
    if n == 1:
        return "1"

    prev = countAndSay(n-1)
    result = ""
    i = 0
    while i < len(prev):
        count = 1
        # Count consecutive same digits
        while i + 1 < len(prev) and prev[i] == prev[i+1]:
            i += 1
            count += 1
        result += str(count) + prev[i]  # append "count + digit"
        i += 1
    return result

# ✅ Example
for i in range(1, 6):
    print(f"{i}: {countAndSay(i)}")


def countAndSay_iter(n: int) -> str:
    result = "1"
    for _ in range(1, n):
        prev = result
        result = ""
        i = 0
        while i < len(prev):
            count = 1
            while i + 1 < len(prev) and prev[i] == prev[i+1]:
                i += 1
                count += 1
            result += str(count) + prev[i]
            i += 1
    return result
