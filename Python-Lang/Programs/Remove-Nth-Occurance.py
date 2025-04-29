print("Printing Nth Occurence Removing ...")

list = ["geeks","for","geeks","for","peddireddy"]

print(list)
n = 2
count = 0
words = ["geeks","for"]
for i in range(0,len(list)-1):
    if list[i] in words:
        count = count + 1
        if count  == n:
            del list[i]

print(list)