import math

def power(x,y):
    if y == 0:
        return 1
    if y % 2 == 0:
        return power(x,y//2)*power(x,y//2)
    return x * power(x,y//2)*power(x,y//2)
# Logic Building
    # power(4,4)*power(4,4)
      # power(4,2)*power(4,2)
        # power(4,1)*power(4,1)
          # x * power(4,1) * power(4,1) == 4 * 4 
            # x * power(4,0.5)*power(4,0.5) == 4 * 4 * 4 * 4 == 256
              # x * power(4,0) * power(4,0)  == 4 
                # x * 1 * 1 == 4 * 1 * 1
powNum = power(4,2)
print(powNum)

# Find the order of Function
def order(num):
    n = 0
    while num != 0:
        n = n + 1
        num = num // 10
    return n
print(order(1234))

print(1//2)

def is_armstrong(x):
    n = order(x)
    temp ,total = x,0
    while temp != 0:
        r = temp % 10
        total = total + power(r,n)
        temp = temp // 10
    return total == x

if __name__ == "__main__":
    x = 153
    print(is_armstrong(x))
    x = 456
    print(is_armstrong(x))


digit = int(math.log10(2346)+1)
print(digit)


def armstrongNumber(n):
    number = str(n)
    length = len(number)
    output = sum(int(i) ** length for i in number)

    return "True" if output == n else "False"

if __name__ == "__main__":
    print(armstrongNumber(153))
    print(armstrongNumber(3456))

def armstrong(n):
    number = str(n)
    n = len(number)
    output = 0
    for i in number:
        output = output + int(i) ** n

    return output == int(number)


if __name__=="__main__":
    arm_list = []
    for i in range(10,20000):
        if armstrong(i):
            arm_list.append(i)
    print(arm_list)


print(2**2)
print(4**4)

