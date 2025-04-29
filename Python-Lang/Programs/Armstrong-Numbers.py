print("Peddireddy Hari Vardhan Reddy ")

print("Congratulation on learning Python Programs...")

def armstrong(x):
    temp = x
    sum = 0 
    while x != 0:
        r = x % 10
        sum = sum + r * r * r
        x = x // 10
    return temp == sum

print(armstrong(100))
arm_list = []
for i in range(0,10000):
    if armstrong(i) == True:
        arm_list.append(i)
print(arm_list)
