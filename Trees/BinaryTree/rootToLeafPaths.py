class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None
paths = []
class Tree:
    global paths
    def pathFinder(self, root, path):
        if root.right == root.left == None:
            print(path)
            paths.append(path)
            return
        else:
            self.pathFinder(root.left, path+" "+str(root.left.data))
            self.pathFinder(root.right, path+" "+str(root.right.data))


root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

tree = Tree()
tree.pathFinder(root1,str(root1.data))
print(paths)

