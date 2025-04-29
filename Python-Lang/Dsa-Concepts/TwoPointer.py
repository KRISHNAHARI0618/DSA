from itertools import count


class solution:
    def twopinter(self,numbers,target):
        left = 0
        right = len(numbers) - 1

        while left < right:
            numbers.sort()
            sum = numbers[left]+numbers[right]
            if sum == target:
                return [left+1,right+1]
            elif sum < target:
                left += 1
            else:
                right = right - 1

obj = solution()
list = [7,15,16,2,3,8]
target = 18
list2 = obj.twopinter(list,target)
print(list2)


class Binary_Search:
    def Binary_Search_Method(self,elements,target):
        left = 0
        right = len(elements) - 1

        while left < right:
            mid = (left + right) // 2
            if elements[mid] < target :
                left = mid + 1
            elif elements[mid] > target:
                right = mid - 1
            else:
                return mid
        return -1


obj = Binary_Search()
list1 = [2,3,4,5,6,10,8,9]
target = 10

obj2 = obj.Binary_Search_Method(list1,target)
print(obj2)


class TwoPointer:
    def TwoPointerMethod(self,elements,target):
        left = 0
        right = len(elements)-1

        while left < right:
            sum = elements[left] + elements[right]
            if sum == target:
                return [left,right]
            elif sum < target:
                left += 1
            else:
                right -= 1

TwoPointerObject = TwoPointer()

elements  = [5,6,1,8,7,3,2,9,3]
target = 10
Found = TwoPointerObject.TwoPointerMethod(elements,target)

print()

def main():
    print("Peddireddy")
print(Found)

main()





