class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def suM(self,root):
        if root == None:
            return 0
        return root.data + self.suM(root.left) + self.suM(root.right)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

tree = Tree()
print(tree.suM(root1))