class Stack:
    def __init__(self)-> any:
        self.list = []

    # Printing Elements
    def __str__(self) -> any:
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    # Pushing the elements
    def push(self,value):
        self.list.append(value)
        return "Added Element Succesfully"
    
    # Checking the Emptiness
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    # Pop Method 
    def popMethod(self):
        if self.isEmpty():
            return False
        else:
            return self.list.pop()
    # Peek Method Just Show last element
    def peekMethod(self):
        if self.isEmpty():
            return False
        else:
            return self.list[len(self.list)-1]
        
    def deleteStack(self):
        self.list = None

stack = Stack()
stack.push(10)
stack.push(20)
stack.push(30)
print(stack.isEmpty())
print(stack)
print(stack.popMethod())
print(stack.popMethod())