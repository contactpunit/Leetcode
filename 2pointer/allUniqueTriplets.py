# given an array of unsorted numbers, find all
# unique triplet in that, that add upto target 0
# [-3, 0, 1, 2, -1, 1, -2]
#answer -> [[-3, 1, 2] , [-2, 0, 2] , [-1, 0, 1] , [-2, 1, 1]]

inputArray = [-3, 0, 1, 2, -1, 1, -2]
target = 0

matches = []

def findAllTriplets(arr, target):
    arr.sort()
    for idx, _ in enumerate(arr):
        left = idx
        right = len(arr) - 1
        startposition = left + 1
        while left < right:
            if arr[left] + arr[right] + arr[startposition] == target:
                matches.append((arr[left], arr[right], arr[startposition]))
                left += 1
                right -= 1
            elif arr[left] + arr[right] + arr[startposition] > target:
                right -= 1
            elif arr[left] + arr[right] + arr[startposition] < target:
                left += 1
    print(matches)

findAllTriplets(inputArray, target)