class Node:
    def __init__(self,value):
        self.value=value
        self.next=None

class Linkedlist:
    def __init__(self):
        self.head=None

class Stack:
    def __init__(self):
        self.Linkedlist=Linkedlist()
    
    def isEmpty(self):
        if self.Linkedlist.head == None:
            return True
        else:
            return False
        
stack = Stack()
print(stack.isEmpty())