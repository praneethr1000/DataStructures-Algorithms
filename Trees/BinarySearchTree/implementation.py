class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insertion(self,data,root):
        if root == None:
            root = Node(data)
        else:
            if data < root.data:
                if root.left == None:
                    root.left = Node(data)
                else:
                    self.insertion(data,root.left)
            else:
                if root.right == None:
                    root.right = Node(data)
                else:
                    self.insertion(data,root.right)

    def deletion(self,root,data):
        if root.data == data:
            if root.right and root.left:
                [psucc,succ] = self.findMin(root.right,root)
                if psucc.left == succ:
                    psucc.left = succ.right
                else:
                    psucc.right = succ.right
                succ.left = root.left
                succ.right = root.right
                return succ
            else:
                if root.left:
                    return root.left
                else:
                    return root.right
        else:
            if root.data > data:
                if root.left:
                    root.left = self.deletion(root.left,data)
            else:
                if root.right:
                    root.right = self.deletion(root.right,data)

    def findMin(self,root,parent):
        if root.left:
            self.findMin(root.left,root)
        else:
            return [parent,root]


    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data,end = " ")
        self.inorder(root.right)

tree = BST()
root = Node(3)
tree.insertion(2,root)
tree.insertion(4,root)
tree.insertion(1,root)
tree.insertion(5,root)
tree.inorder(root)
print("\n",end = "")
tree.deletion(root,3)
tree.inorder(root)
print("\n",end = "")


