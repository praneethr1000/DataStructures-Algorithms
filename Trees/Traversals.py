class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None

    def inorder(self,root):
        if root == None:
            return
        self.inorder(root.left)
        print(root.data, end=" ")
        self.inorder(root.right)

    def preorder(self,root):
        if root == None:
            return
        print(root.data,end= " ")
        self.preorder(root.left)
        self.preorder(root.right)

    def postorder(self,root):
        if root == None:
            return
        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data,end = " ")

    def inorderIterative(self,root):
        if root == None:
            return None
        stk = []
        node = root
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                print(node.data,end = " ")
                node = node.right

    def preorderIterative(self,root):
        if root == None:
            return
        stk = []
        stk.append(root)
        while stk:
            node = stk.pop()
            print(node.data,end = " ")
            if node.right:
                stk.append(node.right)
            if node.left:
                stk.append(node.left)

    def postorderIterative(self,root):
        if root == None:
            return
        stk = []
        node = root
        visited = set()
        while stk or node:
            if node:
                stk.append(node)
                node = node.left
            else:
                node = stk.pop()
                if node.right and not node.right in visited:
                    stk.append(node)
                    node = node.right
                else:
                    visited.add(node)
                    print(node.data,end = " ")
                    node = None

    def levelOrderTraversal(self,root):
        if root == None:
            return
        que = []
        node = None
        que.append(root)
        while que:
            node = que.pop(0)
            print(node.data)
            if node.left:
                que.append(node.left)
            if node.right:
                que.append(node.right)




root = Node("A")
root.left = Node("B")
root.right = Node("C")

tree = Tree()
tree.inorder(root)
print()
tree.inorderIterative(root)
print()
tree.preorder(root)
print()
tree.preorderIterative(root)
print()
tree.postorder(root)
print()
tree.postorderIterative(root)
print()
tree.levelOrderTraversal(root)





