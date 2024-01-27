# Given an array of integers nums, half of the integers in nums are odd, and the other half are even.

# Sort the array so that whenever nums[i] is odd, i is odd, and whenever nums[i] is even, i is even.

# Return any answer array that satisfies this condition.

 

# Example 1:

# Input: nums = [4,2,5,7]
# Output: [4,5,2,7]
# Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.
# Example 2:

# Input: nums = [2,3]
# Output: [2,3]

def sortArrayByParityII(nums):
    starteven = 0
    endodd = len(nums) - 2 if len(nums) - 1 % 2 == 0 else len(nums) - 1 % 2
    while starteven <= len(nums) - 1 and endodd >= 0:
        if nums[starteven] % 2 != 0:
            if nums[endodd] % 2 == 0:
                nums[starteven], nums[endodd] = nums[endodd], nums[starteven]
                starteven += 2
                endodd -= 2
            else:
                endodd -= 2
        elif nums[starteven] % 2 == 0:
            starteven += 2
    return nums

nums = [4,2,5,7]
sortArrayByParityII(nums)
nums = [2,3]
sortArrayByParityII(nums)