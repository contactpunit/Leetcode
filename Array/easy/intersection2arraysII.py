# Given two integer arrays nums1 and nums2, return an array of their intersection. 
# Each element in the result must appear as many times as it shows in both arrays and you
# may return the result in any order.

# Example 1:

# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2,2]
# Example 2:

# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [4,9]
# Explanation: [9,4] is also accepted.
from collections import Counter

def intersect(nums1, nums2):
    counthash = Counter()
    nums1.sort()
    nums2.sort()
    i = j = 0
    while i < len(nums1) and j < len(nums2):
        if nums1[i] == nums2[j]:
            counthash[nums1[i]] += 1
            i += 1
            j += 1
        elif nums1[i] < nums2[j]:
            i += 1
        elif nums1[i] > nums2[j]:
            j += 1
    return [k for k, v in counthash.items() for i in range(v)]

nums1 = [1,2,2,1]
nums2 = [2,2]
print(intersect(nums1, nums2))

nums1 = [4,9,5]
nums2 = [9,4,9,8,4]
print(intersect(nums1, nums2))