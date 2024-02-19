# given an array of unsorted numbers, find a
# unique triplet in that, that add upto 0
# [-3, 0, 1, 2, -1, 1, -2]
#answer -> [[-3, 1, 2] or [-2, 0, 2] or [-1, 0, 1] or [-2, 1, 1]]

def uniqTriplets(arrayOfnums, target=0):
    arrayOfnums.sort() # sort the numbers so they have relation
    result = []
    sPointer = 1
    ePointer = len(arrayOfnums) - 1
    movingPointer = 0
    
    for _ in arrayOfnums:
        while sPointer < ePointer:
            if arrayOfnums[sPointer] + arrayOfnums[ePointer] + arrayOfnums[movingPointer] == target:
                result.append((arrayOfnums[sPointer], arrayOfnums[ePointer], arrayOfnums[movingPointer]))
                sPointer += 1
                ePointer -= 1
            elif arrayOfnums[sPointer] + arrayOfnums[ePointer] + arrayOfnums[movingPointer] > target:
                ePointer -= 1
            elif arrayOfnums[sPointer] + arrayOfnums[ePointer] + arrayOfnums[movingPointer] < target:
                sPointer+= 1
        movingPointer += 1
    return result

numList = [-3, 0, 1, 2, -1, 1, -2]
print(uniqTriplets([-3, 0, 1, 2, -1, 1, -2]))