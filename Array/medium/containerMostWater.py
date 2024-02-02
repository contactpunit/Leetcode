# You are given an integer array height of length n. 
# There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

# Find two lines that together with the x-axis form a container, 
# such that the container contains the most water.

# Return the maximum amount of water a container can store.

# Notice that you may not slant the container.

# Example 1:


# Input: height = [1,8,6,2,5,4,8,3,7]
# Output: 49
# Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. 
# In this case, the max area of water (blue section) the container can contain is 49.
# Example 2:

# Input: height = [1,1]
# Output: 1
 
def maxArea(height):
    start = 0
    end = len(height) - 1
    area = 0
    while start < end:
        temparea = min(height[end], height[start]) * (end - start)
        if temparea > area:
            area = temparea
        if height[start] < height[end]:
            start += 1
        elif height[start] > height[end]:
            end -= 1
        else:
            start += 1
            end -= 1
    return area
        

height = [1,8,6,2,5,4,8,3,7]
maxArea(height)
height = [1,1]
maxArea(height)

