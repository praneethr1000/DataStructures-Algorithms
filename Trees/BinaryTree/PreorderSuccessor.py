class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def preorderSuccessor(self,node):
        if node.left != None:
            return node.left
