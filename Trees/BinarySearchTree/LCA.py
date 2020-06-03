def LCA(root,a,b):
    while root:
        if (a <= root.data and root.data < b) or (a > root.data and root.data >= b):
            return root
        elif a < root.data and b < root.data:
            root = root.left
        else:
            root = root.right
