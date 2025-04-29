def swap(num1,num2):
    num1,num2 = num2,num1
    return num1,num2
print(swap(10,20))



def qs(arr,low,high):
    if low < high:
        pIndex = partition(arr,low,high)
        qs(arr,low,pIndex-1)
        qs(arr,pIndex+1,high)

def partition(arr,low,high):
    pivot = arr[low]
    i = low
    j = high
    while i < j:
        while arr[i] <= pivot and i <= high -1:
            i = i+1
        while arr[j] > pivot and j >= low+1:
            j = j - 1
        if i < j :
            swap(arr[i],arr[j])
    swap(arr[low],arr[j])
    return j

def quickSort(arr):
    qs(arr,0,len(arr)-1)
    return arr

arr = [4,2,1,3,5,9,8,6,7]
print(quickSort(arr))
print()