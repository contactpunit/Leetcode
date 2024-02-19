# Given two strings s and t, return true if they are equal when both are typed into empty text editors.
# '#' means a backspace character.

# Note that after backspacing an empty text, the text will continue empty.

# Example 1:

# Input: s = "ab#c", t = "ad#c"
# Output: true
# Explanation: Both s and t become "ac".
# Example 2:

# Input: s = "ab##", t = "c#d#"
# Output: true
# Explanation: Both s and t become "".
# Example 3:

# Input: s = "a#c", t = "b"
# Output: false
# Explanation: s becomes "c" while t becomes "b".

def backspaceCompare(s, t):
    i = len(s) - 1
    j = len(t) - 1
    ihash = 0
    jhash = 0
    while i >= 0 or j >= 0:
        while i >= 0:
            if s[i] == '#':
                ihash += 1
                i -= 1
            elif ihash > 0:
                i -= 1
                ihash -= 1
            else:
                break
                
        while j >= 0:
            if t[j] == '#':
                jhash += 1
                j -= 1
            elif jhash > 0:
                j -= 1
                jhash -= 1
            else:
                break
        
        if i >= 0  and j >= 0 and s[i] != t[j]:
            return False
        
        if i >= 0 and j < 0:
            return False
        if i < 0 and j >= 0:
            return False
        
        i -= 1
        j -= 1
        
    return True
                        
            

s = "xywrrmp"
t = "xywrrm#p"
print(backspaceCompare(s, t))

# s = "a##c" Abc###
# t = "#a#c"
# print(backspaceCompare(s, t))


# s = "a#####k"
# t = "bnnnnnnk"
# print(backspaceCompare(s, t))

# s = "ab#c"
# t = "ad#c"
# print(backspaceCompare(s, t))

# s = "ab##"
# t = "c#d#"
# print(backspaceCompare(s, t))

# s = "c#b"
# t = "b"
# print(backspaceCompare(s, t))