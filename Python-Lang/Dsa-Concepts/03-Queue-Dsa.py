class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class Queue:
    def __init__(self,value):
        new_node = Node(value)
        self.first = new_node
        self.last = new_node
        self.length = 1
    def printQueue(self):
        temp = self.first
        while temp is not None:
            print(temp.value)
            temp = temp.next
    def enque(self,value):
        new_node = Node(value)
        if self.first is None:
            self.first = new_node
            self.last = new_node
        else:
            self.last.next = new_node
            self.last = new_node
        self.length = self.length + 1
    def deque(self):
        if self.length == 0:
            return None
        temp = self.first
        if self.length == 1:
            self.first = None
            self.last = None
        else:
            self.first = self.first.next
            temp.next = None
        self.length = self.length - 1
        return temp.value

que = Queue(10)
que.enque(20)
que.enque(30)
que.enque(40)
que.printQueue()

print(que.deque())