class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None

    def search(self,root,value):
        if root == None:
            return 0
        if root.data == value:
            return 1
        else:
            temp = self.search(root.left,value)
            if temp == 1:
                return temp
            else:
                return self.search(root.right,value)

    def searchIterative(self,root,value):
        if root == None:
            return 0
        que = []
        node = None
        que.push(root)
        while que and node:
            node = que.pop(0)
            if node.value == value:
                return 1
            if node.left:
                que.push(node.left)
            if node.right:
                que.push(node.right)
        return 0


root = Node(1)
root.left = Node(2)
root.right = Node(3)

tree = Tree()
print(tree.search(root,4))