class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def pathFinder(self,root,val):
        if root == None:
            return
        val = (10*val) + root.data
        if root.right == root.left == None:
            return val
        return self.pathFinder(root.left, val) + self.pathFinder(root.right, val)


    def sumOfNumbers(self,root):
        print(self.pathFinder(root,0))


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

tree = Tree()
tree.sumOfNumbers(root1)