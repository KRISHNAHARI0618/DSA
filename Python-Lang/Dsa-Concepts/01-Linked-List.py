import tarfile


class Node:
    def __init__(self,value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self,value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

o1 = LinkedList(100)
print(o1.head.value)



node = {
   'value' : 23,
   'next' : {
    'value' : 4,
    'next' :{
        'value' : 45,
        'next' : {
            'value' : 6,
            'next' :{
                'value': 21,
                'next': None
            }
        }
    }
   } 
}
print(node.keys().mapping)

# What is Linked List
# Linked list Is a Form of sequential collection and it does not have to be in order. A linked list is made up of independent nodes that may contain any type of data and each node has a reference of next node in the link
# Linked List is not contigious
# Python List 

head = {
    'value' : 23,
    'next' : {
        'value' : 45,
        'next' : {
            'value' : 67,
            'next' : {
                'value' : 89,
                'next' :{ 
                    'value' : 100,
                    'next' : {
                        'value' : 120,
                        'next' : None
                    }
                    
                }
            }
        }

    }
}

print(head['next']['next']['value'])


class Node:
    def __init__(self,Value):
        self.Value = Value
        self.Next = None


class LinkedList:
    def __init__(self,Value):
        new_node = Node(Value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def append(self,Value):
        new_node = Node(Value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.Next = new_node
            self.tail = new_node
        self.length = self.length + 1
        
    def printList(self):
        temp = self.head
        while temp is not None:
            print(temp.Value)
            temp = temp.Next

    def pop(self):
        # Linked List Contains 0 Elements
        if self.length == 0:
            return None
        # LL Contains more than 1 elements
        temp = self.head
        pre = self.head
        while (temp.Next):
            pre = temp
            temp = temp.Next
        self.tail = pre
        self.tail.Next = None
        self.length = self.length - 1
        # LL Contains One element 
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp.Value

    def prepend(self,Value):
        new_node = Node(Value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.Next = self.head
            self.head = new_node
        self.length = self.length + 1

    def pop_first(self):
        # For Empty List 
        if self.length == 0:
            return None
        # For More Than One elements in Linked List
        temp = self.head
        self.head = self.head.Next
        temp.next = None
        self.length = self.length - 1
        # For Linked List Contains one element
        if self.length == 0:
            self.tail = None
        return temp.Value

newLList = LinkedList(10)
print(newLList.head.Value)
newLList.append(200)
newLList.append(300)


newLList.prepend(278)
newLList.printList()

newLList.pop()
newLList.printList()

newLList.pop()
newLList.printList()

newLList.pop_first()

