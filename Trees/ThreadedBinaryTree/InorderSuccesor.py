def InorderSuccesor(p):
    if p.rightTag == 0:
        return p.right
    else:
        pos = p.right
        while pos.leftTag != 0:
            pos = pos.left
        return pos


def InorderTraversal(root):
    p = InorderSuccesor(root)
    while p != root:
        p = InorderSuccesor(p)
        print(p.data)


