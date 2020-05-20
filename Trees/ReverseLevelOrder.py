class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def __init__(self):
        self.root = None
    def reverseLevelOrder(self,root):
        stk = []
        que = []
        node = None
        que.append(root)
        while que:
            node = que.pop(0)
            stk.append(node.data)
            if node.right:
                que.append(node.right)
            if node.left:
                que.append(node.left)
        for _ in range(len(stk)):
            print(stk.pop(),end = " ")

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
root.right.left = Node(6)
root.right.right = Node(7)

tree = Tree()
tree.reverseLevelOrder(root)

