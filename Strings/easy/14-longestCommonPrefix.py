# Write a function to find the longest common prefix string amongst an array of strings.

# If there is no common prefix, return an empty string "".

 

# Example 1:

# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:

# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation: There is no common prefix among the input strings.


def longestCommonPrefix(strs) -> str:
    counter = 0
    for i in zip(*strs):
        result = all(element == i[0] for element in i)
        if result:
            counter += 1
        else:
            return strs[0][:counter]
    return strs[0][:counter]

print(longestCommonPrefix(strs = ["flower","flow","flight"]))
