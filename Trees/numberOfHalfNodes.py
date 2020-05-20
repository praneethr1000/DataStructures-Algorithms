class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def numberOfHalfNodes(self,root):
        if root == None:
            return
        que = []
        que.append(root)
        leaves = []
        while que:
            node = que.pop(0)
            if (node.right and not node.left) or (node.left and not node.right):
                leaves.append(node.data)
            if node.right:
                que.append(node.right)
            if node.left:
                que.append(node.left)
        return leaves

tree = Tree()
root = Node("A")
root.left = Node("B")
root.right = Node("C")
root.right.right = Node("D")
print(tree.numberOfHalfNodes(root))