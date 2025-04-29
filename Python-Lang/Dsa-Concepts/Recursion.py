# It is recursive method 

def factorial(n : any) -> any:
    if n ==1:
        return 1
    return n * factorial(n-1)

print(factorial(5))