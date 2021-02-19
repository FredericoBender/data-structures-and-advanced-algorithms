class Node:
    def __init__(self, value):
        self.value = value
        self.right = None
        self.left = None

    def __str__(self):
        return str(self.value)

class BinaryTree:
    def __init__(self, value=None):
        if value:
            self.root = Node(value)
        else:
            self.root = None

    def insert(self, value):
        parent = None
        currentNode = Node(value)

        while currentNode:
            parent = currentNode
            if value <= currentNode.value:
                currentNode = currentNode.left
            else:
                currentNode = currentNode.right

        if self.root == None:
            self.root = data
        elif value <= parent.value:
            parent.left = Node(value)
        else:
            parent.right = Node(value)
            

if __name__ == "__main__":
    tree = BinaryTree(2)
    tree.insert(8)
    tree.insert(1)
    tree.insert(6)