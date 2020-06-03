class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insertion(self,data,root):
        if root.data < data:
            if root.right == None:
                root.right = Node(data)
            else:
                self.insertion(data,root.right)
        else:
            if root.left == None:
                root.left = Node(data)
            else:
                self.insertion(data,root.left)

    def search(self,root,data):
        if root == None:
            return "notFound"
        if root.data == data:
            return "found"
        elif root.data < data:
            return self.search(root.right,data)
        else:
            return self.search(root.left,data)

    def searchIterative(self,root,data):
        temp = root
        while temp != None and temp.data != data:
            if temp.data < data:
                temp = temp.right
            else:
                temp = temp.left
        return temp


tree = BST()
root = Node(3)
tree.insertion(2,root)
tree.insertion(4,root)
tree.insertion(1,root)
tree.insertion(5,root)
print(tree.search(root,4))
print(tree.search(root,6))
