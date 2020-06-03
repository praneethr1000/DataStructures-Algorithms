class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def height(self,root):
        if root == None:
            return 0
        return max(self.height(root.left),self.height(root.right)) + 1

    def heightIterative(self,root):
        if root == None:
            return 0
        que = []
        temp = 0
        que.append([root,1])
        while que:
            (node, depth) = que.pop()
            temp = max(depth,temp)
            if node.left:
                que.append([node.left,depth+1])
            if node.right:
                que.append([node.right,depth+1])
        return temp


root = Node("A")
root.left = Node("B")
root.right = Node("C")

tree = Tree()
print(tree.height(root))
print(tree.heightIterative(root))