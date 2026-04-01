"""
Requirements:
1. no duplicate elements are allowed

How it worked:
- compare 2 elements until 1st element is greater than 2nd element
- Then swap 1st element with 2nd element

- Max element will be at its position first.
    - if out for loop executes 5 times like 5, 4, 3, 2, 1
    - then inner for loop will executes 4, 3, 2, 1
"""

def bubbleSort(li):
    size = len(li)
    for i in range(1, size):
        for j in range(0, size-i):
            if li[j] > li[j+1]:
                li[j], li[j+1] =  li[j+1], li[j] 
            print(li)
            # print(li[j+1])

li = [60, 50, 40, 30, 20, 10]
result = bubbleSort(li)
print(result)