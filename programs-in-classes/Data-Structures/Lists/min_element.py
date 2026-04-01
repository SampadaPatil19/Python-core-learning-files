# homework - WAP to find out the minimum element from the given list.

def minElement(li):
    min_item = li[0]
    for item in li:
        if min_item > item:
            min_item = item
    return min_item

li = [12, 45, 64, 7, 23, 44]
print(minElement(li))