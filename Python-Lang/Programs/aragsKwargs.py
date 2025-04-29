def demo(*args, **kwargs):
    print("Args:", args)
    print("Kwargs:", kwargs)

demo(1, 2, 3, name="Akhila", role="DevOps")

# Lambda Function:

square = lambda x : x*x
print(square(10))

# Decorator:

def decorator(func):
    def wrapper():
        print("Calling before function ....")
        func()
        print("Calling after function....")
    return wrapper

@decorator
def simpleFunc():
    print("Calling My Func Original ......")
    
simpleFunc()

# Joining two dictionaries

dict1 = {'name':'hari','age': 20}
dict2 = {'name':'simba','age':30}

print(dict1|dict2)

# Map Function
MapDef = map(lambda a : a*a , [1,2,3,4])
print(list(MapDef))

# Filter Function
filterFunc = filter(lambda a : a > 2, [2,3,4,5])
print(list(filterFunc))
