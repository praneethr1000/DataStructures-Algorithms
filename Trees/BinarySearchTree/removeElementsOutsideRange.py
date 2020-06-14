def removeOutOfRange(root,mini,maxi):
    if root == None:
        return
    root.left = removeOutOfRange(root.left,mini,maxi)
    root.right = removeOutOfRange(root.right,mini,maxi)
    if mini <= root.data <= maxi:
        return root
    if root.data < mini:
        return root.right
    if root.data > maxi:
        return root.left
