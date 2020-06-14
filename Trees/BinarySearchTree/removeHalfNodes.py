def RemoveHalfNodes(root):
    if root == None:
        return
    root.left = RemoveHalfNodes(root.left)
    root.right = RemoveHalfNodes(root.right)
    if not root.left and not root.right:
        return root
    if not root.left:
        return root.right
    if not root.right:
        return root.left
    return root