class Node:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None

def BST(A,left,right):
    if left > right:
        return None
    node = Node()
    if not node:
        return
    if left == right:
        node.data = A[left]
        node.left = None
        node.right = None
    else:
        mid = (left+(right-left))//2
        node.data = A[mid]
        node.left = BST(A,left,mid-1)
        node.right = BST(A,mid+1,right)
    return node

A = [1,2,3,4,5]
root = BST(A,0,len(A)-1)
print(root)

#TODO 12


