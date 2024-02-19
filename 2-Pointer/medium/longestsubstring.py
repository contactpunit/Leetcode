
# Example 1:

# Input: s = "abcabcbb"
# Output: 3
# Explanation: The answer is "abc", with the length of 3.
# Example 2:

# Input: s = "bbbbb"
# Output: 1
# Explanation: The answer is "b", with the length of 1.
# Example 3:

# Input: s = "pwwkew"
# Output: 3
# Explanation: The answer is "wke", with the length of 3.
# Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

def lengthOfLongestSubstring(s):
    maxlen = 0
    count = 0
    movingidx = 0
    letterHash = dict()
    for idx, elem in enumerate(s):
        if elem not in letterHash:
            letterHash[elem] = idx
            count += 1
        elif elem in letterHash:
            if letterHash[elem] >= movingidx:
                maxlen = max(maxlen, count)
                movingidx = letterHash[elem] + 1
                count = idx - letterHash[elem]
                letterHash[elem] = idx
            else:
                count += 1
                letterHash[elem] = idx
    return max(maxlen, count)
   
            

# s = "abcabcbb"
# print(lengthOfLongestSubstring(s))
s = "pwwkez"
print(lengthOfLongestSubstring(s))
# s = "bbbbb"
# print(lengthOfLongestSubstring(s))

