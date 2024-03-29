# Given an array of integers arr, and three integers a, b and c. You need to find the number of good triplets.

# A triplet (arr[i], arr[j], arr[k]) is good if the following conditions are true:

# 0 <= i < j < k < arr.length
# |arr[i] - arr[j]| <= a
# |arr[j] - arr[k]| <= b
# |arr[i] - arr[k]| <= c
# Where |x| denotes the absolute value of x.

# Return the number of good triplets.

# Example 1:

# Input: arr = [3,0,1,1,9,7], a = 7, b = 2, c = 3
# Output: 4
# Explanation: There are 4 good triplets: [(3,0,1), (3,0,1), (3,1,1), (0,1,1)].
# Example 2:

# Input: arr = [1,1,2,2,3], a = 0, b = 0, c = 1
# Output: 0
# Explanation: No triplet satisfies all conditions.

def countGoodTriplets(arr, a, b, c):
    count = 0
    arrlen = len(arr)
    for i in range(0, arrlen):
        for j in range(i+1, arrlen):
            if abs(arr[i] - arr[j]) <= a:
                for k in range(j + 1, arrlen):
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                        continue
                    if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        # print(arr[i], arr[j], arr[k])
                        count += 1
    return count

arr = [3,0,1,1,9,7]
a = 7
b = 2
c = 3
print(countGoodTriplets(arr, a, b, c))

arr = [7,3,7,3,12,1,12,2,3]
a = 5
b = 8
c = 1
print(countGoodTriplets(arr, a, b, c))