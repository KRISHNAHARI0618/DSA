def insertionSort(list):
    for i in range(1,len(list)):
        temp = list[i]
        j = i - 1
        while temp < list[j] and j > -1: # 6 < 6 and j = 0 4 < 6 
            list[j+1] = list[j] # list[1] = 6 , list[2] = 6
            list[j] = temp # list[0] = 6
            j = j - 1
    return list

list = [6,5,4,3,2,1]
print(insertionSort(list))