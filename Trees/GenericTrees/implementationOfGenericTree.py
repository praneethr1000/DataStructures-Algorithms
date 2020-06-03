import string
class Node:
    def __init__(self,data):
        self.data = data
        self.child = None
        self.nextSibling = None

class GenericTree:
    def __init__(self,parent,value = None):
        self.parent = parent
        self.value = value
        self.childList = []
        if parent is None:
            self.birthOrder = 0
        else:
            self.birthOrder = len(parent.childList)
            parent.childList.append(self)

    def nChildren(self):
        return len(self.childList)

    def nthChild(self,n):
        return self.childList[n]

    def fullPath(self):
        result = []
        parent = self.parent
        kid = self
        while parent:
            result.insert(0,kid.birthOrder)
            parent, kid = parent.parent, parent
        return result

    def nodeId(self):
        fullPath = self.fullPath()
        return NodeId(fullPath)

class NodeId:
    def __init__(self,path):
        self.path = path

    def __str__(self):
        l = map(str,self.path)
        return string.join(l,"/")

    def find(self,node):
        return self.__refind(node,0)

    def __refind(self,node,i):
        if i >= len(self.path):
            return node.value
        else:
            childNo = self.path[i]
        try:
            child = node.nthChild(childNo)
        except IndexError:
            return None
        return self.__refind(child,i+1)

    def isOnPath(self,node):
        if len(nodePath) > len(self.path):
            return 0
        for i in range(len(nodePath)):
            if nodePath[i] != self.path[i]:
                return 0
        return 1

# root = Node(A)
# root.child = Node(B)
# root.child.nextSibling = Node(C)
# root.child.nextSibling.nextSibling = Node(D)
# root.child.nextSibling.nextSibling.nextSibling = Node(E)
# root.child.nextSibling.nextSibling.child = Node(H)
# root.child.nextSibling.nextSibling.nextSibling.child = Node(I)
# root.child.nextSibling.nextSibling.nextSibling.child.nextSibling = Node(J)
# root.child.nextSibling.nextSibling.nextSibling.child.nextSibling.child = Node(P)
# root.child.nextSibling.nextSibling.nextSibling.child.nextSibling.child.nextSibling = Node(Q)

tree = GenericTree(None,"A")
GenericTree("A","B")
GenericTree("A","C")







