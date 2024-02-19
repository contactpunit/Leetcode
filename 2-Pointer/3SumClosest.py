# Given an integer array nums of length n and an integer target,

# find three integers in nums such that the sum is closest to target.

# Return the sum of the three integers.

# You may assume that each input would have exactly one solution.

 

# Example 1:

# Input: nums = [-1,2,1,-4], target = 1
# Output: 2
# Explanation: The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).
# Example 2:

# Input: nums = [0,0,0], target = 1
# Output: 0
# Explanation: The sum that is closest to the target is 0. (0 + 0 + 0 = 0).
 

# Constraints:

# 3 <= nums.length <= 500
# -1000 <= nums[i] <= 1000
# -104 <= target <= 104

def threeSumClosest(nums, target: int):
    nums.sort()
    closest = 1000
    if len(nums) == 3:
        return sum(nums)
    for i in range(len(nums) - 1):
        moving = i
        left = i + 1
        right = len(nums) - 1
        while left < right and moving != right:
            if (nums[left] + nums[right] + nums[moving]) == target:
                return nums[left] + nums[right] + nums[moving]
            if abs(target - (nums[left] + nums[right] + nums[moving])) < closest:
                closest =  abs(target - (nums[left] + nums[right] + nums[moving]))
                closestPair = [nums[left], nums[moving], nums[right]]
                if target > 0:
                    left += 1
                else:
                    right -= 1
            elif abs(target - (nums[left] +nums[right] + nums[moving])) > closest:
                closest =  abs(target - (nums[left] + nums[right] + nums[moving]))
                closestPair = [nums[left], nums[moving], nums[right]]
                if target > 0:
                    right -= 1
                else:
                    left += 1
            else:
                if target > 0:
                    left += 1
                else:
                    right -= 1
    return sum(closestPair)

    
# print(threeSumClosest([-1,2,1,-4], 1))
# print(threeSumClosest([0,0,0], 1))
# print(threeSumClosest([0,1,2], 0))
# print(threeSumClosest([1,1,1,0], 100))
print(threeSumClosest([1,1,0,1], 2))
# print(threeSumClosest([4,0,5,-5,3,3,0,-4,-5], -2))