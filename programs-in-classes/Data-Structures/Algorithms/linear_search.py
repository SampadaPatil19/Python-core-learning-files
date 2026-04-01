def linerSearch(li, searchEle):
    for index in range(0, len(li)):
        if (li[index] == searchEle):
            return index

    else:
        return -1

li = [78, 28, 45, 26, 90]
ele =26
result = (linerSearch(li, ele))

if linerSearch(li,ele):
    print(f'{ele} is present at index {result}')
else:
    print(f'{ele} is not present list.')

"""
TimeComplexity 
Best - O(1)
Worst - O(n)
Average - O(n//2) => O(n)

"""