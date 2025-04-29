def selectSort(list):
    for i in range(len(list)-1):
        minIndex = i
        for j in range(i+1,len(list)):
            if list[j] < list[minIndex]:
                minIndex = j
        if i != minIndex:
            list[i],list[minIndex] = list[minIndex] ,list[i]
    return list

list = [6,5,3,4,2,1]
# list = [1,2,3,4,5,6]
print(selectSort(list))