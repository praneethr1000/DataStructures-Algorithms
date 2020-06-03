count = 0
def kthSmallest(root,k):
    global count
    if root == None:
        return
    left = kthSmallest(root.left,k)
    if left:
        return left
    count += 1
    if count == k:
        return root
    return kthSmallest(root.right,k)