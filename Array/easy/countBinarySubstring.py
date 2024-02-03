# Given a binary string s, return the number of non-empty substrings that have the same
# number of 0's and 1's, and all the 0's and all the 1's in these substrings are grouped consecutively.

# Substrings that occur multiple times are counted the number of times they occur.

 

# Example 1:

# Input: s = "00110011"
# Output: 6
# Explanation: There are 6 substrings that have equal number of consecutive
# 1's and 0's: "0011", "01", "1100", "10", "0011", and "01".
# Notice that some of these substrings repeat and are counted the number of times they occur.
# Also, "00110011" is not a valid substring because all the 0's (and 1's) are not grouped together.
# Example 2:

# Input: s = "10101"
# Output: 4
# Explanation: There are 4 substrings: "10", "01", "10", "01" that have equal number of 
# consecutive 1's and 0's.
from itertools import takewhile

def countBinarySubstrings(s):
    start = 0
    beginpart = []
    endpart = []
    char = s[0]
    count = 0
    while start < len(s):
        if len(beginpart) > 0:
            beginpart = endpart[::]
            endpart = []
            char = '0' if beginpart[0] == '0' else '1'
        else:
            while start < len(s) and s[start] == char:
                beginpart.append(s[start])
                start += 1
        while start < len(s) and s[start] != char:
            endpart.append(s[start])
            start += 1
        count += min(len(beginpart), len(endpart))
    print(count)
        
        

s = "10101"
countBinarySubstrings(s)
s = "00110011"
countBinarySubstrings(s)
