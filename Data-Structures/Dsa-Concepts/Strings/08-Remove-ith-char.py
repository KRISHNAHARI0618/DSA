print("Pedddireddy")


# Remove ith Char from name
# 1: string 
# 2: Convert to Array 
# 3: check for index and remove it with " "
name = "peddireddy hari vardhan reddy"

arr = []*len(name)
for i in range(0,len(name)):
    if i == 5 and i == 10 and i == 15:
        arr.append(name[i]==" ")
    else:
        arr.append(name[i])
print(arr)

newString = "".join(filter(lambda a : a != 'd',name))
print(newString)

# Filter will take two arguments func and iterable

# filter(func,iterable(list,string,func, tuple))

def even(n):
    return n % 2 == 0

list1 = [1,2,3,4,5,6,7]
addition = filter(even,list1)
print(list(addition))

a = [1,2,3]
b = [4,5,6]

pairs = filter(lambda pair : pair[-1] + pair[-1] > 6,zip(a,b))
print(list(pairs))


# Usage of Lambda Function
a = "peddireddy"
newString = lambda a : a.upper() 
print(newString(a))

# Filter Function will Take only one parameter by default


# Wrapper Function or Decorators Function 
# Takes One input as a function and returns another function which adds features of the calling function

def decorators(func)-> any:
    def wrapper()-> any:
        print("Before Calling Decorator .....")
        func()
        print("After Calling Decorator Function .... ")
    return wrapper

@decorators
def hello()-> any:
    print("Heyy Hii Namaskaram")

hello()

# Lambda to Multiple Two Lists

a = [2,4,6]
b = [7,3,1]

multipliedList = list(map(lambda a,b : a * b , a,b))

print(multipliedList)
