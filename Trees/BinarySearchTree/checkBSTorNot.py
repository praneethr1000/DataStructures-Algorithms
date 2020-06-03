class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class BST:
    #Inorder approach
    def checkBST(self,root,previous):
        if root == None:
            return 1
        if not self.checkBST(root.left,previous):
            return 0
        if root.data < previous:
            return 0
        previous = root.data
        return self.checkBST(root.right,previous)




root = Node(3)
root.left = Node(2)
root.left.left = Node(1)
root.right = Node(6)
root.right.right = Node(5)
tree = BST()
print(tree.checkBST(root,float("-infinity")))