res = 0
def maxPath(root):
    global res
    if root == None:
        return 0
    left = maxPath(root.left)
    right = maxPath(root.right)
    max_now = max(root.data,max(left,right)+root.data)
    max_end = max(max_now,root.data+left+right)
    res = max(res,max_end)
    return max_now

def maxPathSum(root):
    global res
    if root == None:
        return
    res = 0
    maxPath(root)
    return res