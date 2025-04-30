# Create a Node
class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        newNode = Node(value)
        self.first = newNode
        self.last = newNode
        self.length = 1
    def print_queue(self):
        temp = self.first # temp = self.first = newNode = Node(value)
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def EnQueue(self,value):
        newNode = Node(value)
        if self.first is None:
            self.first = newNode
            self.last = newNode
        else:
            self.last.next = newNode
            self.last = newNode
        self.length = self.length+1
    def Dequeue(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length = self.length -1
        return temp.value


n2 = Queue(1)
n2.EnQueue(3)
n2.print_queue()

print(n2.Dequeue())
print(n2.Dequeue())
print(n2.Dequeue())


print(".................")
for i in range(10):
    Queue(i).print_queue()

for _ in range(10):
    n2.Dequeue()
    n2.print_queue()