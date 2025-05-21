class Node:
    def __init__(self,value) -> any:
        self.value = value
        self.next = None
        self.prev = None

class DLL:
    # DLL Constructor
    def __init__(self,value)-> any:
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 0

    # Printing ALL Values 
    def printDLL(self)-> any:
        temp = self.head
        while temp:
            print(temp.value,end=" ")
            temp = temp.next
        print()

    # Appending Values
    def appendDLL(self,value)-> any:
        newNode = Node(value)
        if not self.head:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        self.length = self.length + 1

    # String Representation
    def __str__(self)-> any:
        temp = self.head
        result = ""
        while temp:
            result = result + str(temp.value)
            if temp.next:
                result = result + "<-->"
            temp = temp.next
        return result
    
    # Prepending The values
    def preprending(self,value) -> any:
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.length = self.length + 1
    # Travesal 
    def traversal(self) -> any:
        curr = self.head
        while curr:
            print(curr.value,end=" ")
            curr = curr.next
        print()
    # Reverse Traversal
    def revTraversal(self) -> any:
        curr = self.tail
        while curr:
            print(curr.value,end=" ")
            curr = curr.prev
        print()
    # Searching Value
    def searcingValue(self,val) -> any:
        curr = self.head
        while curr:
            if curr.value == val:
                return True
            curr = curr.next
        return False
    # get Method 
    def getValue(self,index) -> any:
        n = self.length
        if index < n // 2:
            curr = self.head
            for _ in range(index):
                curr = curr.next
        else:
            curr = self.tail
            for _ in range(n-1,index,-1):
                curr = curr.prev
        return curr
    # Set Method:
    def setMethod(self,index,value) -> any:
        node = self.getValue(index)
        if node:
            self.value = value
            return True
        return False
    
    # Insert Method
    def insertMethod(self,index,value)-> any:
        if index < 0 or index > self.length:
            print("Index Out of Range Functions")
            return
        newNode = Node(value)
        if index == 0:
            self.preprending(value)
            return
        elif index == self.length:
            self.appendDLL(value)
            return
        temp = self.getValue(index-1) #temp = 3-1 = 50
        newNode.next = temp.next # 32 -> 50 -> == 10
        newNode.prev = temp # <- 37 == 50
        temp.next.prev = newNode # 50 ->  37 <-10  
        temp.next = newNode # 50 -> 37 
        self.length = self.length+1

    
dll = DLL(10)
dll.appendDLL(20)
dll.appendDLL(30)
dll.appendDLL(40)
dll.preprending(50)
dll.preprending(60)
dll.preprending(70)


dll.printDLL()
dll.traversal()
dll.revTraversal()

print(dll.searcingValue(70))
print(dll.getValue(-1))

print(dll)
print(dll.setMethod(3,37))
print(dll)

print(dll.insertMethod(3,37))
print(dll)

print(dll.insertMethod(-1,47))
print(dll)

print(dll.insertMethod(10,57))
print(dll)
    