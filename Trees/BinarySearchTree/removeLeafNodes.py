def removeLeaves(root):
    if root == None:
        return
    if root.left == root.right == None:
        return None
    root.left = removeLeaves(root.left)
    root.right = removeLeaves(root.right)
    return root