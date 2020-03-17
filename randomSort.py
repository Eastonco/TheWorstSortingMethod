import time
import random
random.seed()

# The worst sorting method of all time
# Randomly generates indecies and checks if the list is in order
# Probably has a execution time of n!
def sortThis(arr):
    start = time.time()
    tmp = arr.copy()
    while(not isInOrder(tmp)):
        indecies = newIndecies(tmp)
        for index, val in enumerate(indecies):
            tmp[index] = arr[val]
    print("Sorted! It took", (round((time.time() - start), 5)) , "Seconds to run")
    return tmp


# Generates new array of indecies given an array of values
# No duplicate indicies will be in the return array
def newIndecies(arr):
    tmp = [None] * len(arr)
    while isDupes(tmp):
        for index, val in enumerate(arr):
            tmp[index] = random.randrange(len(arr))
    return tmp


# Accepts an array
# Returns True if duplicates exists, False otherwise
def isDupes(arr):
    tmp = []
    for val in arr:
        if val in tmp:
            return True
        tmp.append(val)
    return False


# Accepts the array to be sorted
# Returns True if it's sorted from Smallest -> Greatest
# False otherwise
def isInOrder(arr):
    index = 0
    for val in arr:
        if(index > 0):
            if not (arr[index -1] < val):
                return False
        index += 1
    return True