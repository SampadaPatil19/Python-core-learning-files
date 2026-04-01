def maxElement(li):
    max_item = li[0]
    for item in li:
        if ( max_item < li[item] ):
            max_item = li[item]
        return max_item

li = [12, 69, 34, 23, 54, 66]
result = maxElement(li)
print(f'Maximum element is {result}')