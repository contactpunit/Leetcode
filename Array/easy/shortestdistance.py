# Given a string s and a character c that occurs in s, return an array of integers answer
# where answer.length == s.length and answer[i] is the distance from index i to the closest
# occurrence of character c in s.

# The distance between two indices i and j is abs(i - j), where abs is the absolute value function.


# Example 1:

# Input: s = "loveleetcode", c = "e"
# Output: [3,2,1,0,1,0,0,1,2,2,1,0]
# Explanation: The character 'e' appears at indices 3, 5, 6, and 11 (0-indexed).
# The closest occurrence of 'e' for index 0 is at index 3, so the distance is abs(0 - 3) = 3.
# The closest occurrence of 'e' for index 1 is at index 3, so the distance is abs(1 - 3) = 2.
# For index 4, there is a tie between the 'e' at index 3 and the 'e' at index 5, but the distance is
# still the same: abs(4 - 3) == abs(4 - 5) = 1.
# The closest occurrence of 'e' for index 8 is at index 6, so the distance is abs(8 - 6) = 2.
# Example 2:

# Input: s = "aaab", c = "b"
# Output: [3,2,1,0]
 
def shortestToChar(s, c):
    final = []
    size = len(s)
    for idx, char in enumerate(s):
        start = end = idx
        found = 0
        if char == c:
            final.append(0)
            continue
        while start > 0 and end < size -1:
            start -= 1
            end += 1
            if s[start] == c:
                final.append(abs(idx - start))
                found = 1
                break
            elif s[end] == c:
                final.append(abs(end - idx))
                found = 1
                break
        if found == 0 and start <= 0:
            if end < size - 1:
                while end <= size - 1:
                    if s[end] == c:
                        final.append(abs(end - idx))
                        found = 1
                        break
                    end += 1
        elif found == 0 and end >= size -1:
            if start > 0:
                while start >= 0:
                    if s[start] == c:
                        final.append(abs(idx - start))
                        found = 1
                        break
                    start -= 1
    return final

s = "loveleetcode"
c = "e"
print(shortestToChar(s, c))
s = "aaab"
c = "b"
print(shortestToChar(s, c))