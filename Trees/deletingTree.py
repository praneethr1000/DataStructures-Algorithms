class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def delete(self,root):
        if root == None:
            return
        self.delete(root.left)
        self.delete(root.right)
        del root

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

root = Node("A")
root.left = Node("B")
root.right = Node("C")

tree = Tree()
tree.inorder(root)
tree.delete(root)

