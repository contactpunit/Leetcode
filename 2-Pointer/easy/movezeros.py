
# Given an integer array nums, move all 0's to the end of it while maintaining the 
# relative order of the non-zero elements.

# Note that you must do this in-place without making a copy of the array.

# Example 1:

# Input: nums = [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Example 2:

# Input: nums = [0]
# Output: [0]

def moveZeroes(nums):
    start = 0
    size = len(nums)
    for elem in nums:
        if elem != 0:
            nums[start] = elem
            start += 1
    while start < size:
        nums[start] = 0
        start += 1
    print(nums)

nums = [0,1,0,3,12]
moveZeroes(nums)
nums = [0,1,0,0,0]
moveZeroes(nums)
nums = [0,1,2,0,4]
moveZeroes(nums)
nums = [4,1,2,8, 6,9,0,0,0,0,0,0,3,4,4,4,4]
moveZeroes(nums)
nums = [-53760,84068,-16069,72746,58690,-71149,-22950,-12274,96637,-81284,-39127,-49651,-17647,58022,-44789,58691,-16147,-14319,14896,895,57955,27033,-70106,68552,8416,-77243,-35301,27253,95595,-27195,-8996,-17886,98974,-39038,-99612,-92071,-11299,3482,-53441,-9649,-65402,40503,-17338,-64641,-7897,-94005,-80726,0,-96691,-47830,-13500,-18458,-51458,16976,-4899,63670,-76323,91906,-51742,95588,83634,28742,-66729,-82026,14786,0,-52143,83663,20022,-52850,-92499,-74631,33067,17901,-22932,-26561,-25170,89490,95464,60769,16495,44798,-19605,3128,-67702,4839,-58592,74850,89144,23899,-9077,-58725,-83740,-82577,6516,61472,0,-50701,0,-31098]
moveZeroes(nums)
