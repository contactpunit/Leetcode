# Given a string s and an array of strings words, determine whether s is a prefix string of words.

# A string s is a prefix string of words if s can be made by concatenating the first k strings
# in words for some positive k no larger than words.length.

# Return true if s is a prefix string of words, or false otherwise.

# Example 1:

# Input: s = "iloveleetcode", words = ["i","love","leetcode","apples"]
# Output: true
# Explanation:
# s can be made by concatenating "i", "love", and "leetcode" together.
# Example 2:

# Input: s = "iloveleetcode", words = ["apples","i","love","leetcode"]
# Output: false
# Explanation:
# It is impossible to make s using a prefix of arr.

def isPrefixString(s, words):
    n = len(words)
    for i in range(n):
        print("".join(words[:i+1]), s)
        if "".join(words[:i+1]) == s:
            return True
    return False
        

s = "iloveleetcode"
words = ["i","love","leetcode","apples"]
print(isPrefixString(s, words))

# s = "iloveleetcode"
# words = ["apples","i","love","leetcode"]
# print(isPrefixString(s, words))

# s = "a"
# words = ["aa","aaaa","banana"]
# print(isPrefixString(s, words))

# s="aaa"
# words = ["aa","aaa","fjaklfj"]
# print(isPrefixString(s, words))

# s="z"
# words = ["z"]
# print(isPrefixString(s, words))

# s ="aaaaaaa"
# words =["a","a","a","a","a","a"]
# print(isPrefixString(s, words))