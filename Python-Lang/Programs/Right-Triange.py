n = int(input("Please enter the number : "))

for i in range(n,0,-1):
    for j in  range(1,i+1):
        print(i,end=" ")
    print()

num = 10
count = 1
pm_list = []
for i in range(1,num+1):
    if num % i == 0:
        count = count + 1
        pm_list.append(i)
if count > 3:
    print("Non Prime Number")
    print(pm_list)
else:
    print("Prime Number")
    print(pm_list)
