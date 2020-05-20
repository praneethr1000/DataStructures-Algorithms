class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def mirror(self,root):
        if root == None:
            return
        else:
            self.mirror(root.left)
            self.mirror(root.right)
            temp = root.left
            root.left = root.right
            root.right = temp
        return root

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end = " ")
        self.inorder(root.right)


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

tree = Tree()
tree.inorder(root1)
print()
tree.mirror(root1)
tree.inorder(root1)