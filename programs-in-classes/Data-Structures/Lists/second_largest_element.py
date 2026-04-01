# find the second largest element in list

def secondLarge(li):
    max_item = li[0]
    sec_max = 0
    for i in li:
        if i > max_item:
            sec_max = max_item
            max_item = i
        
        elif i > sec_max  :
            sec_max = i
    
    return sec_max

li = [78, 59, 23, 79, 90]
print(secondLarge(li))