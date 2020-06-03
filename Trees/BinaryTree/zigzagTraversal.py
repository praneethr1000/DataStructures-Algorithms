class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def zigzag(self,root):
        if root == None:
            return
        que = []
        stk = []
        que.append(root)
        while que:
            node = que.pop(0)
            stk.append(node.data)
            if node.right:
                que.append(node.right)
            if node.left:
                que.append(node.left)


# TODO: 7.Problem 32 Do it later


