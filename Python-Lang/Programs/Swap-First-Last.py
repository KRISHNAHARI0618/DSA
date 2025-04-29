print("Swapping First and Last Number ....")

list = [3,8,1,5,9,4,6,2]

list[0],list[-1] = list[-1],list[0]
print(list)

start,*middle,end=list
print(start)
print(middle)
print(end)
list = [end,middle,start]

