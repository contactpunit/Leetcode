# Given a string s, reverse the order of characters in each word within a sentence while still
# preserving whitespace and initial word order.

 

# Example 1:

# Input: s = "Let's take LeetCode contest"
# Output: "s'teL ekat edoCteeL tsetnoc"
# Example 2:

# Input: s = "Mr Ding"
# Output: "rM gniD"

def reverseWords(s):
    reversedStr = []
    for part in s.split():
        revString = ''
        i = len(part) - 1
        while i >= 0:
            revString += part[i]
            i -= 1
        reversedStr.append(revString)
    return ' '.join(reversedStr)
        

s = "Let's take LeetCode contest"
# s = "abcd"
print(reverseWords(s))