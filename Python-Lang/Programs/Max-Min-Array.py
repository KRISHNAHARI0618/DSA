print("Minimum Number and Maximum Number ...")

list = [2,9,6,8,4,5,3]

print(list)

max = list[0]
for i in list:
    if i < max:
        max = i
print(max)
