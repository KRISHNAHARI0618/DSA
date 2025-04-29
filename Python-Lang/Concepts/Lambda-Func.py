'''
Lambda Function is a anonymous function which does not have any name
lambda keyword is used to define the function
syntax: lambda arguments/functions : expression
'''
s = "peddireddy hari vardhan reddy"
c = lambda func : func.upper() 
print(c(s))

n = lambda x : "positive" if x > 0 else "nagative"

print(n(10))