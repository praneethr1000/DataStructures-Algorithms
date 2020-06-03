def PreOrderSuccessor(p):
    if p.leftTag == 1:
        return p.left
    else:
        pos = p
        while pos.rightTag == 0:
            pos = pos.right
        return pos.right

def PreOrderTraversal(root):
    p = PreOrderSuccessor(root)
    while p != root:
        p = PreOrderSuccessor(p)
        print(p.data)



