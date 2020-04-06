#encoding=utf-8

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Stack:
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self,value):
        node = Node(value)
        node.next = self.top
        self.top = node
        self._size+=1

    def pop(self):
        if(self._size>0):
            node=self.top
            self.top = node.next
            self._size-=1
            return node.value
        else:
            raise IndexError("The stack is empty")

    def peek(self):
        if(self._size>0):
            return self.top.value
        else:
            raise IndexError("The stack is empty")

    def __len__(self): 
        return self._size

    def __repr__(self):
        r = ""
        pointer = self.top
        while(pointer):
            r = r + str(pointer.value) + "\n"
            pointer = pointer.next
        return r

    def __str__(self):
        return self.__repr__()


if (__name__=="__main__"):
    stackList = Stack()
    stackList.push(2)
    stackList.push("mahoe")
    stackList.push("batata")
    stackList.push(3)

    print("size = {}".format(len(stackList)))
    print("stack = \n{}".format(stackList))
    stackList.pop()
    print("stack = \n{}".format(stackList))