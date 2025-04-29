import math

# Using For Loops

n = int(input("Please enter number : "))
sum = 1
for i in range(n):
    sum = sum + sum * i
print(sum)

# Using Built in Function

result = math.factorial(5)
print(result)

# Using Recursion

def fact(n):
    if n <= 0:
        return 1
    return n * fact(n-1)

print(fact(n))

# Looping Over 10 Factorials
fact_list = []
for i in range(1,10):
    nums = fact(i-1)
    fact_list.append(nums)

print(fact_list)