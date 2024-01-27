# Given an integer array nums, move all the even integers at the beginning of the array 
# followed by all the odd integers.

# Return any array that satisfies this condition.

 

# Example 1:

# Input: nums = [3,1,2,4]
# Output: [2,4,3,1]
# Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.
# Example 2:

# Input: nums = [0]
# Output: [0]

def sortArrayByParity(nums):
    start = 0
    end = len(nums) -1
    while start < end:
        if nums[start] % 2 != 0:
            if nums[end] % 2 == 0:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1
            else:
                end -= 1
        else:
            start += 1
    return nums
         

sortArrayByParity([3,1,2,4])