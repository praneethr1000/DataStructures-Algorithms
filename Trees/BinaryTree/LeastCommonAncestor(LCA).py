class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def lca(self,root,node1,node2):
        if root == None:
            return None
        if root.data == node1 or root.data == node2:
            return root.data
        left = self.lca(root.left,node1,node2)
        right = self.lca(root.right,node1,node2)
        if left and right:
            return root.data
        else:
            return left if left else right


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

tree = Tree()
print(tree.lca(root1,root1.left.left.data,root1.left.right.data))