# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

# Notice that the solution set must not contain duplicate triplets.

# Example 1:

# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
# Explanation: 
# nums[0] + nums[1] + nums[2] = (-1) + 0 + 1 = 0.
# nums[1] + nums[2] + nums[4] = 0 + 1 + (-1) = 0.
# nums[0] + nums[3] + nums[4] = (-1) + 2 + (-1) = 0.
# The distinct triplets are [-1,0,1] and [-1,-1,2].
# Notice that the order of the output and the order of the triplets does not matter.

def threeSum(nums):
    result = set()
    target = 0
    nums.sort()
    for i in range(len(nums) - 1):
        spointer = i + 1
        epointer = len(nums) - 1
        thirdpointer = i
        while spointer < epointer:
            if nums[spointer] + nums[epointer] + nums[thirdpointer] == target:
                result.add(tuple([nums[spointer], nums[thirdpointer], nums[epointer]]))
                spointer += 1
                epointer -= 1
            elif nums[spointer] + nums[epointer] + nums[thirdpointer] > target:
                epointer -= 1
            elif nums[spointer] + nums[epointer] + nums[thirdpointer] < target:
                spointer += 1
    return list(result)
  
print(threeSum([-1,0,1,2,-1,-4]))
print(threeSum([0,1,1]))
print(threeSum([0,0,0]))
print(threeSum([1,2,-2,-1]))