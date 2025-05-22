from xml.sax.handler import property_interning_dict


arr = [1,2,3,4,5]
print(arr)

def rotate(arr):
    lastElement = arr[-1]
    for i in range(len(arr)-1,0,-1):
        arr[i] = arr[i-1]
    arr[0] = lastElement
if __name__ == "__main__":
    rotate(arr)
    for i in range(0,len(arr)):
        print(arr[i],end=" ")

