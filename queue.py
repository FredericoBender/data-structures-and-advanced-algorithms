#encoding=utf-8

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self._size = 0

    def push(self,value):
        node = Node(value)
        if(self.last==None):
            self.last = node
        else:
            self.last.next = node
            self.last = node
        if (self.first==None):
            self.first = node
        self._size+=1

    def pop(self):
        if(self.first!=None):
            value = self.first.value
            self.first = self.first.next
            self._size-=1
            return value
        else:
            raise IndexError("The queue is empty")

    def peek(self):
        if(self._size>0):
            value = self.first.value
            return value
        else:
            raise IndexError("The stack is empty")

    def __len__(self): 
        return self._size

    def __repr__(self):
        if (self._size>0):
            r = ""
            pointer = self.first
            while(pointer):
                r = r + str(pointer.value) + " "
                pointer = pointer.next
            return r
        return "Empty queue"

    def __str__(self):
        return self.__repr__()


if (__name__=="__main__"):
    queueList = Queue()
    queueList.push(2)
    queueList.push("mahoe")
    queueList.push("batata")
    queueList.push(3)

    print("size = {}".format(len(queueList)))
    print("queue = \n{}".format(queueList))
    queueList.pop()
    queueList.push(6)
    print("queue = \n{}".format(queueList))