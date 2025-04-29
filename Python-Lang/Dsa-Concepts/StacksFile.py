# Stacks : LIFO last in first out 
'''
example: window tabs in laptop or pc
- stack only top element
- 
'''
from prompt_toolkit import print_formatted_text


class Node:
    def __init__(self,value):
        self.value = value
        self.next = None
    
class Stack:

    def __init__(self,value):
        new_node = Node(value)
        self.top = new_node
        self.height = 1

    def print_stack(self):
        temp = self.top
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def push(self,value):
        new_node = Node(value)
        if self.height == 0:
            self.top = new_node
        else:
            new_node.next = self.top
            self.top = new_node
        self.height = self.height+1

    def pop(self):
        if self.height == 0:
            return None
        temp = self.top
        self.top = self.top.next
        temp.next = None
        self.height = self.height - 1
        return temp

my_stack = Stack(4)
my_stack.push(1)
my_stack.push(7)
my_stack.push(8)
my_stack.push(10)
my_stack.push(20)
my_stack.print_stack()

my_stack.pop()
my_stack.print_stack()
my_stack.pop()
my_stack.print_stack()
my_stack.pop()
my_stack.print_stack()
my_stack.pop()
my_stack.print_stack()


s = "peddireddy"
stack = []
for char in s:
    stack.append(char)

print(stack)
reversed_string = ""
while stack:
    reversed_string = reversed_string + stack.pop()


print(reversed_string)