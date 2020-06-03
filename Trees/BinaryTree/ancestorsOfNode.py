class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def ancestors(self,root,node,ancestors):
        if root == None:
            return 0
        left = self.ancestors(root.left,node,ancestors)
        right = self.ancestors(root.right,node,ancestors)
        if root.left == node or root.right == node or left or right:
            ancestors.append(root.data)
            return 1
        return 0

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

tree = Tree()
ancestors = []
tree.ancestors(root1,root1.left.left,ancestors)
print(ancestors)


