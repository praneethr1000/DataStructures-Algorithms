class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
class Tree:
    def structuralIdentical(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 != None and root2 != None:
            return (self.structuralIdentical(root1.left,root2.left) and
                   self.structuralIdentical(root1.right,root2.right))
        return False

    def identicalWithData(self,root1,root2):
        if root1 == None and root2 == None:
            return True
        if root1 != None and root2 != None:
            return ((root1.data == root2.data) and
                   self.identicalWithData(root1.left,root2.left) and
                   self.identicalWithData(root1.right,root2.right))
        return False


root1 = Node(1)
root2 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

root2.left = Node(2)
root2.right = Node(3)
root2.left.left = Node(4)
root2.left.right = Node(5)

tree = Tree()
print(tree.structuralIdentical(root1,root2))
print(tree.identicalWithData(root1,root2))