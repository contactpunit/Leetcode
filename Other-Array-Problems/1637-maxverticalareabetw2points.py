# Given n points on a 2D plane where points[i] = [xi, yi], Return the widest vertical area between
# two points such that no points are inside the area.

# A vertical area is an area of fixed-width extending infinitely along the y-axis (i.e., infinite height).
# The widest vertical area is the one with the maximum width.

# Note that points on the edge of a vertical area are not considered included in the area.

# Example 1:

# ​
# Input: points = [[8,7],[9,9],[7,4],[9,7]]
# Output: 1
# Explanation: Both the red and the blue area are optimal.
# Example 2:

# Input: points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
# Output: 3

def maxWidthOfVerticalArea(points):
    sortedPoints = sorted(points, key=lambda point: point[0])
    i = 0
    j = 1
    maxdiff = 0
    while j < len(sortedPoints):
        diff = sortedPoints[j][0] - sortedPoints[i][0]
        if diff > maxdiff:
            maxdiff = diff
        i += 1
        j += 1
    return maxdiff

points = [[8,7],[9,9],[7,4],[9,7]]
print(maxWidthOfVerticalArea(points))

points = [[3,1],[9,0],[1,0],[1,4],[5,3],[8,8]]
print(maxWidthOfVerticalArea(points))