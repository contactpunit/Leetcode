# Given an integer x, return true if x is a 
# palindrome
# , and false otherwise.

 

# Example 1:

# Input: x = 121
# Output: true
# Explanation: 121 reads as 121 from left to right and from right to left.
# Example 2:

# Input: x = -121
# Output: false
# Explanation: From left to right, it reads -121. From right to left, it becomes 121-. 
# Therefore it is not a palindrome.
# Example 3:
# Input: x = 10
# Output: false
# Explanation: Reads 01 from right to left. Therefore it is not a palindrome.

def isPalindrome(x: int):
    # without python library
    isPalindrome = True
    x_in_str = str(x)
    start = 0
    end = len(x_in_str) -1
    while start < end:
        if x_in_str[start] != x_in_str[end]:
            isPalindrome = False
            break
            return False
        else:
            start += 1
            end -= 1
    return isPalindrome

print(isPalindrome(121))
print(isPalindrome(-121))
print(isPalindrome(10))