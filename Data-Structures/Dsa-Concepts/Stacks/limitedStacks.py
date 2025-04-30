class Stack:
    def __init__(self,maxList):
        self.maxList = maxList
        self.list = []

    def __str__(self):
        values = [str(x) for x in reversed(self.list)]
        return '\n'.join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False

maxStack = Stack()