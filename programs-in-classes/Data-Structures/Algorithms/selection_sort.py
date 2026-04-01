def selectionSort(li):
    for i in range(len(li)):
        min = i
        for j in range(i+1, len(li)):
            if li[min] > li[j]:
                min = j
            li[i], li[min] = li[min], li[i]

    return li

li = [60, 50, 40, 30, 20, 10]
result = selectionSort(li)
print(result)