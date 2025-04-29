import string


num = int(input("Please enter your number : "))

for i in range(0,num):
    for j in range(0,num):
        if i==0 or j==(num-1) or i==j:
            print("*",end=" ")
        else:
            print(" ",end=" ")
    print()

name = "peddireddy"

length = len(name)

for i in range(length):
    for j in range(i+1):
        print(name[j],end=" ")
    print()
# Last element in array will get excluded
    

