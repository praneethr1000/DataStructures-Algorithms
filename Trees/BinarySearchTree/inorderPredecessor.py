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

    def predecessor(self,node):
        temp = None
        if node.left:
            temp = node.left
            while temp.right:
                temp = temp.right
        return temp.data

    def successor(self,node):
        temp = None
        if node.right:
            temp = node.right
            while temp.left:
                temp = temp.left
        return temp.data

tree = BST()
root = Node(3)
tree.insertion(2,root)
tree.insertion(4,root)
tree.insertion(1,root)
tree.insertion(5,root)
print(tree.predecessor(root.left))
print(tree.successor(root.right))
