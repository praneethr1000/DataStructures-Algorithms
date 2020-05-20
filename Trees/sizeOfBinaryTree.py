class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None

    def size(self,root):
        if root == None:
            return 0
        return self.size(root.left) + self.size(root.right) + 1

    def sizeUsingIteration(self,root):
        if root == None:
            return 0
        que = []
        node = None
        size = 0
        que.append(root)
        while que:
            node = que.pop(0)
            size += 1
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        return size

root = Node("A")
root.left = Node("B")
root.right = Node("C")

tree = Tree()
print(tree.size(root))
print(tree.sizeUsingIteration(root))