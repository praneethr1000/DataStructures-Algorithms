class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def deepestNode(self,root):
        if root == None:
            return 0
        que = []
        que.append(root)
        while que:
            node = que.pop(0)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return node.data

root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.right.right = Node("D")

tree = Tree()
print(tree.deepestNode(root))

