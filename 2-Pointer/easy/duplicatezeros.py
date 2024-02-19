# Given a fixed-length integer array arr, duplicate each occurrence of zero, 
# shifting the remaining elements to the right.

# Note that elements beyond the length of the original array are not written. Do the above modifications to the input array in place and do not return anything.

 

# Example 1:

# Input: arr = [1,0,2,3,0,4,5,0]
# Output: [1,0,0,2,3,0,0,4]
# Explanation: After calling your function, the input array is modified to: [1,0,0,2,3,0,0,4]
# Example 2:

# Input: arr = [1,2,3]
# Output: [1,2,3]
# Explanation: After calling your function, the input array is modified to: [1,2,3]


# zeros = arr.count(0)
#     i = len(arr) - 1
#     j = len(arr) + zeros - 1

#     while i < j:
#       if j < len(arr):
#         arr[j] = arr[i]
#       if arr[i] == 0:
#         j -= 1
#         if j < len(arr):
#           arr[j] = arr[i]
#       i -= 1
#       j -= 1
#     print(arr)

def duplicateZeros(arr):
    count = arr.count(0)
    if count == 0:
        return arr
    else:
        i = len(arr) - 1
        j = i + count
        while i < j:
            if j > len(arr) - 1:
                if arr[i] == 0:
                   j -= 1
                   if j < len(arr):
                       arr[j] = arr[i]
                j -= 1
                i -= 1
            else:
                arr[j] = arr[i]
                if arr[i] == 0: 
                    j -= 1
                    if j < len(arr):
                        arr[j] = arr[i]
                i -= 1
                j -= 1 
    print(arr)

arr = [1,0,2,3,0,5]
duplicateZeros(arr)

arr = [1,0,2,3,0,4,5,0]
duplicateZeros(arr)
