class HashTable:
    def __init__(self,size):
        self.data_map = [None] * size
    
    def _hash(self,key):
        my_Hash = 0
        for letter in key:
            my_Hash = (my_Hash + ord(letter) * 23)%len(self.data_map)
        return my_Hash
    def printTable(self):
        for i , val in enumerate(self.data_map):
            print(i,":",val)

    def set_item(self,key,value):
        index = self._hash(key)
        if self.data_map[index] == None:
            self.data_map[index] = []
        self.data_map[index].append([key,value])

    def get_item(self,key):
        index = self._hash(key)
        if self.data_map[index] is not None:
            for i in range(len(self.data_map[index])):
                if self.data_map[index][i][0] == key:
                    return self.data_map[index][i][1]
        return None
    def keys(self):
        all_keys=[]
        for i in range(len(self.data_map)):
            if self.data_map[i] is not None:
                for j in range(len(self.data_map[i])):
                    all_keys.append(self.data_map[i][j][0])
        return all_keys

obj1 = HashTable(8)
obj1.printTable()

print("This is setting table..........")
obj1.set_item('hari',100)
obj1.set_item('jio',300)
obj1.set_item('airtel',500)
obj1.set_item('aicel',800)
obj1.set_item('biga',800)
obj1.set_item('duall',800)
obj1.set_item('simple',800)
obj1.set_item('harly',800)
obj1.printTable()

print("getting the value .........")
print(obj1.get_item('hari'))

print(obj1.keys())


def hasT(list1,list2):
    myDict = {}
    for i in list1:
        myDict[i] = True
    for j in list2:
        if j in myDict:
            return True
    return False

list1 = [1,2,3]
list2 = [6,7,8]
print(hasT(list1,list2))
