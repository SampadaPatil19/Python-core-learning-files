"""
requiremnets
1. data list should be same
2. no duplicate allowed
"""

def binarySearch(li, element):
    beg = 0
    end = len(li) - 1

    while (beg<=end):
        mid = (beg + end) // 2
        if li[mid] == element:
            return mid
        elif element < li[mid]:
            end = mid - 1
        else:
            beg = mid + 1
    return -1

li = [25, 26, 39, 55, 70, 89]
element = 26
print(binarySearch(li, element))

# Binary Search using Recursion
def binarySearchRec(li, beg, end, element):
    if beg > end:
        return -1
    mid = (beg + end) // 2
    if li[mid] == element:
        return mid
    elif element < li[mid]:
        return binarySearchRec(li, beg, mid - 1, element)
    else:
        return binarySearchRec(li, mid + 1, end, element)
    
li = [25, 26, 39, 55, 70, 89]
element = 26
print(binarySearch(li, element))