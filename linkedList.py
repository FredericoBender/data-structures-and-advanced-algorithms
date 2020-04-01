#encoding=utf-8
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self): #__init__ é o construtor que sempre executa ao inicilizar a classe
        self.head = None
        self._size = 0

    def append(self, value):
        """Append a value in the list"""
        if(self.head ):
            pointer = self.head
            while (pointer.next!=None):
                pointer = pointer.next
            pointer.next = Node(value)
        else:
            self.head = Node(value)
        self._size+=1

    def set (self, index):
        pass
    def get(self, index):
        pass

    def __getitem__(self, index): #__ é sobrecarga de operador, da pra usar coisas nativas da linguagem no seu objeto como o []
        currentValue = self.head
        for i in range(index):
            if(currentValue): #Se ele existe
                currentValue = currentValue.next
            else:
                raise IndexError("list index out of range")
        if(currentValue):
            return currentValue.value
        else:
            raise IndexError("list index out of range")

    def __setitem__(self,index,value):
        currentValue = self.head
        for i in range(index):
            if(currentValue): 
                currentValue = currentValue.next
            else:
                raise IndexError("list index out of range")
        if(currentValue):
            currentValue.value = value
        else:
            raise IndexError("list index out of range")

    def index (self, value):
        """Return index of a value in the list"""
        currentValue = self.head
        i=0
        while(currentValue):
            if(currentValue.value==value): 
                return i
            currentValue = currentValue.next
            i+=1
        raise ValueError("{} is not in list".format(value))
    
    def __len__(self): #Python function len now will work with this object
        """Return the size of the list"""
        return self._size

if (__name__=="__main__"):
    valuesList = LinkedList()
    valuesList.append(4)
    valuesList.append(3)
    print(valuesList[0])
    print(valuesList[1])
    print(valuesList.index(4))
    print(len(valuesList))