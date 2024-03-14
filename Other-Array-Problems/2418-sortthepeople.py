# You are given an array of strings names, and an array heights that consists of distinct 
# positive integers. Both arrays are of length n.

# For each index i, names[i] and heights[i] denote the name and height of the ith person.

# Return names sorted in descending order by the people's heights.

# Example 1:

# Input: names = ["Mary","John","Emma"], heights = [180,165,170]
# Output: ["Mary","Emma","John"]
# Explanation: Mary is the tallest, followed by Emma and John.
# Example 2:

# Input: names = ["Alice","Bob","Bob"], heights = [155,185,150]
# Output: ["Bob","Alice","Bob"]
# Explanation: The first Bob is the tallest, followed by Alice and the second Bob.

def sortPeople(names, heights):
    # uw/o using sort or python lib functions
    matchMap = dict(zip(names, heights))
    nameslen = len(names)
    for i in range(1, nameslen):
        print(i)
        if matchMap[names[i - 1]] < matchMap[names[i]]:
            names[i -1], names[i] = names[i], names[i -1]
    return names

names = ["Mary","John","Emma"]
heights = [180,165,170]
print(sortPeople(names, heights))