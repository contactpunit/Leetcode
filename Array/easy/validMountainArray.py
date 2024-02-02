# Given an array of integers arr, return true if and only if it is a valid mountain array.

# Recall that arr is a mountain array if and only if:

# arr.length >= 3
# There exists some i with 0 < i < arr.length - 1 such that:
# arr[0] < arr[1] < ... < arr[i - 1] < arr[i] 
# arr[i] > arr[i + 1] > ... > arr[arr.length - 1]

 

# Example 1:

# Input: arr = [2,1]
# Output: false
# Example 2:

# Input: arr = [3,5,5]
# Output: false
# Example 3:

# Input: arr = [0,3,2,1]
# Output: true
 
def validMountainArray(arr):
    if len(arr) < 3:
        return False
    else:
        start = 0
        end = len(arr) - 1
        if arr[end] > arr[end - 1] or arr[start + 1] < arr[start]:
            return False
        while start < end and start + 1 != end:
            if arr[start] == arr[start + 1] or arr[end] == arr[end - 1]:
                return False
            if arr[start + 1] > arr[start]:
                start += 1
            elif arr[end] < arr[end - 1]:
                end -= 1
            else:
                return False
        if start + 1 != end:
            return False
        return True
        
 
arr = [3,5,5]
print(validMountainArray(arr))
arr = [0,3,2,1]
print(validMountainArray(arr))
arr = [1,3,2]
print(validMountainArray(arr))
arr = [0,1,2,3,4,5,6,7,8,9]
print(validMountainArray(arr))
arr = [3, 2, 4]
print(validMountainArray(arr))
arr = [0,1,2,4,2,1]
print(validMountainArray(arr))
arr = [0,1,6,8,7,2,1]
print(validMountainArray(arr))
arr = [9,8,7,6,5,4,3,2,1,0]
print(validMountainArray(arr))

