# On a 2D plane, there are n points with integer coordinates points[i] = [xi, yi]. 
# Return the minimum time in seconds to visit all the points in the order given by points.

# You can move according to these rules:

# In 1 second, you can either:
# move vertically by one unit,
# move horizontally by one unit, or
# move diagonally sqrt(2) units (in other words, move one unit vertically then one unit horizontally in 1 second).
# You have to visit the points in the same order as they appear in the array.
# You are allowed to pass through points that appear later in the order, but these do not count as visits.

# Example 1:


# Input: points = [[1,1],[3,4],[-1,0]]
# Output: 7
# Explanation: One optimal path is [1,1] -> [2,2] -> [3,3] -> [3,4] -> [2,3] -> [1,2] -> [0,1] -> [-1,0]   
# Time from [1,1] to [3,4] = 3 seconds 
# Time from [3,4] to [-1,0] = 4 seconds
# Total time = 7 seconds
# Example 2:

# Input: points = [[3,2],[-2,2]]
# Output: 5

def minTimeToVisitAllPoints(points):
    i = 0
    j = i + 1
    steps = 0
    ptlen = len(points)
    while j < ptlen:
        idx0diff = abs(points[j][0] - points[i][0])
        idx1diff = abs(points[j][1] - points[i][1])
        steps += min(idx0diff, idx1diff)
        remain = idx1diff - idx0diff if idx1diff - idx0diff >= 0 else idx0diff - idx1diff
        steps += idx1diff - idx0diff if idx1diff - idx0diff >= 0 else idx0diff - idx1diff
        i += 1
        j += 1
    return steps

points = [[1,1],[3,4],[-1,0]]
print(minTimeToVisitAllPoints(points))

points = [[3,2],[-2,2]]
print(minTimeToVisitAllPoints(points))