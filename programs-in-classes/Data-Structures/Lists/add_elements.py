
def sumOfElements(list):
    sum = 0 

    for row in li:
        for num in row:
            sum += num
    return sum

li = [[10, 20], [30, 40], [50, 60]]
# li = [10, 20, [30, 40], 50, 60]

print(sumOfElements(li))


