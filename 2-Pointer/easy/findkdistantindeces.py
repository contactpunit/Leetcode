# You are given a 0-indexed integer array nums and two integers key and k. 
# A k-distant index is an index i of nums for which there exists at least one index j
# such that |i - j| <= k and nums[j] == key.

# Return a list of all k-distant indices sorted in increasing order.

 

# Example 1:

# Input: nums = [3,4,9,1,3,9,5], key = 9, k = 1
# Output: [1,2,3,4,5,6]
# Explanation: Here, nums[2] == key and nums[5] == key.
# - For index 0, |0 - 2| > k and |0 - 5| > k, so there is no j where |0 - j| <= k and nums[j] == key. 
# Thus, 0 is not a k-distant index.
# - For index 1, |1 - 2| <= k and nums[2] == key, so 1 is a k-distant index.
# - For index 2, |2 - 2| <= k and nums[2] == key, so 2 is a k-distant index.
# - For index 3, |3 - 2| <= k and nums[2] == key, so 3 is a k-distant index.
# - For index 4, |4 - 5| <= k and nums[5] == key, so 4 is a k-distant index.
# - For index 5, |5 - 5| <= k and nums[5] == key, so 5 is a k-distant index.
# - For index 6, |6 - 5| <= k and nums[5] == key, so 6 is a k-distant index.
# Thus, we return [1,2,3,4,5,6] which is sorted in increasing order. 
# Example 2:

# Input: nums = [2,2,2,2,2], key = 2, k = 2
# Output: [0,1,2,3,4]
# Explanation: For all indices i in nums, there exists some index j such that
# |i - j| <= k and nums[j] == key, so every index is a k-distant index. 
# Hence, we return [0,1,2,3,4].
 
def findKDistantIndices(nums, key, k):
    if len(nums) == 1:
        return [0]
    else:
        validIndexes = [idx for idx, elem in enumerate(nums) if elem == key]
        start= 0
        if len(validIndexes) == 0:
            return []
        elif len(validIndexes) == len(nums):
            return list(range(len(nums)))
        else:
            output = []
            for idx in validIndexes:
                output += range(max(start, idx - k), min(idx + k + 1, len(nums)) )
                start = idx + k + 1
            return list(output)

nums = [3,4,9,1,3,9,5]
key = 9
k = 1
print(findKDistantIndices(nums, key, k))

nums = [2,2,2,2,2]
key = 2
k = 2
print(findKDistantIndices(nums, key, k))

nums = [1,1000,1,1000]
key = 1000
k = 4
print(findKDistantIndices(nums, key, k))

