# Given an array arr of integers, check if there exist two indices i and j such that :

# i != j
# 0 <= i, j < arr.length
# arr[i] == 2 * arr[j]
 

# Example 1:

# Input: arr = [10,2,5,53]
# Output: true
# Explanation: For i = 0 and j = 2, arr[i] == 10 == 2 * 5 == 2 * arr[j]
# Example 2:

# Input: arr = [3,1,7,11]
# Output: false
# Explanation: There is no i and j that satisfy the conditions.

def checkIfExist(arr):
    s = set(arr)
    for elem in arr:
        if elem * 2 in s:
            return True
    return False
    

arr = [10,2,5,3]
print(checkIfExist(arr))

arr = [3,1,7,11]
print(checkIfExist(arr))

arr = [-10,12,-20,-8,15]
print(checkIfExist(arr))

arr = [-16,-13,8]
print(checkIfExist(arr))

arr = [-20,8,-6,-14,0,-19,14,4]
print(checkIfExist(arr))

arr = [0, 0]
print(checkIfExist(arr))

# arr = [-16,-19]
# print(checkIfExist(arr))