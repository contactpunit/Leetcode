# Given a string s, reverse the string according to the following rules:

# All the characters that are not English letters remain in the same position.
# All the English letters (lowercase or uppercase) should be reversed.
# Return s after reversing it.

 

# Example 1:

# Input: s = "ab-cd"
# Output: "dc-ba"
# Example 2:

# Input: s = "a-bC-dEf-ghIj"
# Output: "j-Ih-gfE-dCba"
# Example 3:

# Input: s = "Test1ng-Leet=code-Q!"
# Output: "Qedo1ct-eeLg=ntse-T!"

def reverseOnlyLetters(s):
    wordlist = list(s)
    start = 0
    end = len(wordlist) - 1
    while start < end:
        if wordlist[start].isalpha() and wordlist[end].isalpha():
            wordlist[start], wordlist[end] = wordlist[end], wordlist[start]
            start += 1
            end -= 1
        else:
            if not wordlist[start].isalpha():
                start += 1
            elif not wordlist[end].isalpha():
                end -= 1
    return ''.join(wordlist) 

s = "a-bC-dEf-ghIj"
print(reverseOnlyLetters(s))