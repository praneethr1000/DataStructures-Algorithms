class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class BST:
    def insertion(self,data,root):
        if root.data < data:
            if root.right == None:
                root.right = Node(data)
            else:
                self.insertion(data,root.right)
        else:
            if root.left == None:
                root.left = Node(data)
            else:
                self.insertion(data,root.left)

    def minimumElement(self,root):
        if root.left == None:
            return root.data
        return self.minimumElement(root.left)

    def maximumElement(self,root):
        if root.right == None:
            return root.data
        return self.maximumElement(root.right)

tree = BST()
root = Node(3)
tree.insertion(2,root)
tree.insertion(4,root)
tree.insertion(1,root)
tree.insertion(5,root)
print(tree.minimumElement(root))
print(tree.maximumElement(root))