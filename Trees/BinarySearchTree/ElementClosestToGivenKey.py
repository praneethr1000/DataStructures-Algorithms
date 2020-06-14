def mini(root, k):
    global res
    if root == None:
        return
    que = []
    que.append(root)
    while que:
        node = que.pop(0)
        res = min(abs(node.data - k), res)
        if node.left:
            que.append(node.left)
        if node.right:
            que.append(node.right)

res = float('inf')
def minDiff(root, K):
    global res
    res = float('inf')
    mini(root, K)
    return res