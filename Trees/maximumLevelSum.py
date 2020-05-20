class Node:
    def __init__(self,data):
        self.data = data
        self.right = None
        self.left = None

class Tree:
    def maxLevelSum(self,root):
        if root == None:
            return 0
        que = []
        que.append(root)
        que.append(None)
        level = maxlevel = maxSum = currentSum = 0
        while que:
            node = que.pop(0)
            if node == None:
                if currentSum > maxSum:
                    maxSum = currentSum
                    maxlevel = level
                currentSum = 0
                if que:
                    que.append(None)
                    level += 1
            else:
                currentSum = currentSum + node.data
                if node.left:
                    que.append(node.left)
                if node.right:
                    que.append(node.right)
        print(maxlevel)



root1 = Node(1)
root1.left = Node(2)
root1.right = Node(3)
root1.left.left = Node(4)
root1.left.right = Node(5)

tree = Tree()
tree.maxLevelSum(root1)

