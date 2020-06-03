def trim(root,minVal,maxVal):
    if root == None:
        return
    root.left = trim(root.left,minVal,maxVal)
    root.right = trim(root.right,minVal,maxVal)
    if minVal <= root.data <= maxVal:
        return root
    if root.data < minVal:
        return root.right
    if root.data > maxVal:
        return root.left
