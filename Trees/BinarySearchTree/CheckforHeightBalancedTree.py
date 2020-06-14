class Height:
    def __init__(self):
        self.height = 0


def balanceUtil(root, height):
    if root == None:
        return True

    lh = Height()
    rh = Height()

    left = balanceUtil(root.left, lh)
    right = balanceUtil(root.right, rh)

    height.height = 1 + max(lh.height, rh.height)

    if abs(lh.height - rh.height) <= 1:
        return left and right
    return False


def isBalanced(root):
    height = Height()
    return balanceUtil(root, height)