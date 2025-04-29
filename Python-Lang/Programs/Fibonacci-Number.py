print("Printing Fibonacci Numbers ....")

# Fibonacci Numbers ..

n1 = 0
n2 = 1
print(n1,n2)
fib_list = []
fib_list.append(n1)
fib_list.append(n2)
for i in range(2,20):
    sum = n1+n2
    print(sum,end=" ")
    fib_list.append(sum)
    n1 = n2
    n2 = sum
print()
print(fib_list)


first = 0
second = 1
for i in range(10):
    print(first,end=" ")
    temp = first  
    first = second
    second = temp + second
print()
recFib = []
def fibona(n):
    if n in [0,1]:
        return n
    else:
        return fibona(n-1)+fibona(n-2)
print("Fibonacci..")
print(fibona(10))
