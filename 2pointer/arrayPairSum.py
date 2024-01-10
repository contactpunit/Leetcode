# given an array of sorted numbers and a target sum, 
# find a pair in the array whose sum is equal to target sum
# [1,2,3,4,5] , target sum = 7

def findPair(arrayOfNums, targetSum):
    leftPointer = 0
    lastPointer = len(arrayOfNums) - 1
    for _ in range(len(arrayOfNums) - 1):
        if arrayOfNums[leftPointer] + arrayOfNums[lastPointer] < targetSum:
            leftPointer += 1
        elif arrayOfNums[leftPointer] + arrayOfNums[lastPointer] > targetSum:
            lastPointer -= 1
        elif arrayOfNums[leftPointer] + arrayOfNums[lastPointer] == targetSum:
            return (arrayOfNums[leftPointer], arrayOfNums[lastPointer])
        elif arrayOfNums[leftPointer] == arrayOfNums[lastPointer]:
            return -1
    return -1
            
print(findPair([1, 2, 3, 4, 5], 7)) # [2, 5]
print(findPair([1, 6, 8, 9, 10], 14)) # [6, 8]
print(findPair([1, 2, 3, 4, 5], 10)) # -1
