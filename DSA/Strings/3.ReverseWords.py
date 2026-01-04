def reverseWords(s: str) -> str:
    # Step 1: Split string into words, automatically removes extra spaces
    words = s.split()

    # Step 2: Reverse the list of words
    reversed_words = words[::-1]

    # Step 3: Join the words with a single space
    return ' '.join(reversed_words)


# ✅ Example
s = "welcome to the jungle"
print(reverseWords(s))  # Output: "jungle the to welcome"


# Reverse the entire input string first. Start iterating through the string to process each word.
# Words are identified as sequences of characters separated by spaces.
# For each word found, its characters are reversed individually while maintaining their relative positions
# in the sentence and moving them in front to trim down any unnecessary spaces.
# Any extra spaces at the end are removed before returning the final result.

class Solution:
    def reverseString_1(self, s, start, end):
        while start < end:
            s[start], s[end] = s[end], s[start]
            start += 1
            end -= 1

    def reverseWords(self, s: str) -> str:
        n = len(s)

        # Reverse the entire string
        s = list(s)
        self.reverseString_1(s, 0, n - 1)

        i = 0
        j = 0
        start = 0
        end = 0

        while j < n:
            # Skip spaces
            while j < n and s[j] == ' ':
                j += 1
            if j == n:
                break

            start = i

            # Copy the word characters forward
            while j < n and s[j] != ' ':
                s[i] = s[j]
                i += 1
                j += 1

            end = i - 1

            # Reverse the current word using start and end
            self.reverseString(s, start, end)

            # Add a space after the word if it's not the last word
            if j < n:
                s[i] = ' '
                i += 1

        # Remove trailing space if present
        if i > 0 and s[i - 1] == ' ':
            i -= 1

        return "".join(s[:i])


if __name__ == "__main__":
    s = " amazing coding skills "

    # Creating an instance of Solution class
    sol = Solution()

    # Function call to reverse every word in the given string
    ans = sol.reverseWords(s)

    # Output
    print("Input string:", s)
    print("After reversing every word:", ans)
