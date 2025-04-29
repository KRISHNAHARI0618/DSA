from abc import ABC , abstractmethod

class BaseClass(ABC):
    @abstractmethod
    def method1():
        print("hello world")

# Python does not support by deafult abstract class and its methods
# What is abstract class
# 

class computer(ABC):
    @abstractmethod
    def process(Self):
        pass
    @abstractmethod
    def addition(self):
        pass

class simple(computer):
    def process(Self):
        print("Hello World Simple....")
    def addition(self):
        print("Calling Addition Class.....")

class hardly(computer):
    def subtraction(self):
        print("Calling Substraction Method.....")

com1= simple()
com1.process()
com1.addition()

# com2 = hardly()
# com2.subtraction()

# Encapsulation in Python:
# Access Specifiers Public, Private, Protected
# Protected Attribute (_variable name)
# Private Attribute (__variable name)
class Student:
    def __init__(self,name,rollno):
        self.name = name #Public Variable
        self._rollno = rollno  # Protected Variable
    def display(self):
        print(f"Hi My Self is {self.name} and my RollNo is {self._rollno}")

s1 = Student(10,20)
s1.display()

class Branch(Student):
    pass

s2 = Branch("peddireddy",40)
print(s2.name)
print(s2._rollno)

class TestPrivate:
    def __init__(self,age,rollno):
        self.age = age
        self.__rollno = rollno
    
    def show(self):
        print(f"My Age is {self.age} and my roll no is {self.__rollno}")

c1 = TestPrivate(20,30)
c1.show()
print(c1.age)
print(c1.__rollno)