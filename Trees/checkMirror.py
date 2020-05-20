class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def mirror(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 == None or root2 == None:
            return False
        return ( root1.data == root2.data and
                self.mirror(root1.left,root2.right) and
                self.mirror(root1.right,root2.left) )

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2 = Node(1)
root2.left = Node(3)
root2.right = Node(2)
root2.right.left = Node(5)
root2.right.right = Node(4)

tree = Tree()
print(tree.mirror(root1,root2))