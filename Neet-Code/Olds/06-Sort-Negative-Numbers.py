list = [-12,-34,4,-3,7,9,1]
# print(sorted(list))

def move(arr):
    j = 0
    for i in range(len(arr)):
        if arr[i] < 0:
            arr[i],arr[j] = arr[j],arr[i]
            j = j +1
    return arr


print(move(list))