import sys


dict1 = {}
print(dict1)

dict1 = dict(name='hari',age=20)
print(dict1)

dict2 = [('name','akhila'),('age',25),('year',2025)]
print(dict(dict2))

dict3= dict1|dict(dict2)
print(dict3)

class a:
    def add(a,b):
        print(a+b)

a1 = a()
a2 = a()
a3 = a()

a4 = sys.getrefcount(a)
print(a4)

myDict = {'name':'hari','age':25,'year':2025}
print(myDict)

for key in myDict:
    print(key,myDict[key])

name1 = {}

# From keys
# Copy dictionary
# get method 
# items

for key,value in dict3.items():
    print(key,value)

list1 = dict3.values()
print(list1)

a = 0b0101
b = 4
c = a + b
print(c)