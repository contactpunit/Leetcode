# Given two strings needle and haystack, return the index of the first occurrence of needle in haystack,
# or -1 if needle is not part of haystack.

 

# Example 1:

# Input: haystack = "sadbutsad", needle = "sad"
# Output: 0
# Explanation: "sad" occurs at index 0 and 6.
# The first occurrence is at index 0, so we return 0.
# Example 2:

# Input: haystack = "leetcode", needle = "leeto"
# Output: -1
# Explanation: "leeto" did not occur in "leetcode", so we return -1.

def strStr(haystack, needle):
    nlen = len(needle)
    i = 0
    startidx = -1
    if nlen > len(haystack) or nlen == 0:
        return startidx
    while i < len(haystack):
        if haystack[i] == needle[0]:
            try:
                if haystack[i + nlen - 1] == needle[nlen - 1]:
                    startidx = i
                    for j in range(nlen):
                        if haystack[i + j] != needle[j]:
                            startidx = -1
                            break
                    if startidx != -1:
                        return startidx
                    else:
                        i += 1
                else:
                        i += 1
            except IndexError:
                return -1
        else:
            i += 1
    return startidx       

print(strStr('sadbutsad', 'leeto'))
print(strStr('sadbutsad', 'sad'))
print(strStr('hello', 'll'))
print(strStr('aaa', 'aaaa'))
print(strStr('mississippi', 'issipi'))