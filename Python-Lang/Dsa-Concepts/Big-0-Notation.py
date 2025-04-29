import os
import platform

print(" starts '''''''''''''''  starts  ")

print()

print(os.name)
print(os.uname().release)

print(platform.machine())
print(platform.node())
print()
print("Learning DSA Concepts ..... ")

class stack:
    def __init__(self):
        self.items= []

    def is_empty(self):
        return not self.items
    
    def push(self,item):
        return self.items.append(item)

    def pop(self):
        return self.items[-1]
    
    def peek(self):
        return self.items[-1]
    
    def __str__(self):
        return str(self.items)

if __name__ == "__main__":
    s = stack()
    print(s.is_empty())

    s.push(3)
    s.push(3)
    s.push(3)
    s.push(3)
    print(s)

print("Peddireddy hari vardhan reddy")



list = [20,30,40,50,60]

print(list)


# Checking the Number is even or odd
def isEven(n):
    return (n%2 == 0)

if __name__=="__main__":
    n = 107
    if isEven(n):
        print("True")
    else:
        print("False")


class Dog:
    species = "Canine"
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def callDog(self):
        result = f"My name is {self.name} and my age is {self.age}"

obj = Dog("Peddireddy",234)
print(obj.species,obj.name,obj.age)


class A:
    def __init__(self,name):
        self.name = name
    def display_name(self):
        print(f"my name is {self.name}")


class B(A):
    def __init__(self,name):
        self.name = name
    def sound(self):
        print(f"I like Violin Sound ... {self.name}")


obj2 = B(123)
print(obj2.name)
obj2.display_name()
obj2.sound()

'''
1: Design Patterns
2: Programatic Programmer
3: Clean Code
'''

