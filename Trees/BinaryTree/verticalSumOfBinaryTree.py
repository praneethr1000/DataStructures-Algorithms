class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    dic = {}
    def verticalSum(self,root,column):
        if root == None:
            return
        if column not in self.dic:
            self.dic[column] = 0
        self.dic[column] += root.data
        self.verticalSum(root.left,column-1)
        self.verticalSum(root.right,column+1)

root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)
root1.right.left = Node(6)
root1.right.right = Node(7)

tree = Tree()
tree.verticalSum(root1,0)
t = list(tree.dic.keys())
t.sort()
for i in t:
    print(tree.dic[i],end = " ")