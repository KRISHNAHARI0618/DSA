def add(a,b):
    return a + b

def sub(a,b):
    return a-b

print(__name__)
if __name__=="__main__":
    print("This is simple calculator...")
    num1 = int(input("Please enter number 1:  "))
    num2 = int(input("Please enter number 2:  "))
    print(f"The addition of {num1} and {num2} is {add(num1,num2)}")
    print(f"The Subtraction for {num1} and {num2} are {sub(num1,num2)}")


