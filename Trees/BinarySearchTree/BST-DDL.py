class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    head = None
    prev = None
    def BinaryTree2DoubleLinkedList(self,root):
        if root == None:
            return
        self.BinaryTree2DoubleLinkedList(root.left)
        if self.prev == None:
            self.head = root
        else:
            root.left = self.prev
            self.prev.right = root
        self.prev = root
        self.BinaryTree2DoubleLinkedList(root.right)

    def display(self,temp):
        while temp:
            print(temp.data,end = " ")
            temp = temp.right

tree = Tree()
root = Node(10)
root.left = Node(12)
root.right = Node(15)
root.left.left = Node(25)
root.left.right = Node(30)
root.right.left = Node(36)


tree.BinaryTree2DoubleLinkedList(root)
tree.display(tree.head)

