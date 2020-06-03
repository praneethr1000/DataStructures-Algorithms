maxData = 0
class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None

    def maximumElement(self,root):
        if root == None:
            return
        que = []
        node = None
        x = root.data
        que.append(root)
        while que:
            node = que.pop(0)
            if node.data > x:
                x = node.data
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)
        print(x)

    def maximumElementRecursion(self,root):
        global maxData
        if root == None:
            return maxData
        if root.data > maxData:
            maxData = root.data
        self.maximumElementRecursion(root.left)
        self.maximumElementRecursion(root.right)
        return maxData


root = Node(1)
root.left = Node(2)
root.right = Node(3)

tree = Tree()
tree.maximumElement(root)
print(tree.maximumElementRecursion(root))