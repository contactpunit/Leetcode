# Given an array of strings words, return the first palindromic string in the array. 
# If there is no such string, return an empty string "".

# A string is palindromic if it reads the same forward and backward.

 

# Example 1:

# Input: words = ["abc","car","ada","racecar","cool"]
# Output: "ada"
# Explanation: The first string that is palindromic is "ada".
# Note that "racecar" is also palindromic, but it is not the first.
# Example 2:

# Input: words = ["notapalindrome","racecar"]
# Output: "racecar"
# Explanation: The first and only string that is palindromic is "racecar".
# Example 3:

# Input: words = ["def","ghi"]
# Output: ""
# Explanation: There are no palindromic strings, so the empty string is returned.

def firstPalindrome(words):
    for word in words:
        start = 0
        end = len(word) - 1
        nomatch = 0
        while start < end:
            if word[start] != word[end]:
                nomatch = 1
                break
            start += 1
            end -= 1
        if nomatch == 0:
            return word
    return ""
            

print(firstPalindrome(["notapalindrome","racecar"]))
print(firstPalindrome(["abc","car","ada","racecar","cool"]))
print(firstPalindrome(["def","ghi"]))