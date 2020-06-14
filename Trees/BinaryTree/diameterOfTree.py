res = 0
def height(root):
    global res
    if root == None:
        return 0
    left = height(root.left)
    right = height(root.right)
    res = max(res,(1+left+right))
    return 1 + max(left,right)

def diameter(root):
    global res
    if root == None:
        return 0
    res = 0
    height(root)
    return res