class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None

    def insertionUsingLevelOrder(self,data,root):
        newNode = Node(data)
        if root == None:
            root = newNode
            return root
        que = []
        que.append(root)
        while que:
            node = que.pop(0)
            if node.left == None:
                node.left = newNode
                return root
            else:
                que.append(node.left)
            if node.right == None:
                node.right = newNode
                return root
            else:
                que.append(node.right)

    def preorder(self,root):
        if root == None:
            return
        print(root.data,end = " ")
        self.preorder(root.left)
        self.preorder(root.right)

    def insertLeft(self,node,data):
        if node.left == None:
            node.left = Node(data)
        else:
            temp = Node(data)
            temp.left = node.left
            node.left = temp

    def insertRight(self,node,data):
        if node.right == None:
            node.right = Node(data)
        else:
            temp = Node(data)
            temp.left = node.left
            node.left = temp

tree = Tree()
node = None
root = tree.insertionUsingLevelOrder(1,node)
tree.insertionUsingLevelOrder(2,root)
tree.insertionUsingLevelOrder(3,root)
tree.insertLeft(root.left,4)
tree.preorder(root)