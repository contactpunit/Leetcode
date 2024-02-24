# Given an array nums. We define a running sum of an array as runningSum[i] = sum(nums[0]…nums[i]).

# Return the running sum of nums.

# Example 1:

# Input: nums = [1,2,3,4]
# Output: [1,3,6,10]
# Explanation: Running sum is obtained as follows: [1, 1+2, 1+2+3, 1+2+3+4].
# Example 2:

# Input: nums = [1,1,1,1,1]
# Output: [1,2,3,4,5]
# Explanation: Running sum is obtained as follows: [1, 1+1, 1+1+1, 1+1+1+1, 1+1+1+1+1].
# Example 3:

# Input: nums = [3,1,2,10,1]
# Output: [3,4,6,16,17]

def runningSum(nums):
    # method with time complexty O(n) and space complexity O(1) w/ousingextra array
    for idx, elem in enumerate(nums):
        if idx != 0:
            nums[idx] = elem + nums[idx - 1]
    return nums

nums = [1,2,3,4]
print(runningSum(nums))

nums = [1,1,1,1,1]
print(runningSum(nums))

nums = [3,1,2,10,1]
print(runningSum(nums))
