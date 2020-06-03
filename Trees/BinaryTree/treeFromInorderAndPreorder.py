class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def buildTree(self,inorder,preorder):
        if not inorder:
            return None
        root = Node(preorder[0])
        posIndex = inorder.index(preorder[0])
        root.left = self.buildTree(inorder[:posIndex],preorder[1:1+posIndex])
        root.right = self.buildTree(inorder[posIndex+1:],preorder[posIndex+1:])
        return root

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data,end = " ")
        self.inorder(root.right)

inorder = ["D","B","E","A","F","C"]
preorder = ["A","B","D","E","C","F"]
tree = Tree()
root = tree.buildTree(inorder,preorder)
tree.inorder(root)