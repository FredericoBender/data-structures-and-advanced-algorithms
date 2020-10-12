#encoding=utf-8

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self._size = 0

    def _get(self, index):
        currentValue = self.head
        for i in range(index):
            if currentValue: 
                currentValue = currentValue.next
            else:
                raise IndexError("list index out of range")
        return currentValue

    def append(self, value):
        """Append a value in the list"""
        if self.head:
            pointer = self.head
            while pointer.next != None:
                pointer = pointer.next
            pointer.next = Node(value)
        else:
            self.head = Node(value)
        self._size += 1
    
    def index(self, value):
        """Return index of a value in the list"""
        currentValue = self.head
        i = 0
        while currentValue:
            if currentValue.value == value: 
                return i
            currentValue = currentValue.next
            i += 1
        raise ValueError("{} is not in list".format(value))
    
    def insert(self, index, value):
        """Insert a value in the list"""
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            pointer = self._get(index - 1)
            node.next = pointer.next
            pointer.next = node
        self._size = self._size + 1

    def remove(self, value):
        """Remove a value in the list"""
        if self.head == None:
            raise ValueError("{} is not in list".format(value))
        elif self.head.value == value:
            self.head = self.head.next
            self._size = self._size - 1
            return True
        else:
            ancestor = self.head
            pointer = self.head.next
            while pointer:
                if pointer.value == value:
                    ancestor.next = pointer.next
                    pointer.next = None
                    self._size = self._size - 1
                    return True
                ancestor = pointer
                pointer = pointer.next
        raise ValueError("{} is not in list".format(value))

    def __getitem__(self, index): 
        currentValue = self._get(index)
        if currentValue:
            return currentValue.value
        else:
            raise IndexError("list index out of range")

    def __setitem__(self, index, value):
        currentValue = self._get(index)
        if currentValue:
            currentValue.value = value
        else:
            raise IndexError("list index out of range")
    
    def __len__(self): #Python function len now will work with this object
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.head
        while pointer:
            r = r + str(pointer.value) + "->"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()

if __name__ == "__main__":
    valuesList = LinkedList()
    valuesList.append(4)
    valuesList.append(3)

    valuesList.insert(0,13)
    valuesList.insert(1,123)

    valuesList[3] = 300

    print(valuesList[0])
    print(valuesList[1])

    #print(valuesList.index(4))
    #print(len(valuesList))
    print(valuesList)