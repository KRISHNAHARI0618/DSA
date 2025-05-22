# Using List Python Sort
# Command To see tree structures tree -aI <Path>

def KthLargest(arr,k):
    arr.sort(reverse=True)
    res = arr[:k]
    return res

def Kthsmallest(arr,k):
    arr.sort()
    res = arr[:k]
    return res

if __name__ == "__main__":
    arr = [1,4,0,3,5,8,9,2,6,7]
    k = 3
    res = KthLargest(arr,k)
    print(','.join(map(str,res)))
    res1 = Kthsmallest(arr,k)
    print(','.join(map(str,res1)))