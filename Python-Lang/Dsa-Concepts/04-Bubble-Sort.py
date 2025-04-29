def bubbleSort(myList):
    for i in range(len(myList)-1,0,-1):
        for j in range(i):
            if myList[j] > myList[j+1]:
                # temp = myList[j]
                # myList[j]  = myList[j+1]
                # myList[j+1] = temp
                myList[j],myList[j+1] = myList[j+1],myList[j]
    return myList
        
list = [2,7,9,4,3,5]

print(bubbleSort((list)))

