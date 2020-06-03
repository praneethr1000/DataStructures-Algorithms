def rangePrinter(root,k1,k2):
    if root == None:
        return
    if k1 <= root.data <= k2:
        print(root.data)
    if root.data < k1:
        return rangePrinter(root.right,k1,k2)
    if root.data > k2:
        return rangePrinter(root.left,k1,k2)


