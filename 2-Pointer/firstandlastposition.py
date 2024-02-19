# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.

# If target is not found in the array, return [-1, -1].

# You must write an algorithm with O(log n) runtime complexity.

# Example 1:

# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
# Example 2:

# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
# Example 3:

# Input: nums = [], target = 0
# Output: [-1,-1]
 
def searchRange(nums, target):
    start = 0
    firststart = 0
    endend = len(nums) - 1
    end = len(nums) - 1
    firsindex = ''
    endindex = ''
    while start < end:
        mid = (end + start) // 2
        firstend = mid - 1
        endstart = mid + 1
        if nums[mid] == target:
            firstindex = endindex = mid


nums = [5,7,7,8,8,10]
target = 8
searchRange(nums, target)