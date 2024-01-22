# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same. Then return the number of unique elements in nums.

# Consider the number of unique elements of nums to be k, to get accepted, you need to do the following things:

# Change the array nums such that the first k elements of nums contain the unique elements in the order they were present in nums initially.
# The remaining elements of nums are not important as well as the size of nums.
# Return k.
# Custom Judge:

# The judge will test your solution with the following code:

# int[] nums = [...]; // Input array
# int[] expectedNums = [...]; // The expected answer with correct length

# int k = removeDuplicates(nums); // Calls your implementation

# assert k == expectedNums.length;
# for (int i = 0; i < k; i++) {
#     assert nums[i] == expectedNums[i];
# }
# If all assertions pass, then your solution will be accepted.

 

# Example 1:

# Input: nums = [1,1,2]
# Output: 2, nums = [1,2,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 1 and 2 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
# Example 2:

# Input: nums = [0,0,1,1,1,2,2,3,3,4]
# Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums being 0, 1, 2, 3, and 4 respectively.
# It does not matter what you leave beyond the returned k (hence they are underscores).
 
def removeDuplicates(nums):
    posReplace = 1
    i = 1
    while i < len(nums):
        if nums[posReplace] <= nums[posReplace -1]:
            if nums[i] > nums[posReplace -1]:
                nums[posReplace] = nums[i]
                i += 1
                posReplace += 1
            else:
                i += 1
        else:
            i += 1
            posReplace += 1
    return posReplace, nums  
    

nums = [0,0,1,1,1,2,2,3,3,4]
print(removeDuplicates(nums))
nums = [1,1,2]
print(removeDuplicates(nums))
nums = [1,2]
print(removeDuplicates(nums))
nums = [1,2,2]
print(removeDuplicates(nums))
nums = [1,2,3]
print(removeDuplicates(nums))
nums = [-50,-49,-48,-46,-46,-44,-44,-44,-44,-43,-43,-43,-42,-42,-41,-40,-39,-39,-38,-38,-37,-35,-34,-33,-31,-31,-30,-30,-28,-28,-27,-25,-22,-22,-22,-22,-22,-21,-21,-21,-21,-19,-18,-17,-17,-16,-16,-15,-15,-14,-13,-13,-10,-10,-9,-9,-8,-7,-7,-7,-7,-6,-5,-4,-4,-4,-4,-3,-3,-2,-2,-2,0,0,1,2,2,2,3,3,4,5,5,5,7,8,8,8,10,10,14,15,16,16,18,18,19,21,23,23,24,24,24,25,25,25,26,27,28,28,30,32,32,32,34,36,37,37,37,38,38,38,39,40,40,40,41,41,43,43,43,44,45,46,46,47,48,48,50,50,50]
print(removeDuplicates(nums))

