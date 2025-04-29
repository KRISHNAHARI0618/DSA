# Fibonacci Series 0 1 1 2 3 5 8 13 21 34

def fibonacci(n):
    if n < 0:
        return f"{n} is not Correct Number"
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = 20
s = fibonacci(-2)
print(s)

for i in range(0,10):
    print(fibonacci(i),end=" ")
print()

print(type('|'))



a ,b = 0,1
for _ in range(10):
    print(a,end=" ")
    a ,b = b , a+b
print()

    