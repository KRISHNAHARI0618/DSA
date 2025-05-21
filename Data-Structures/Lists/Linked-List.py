# Node Declaration
class Node:
    def __init__(self,value)->any:
        self.value = value
        self.next = None

#Linked List Declaration

class LinkedList:
    def __init__(self,value)-> any:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def appending(self,value)-> any:
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length = self.length + 1

    def printlist(self)-> any:
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

linkedlist2 = LinkedList(10)
linkedlist2.appending(20)
linkedlist2.appending(30)
linkedlist2.appending(40)
linkedlist2.appending(50)
linkedlist2.appending(60)
linkedlist2.printlist()









