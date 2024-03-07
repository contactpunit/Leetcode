# Given an integer array nums and an integer k, return the number of pairs (i, j)
# where i < j such that |nums[i] - nums[j]| == k.

# The value of |x| is defined as:

# x if x >= 0.
# -x if x < 0.

# Example 1:

# Input: nums = [1,2,2,1], k = 1
# Output: 4
# Explanation: The pairs with an absolute difference of 1 are:
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# - [1,2,2,1]
# Example 2:

# Input: nums = [1,3], k = 3
# Output: 0
# Explanation: There are no pairs with an absolute difference of 3.
# Example 3:

# Input: nums = [3,2,1,5,4], k = 2
# Output: 3
# Explanation: The pairs with an absolute difference of 2 are:
# - [3,2,1,5,4]
# - [3,2,1,5,4]
# - [3,2,1,5,4]
 
def countKDifference(nums, k):
    # using O(n) time complexity
    counter = 0
    hashmap = {}
    for elem in nums:
        if elem not in hashmap:
            hashmap[elem] = 1
        else:
            hashmap[elem] += 1
    for elem in nums:
        lowerdiff = elem - k
        if lowerdiff in hashmap:
            counter += hashmap[lowerdiff]
    return counter
        
        

nums = [1,2,2,1]
k = 1
print(countKDifference(nums, k))

nums = [3,2,1,5,4]
k = 2
print(countKDifference(nums, k))

nums = [7,7,8,3,1,2,7,2,9,5]
k = 6
print(countKDifference(nums, k))
