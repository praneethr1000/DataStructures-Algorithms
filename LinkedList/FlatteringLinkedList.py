def flatten(root):
    current = root
    l =[]
    while current != None:
        l.append(current.data)
        temp = current.next
        if current.bottom:
            temp1 = current.bottom
        while temp1 != None:
            l.append(temp1.data)
            temp1 = temp1.bottom
        current = temp
    print(l)
    l.sort()
    print(l)
    new_root = Node(l[0])
    current = new_root
    for i in range(1,len(l)):
        current.bottom = Node(l[i])
        current = current.bottom
    return new_root

class Node:
    def __init__(self,d):
        self.data = d
        self.next = None
        self.bottom = None

def printList(node):
    while(node is not None):
        print(node.data,end= " ")
        node = node.bottom

    print()

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        head = None
        N= int(input())
        arr = []
        arr = [int(x) for x in input().strip().split()]
        temp = None
        tempB = None
        pre= None
        preB = None

        flag = 1
        flag1 = 1
        listo = [int(x) for x in input().strip().split()]
        it = 0
        for i in range(N):
            m = arr[i]
            m-=1
            a1 = listo[it]
            it +=1
            temp = Node(a1)
            if flag == 1:
                head = temp
                pre = temp
                flag = 0
                flag1 = 1
            else:
                pre.next = temp
                pre = temp
                flag1 = 1
            for j in range(m):
                a = listo[it]
                it +=1
                tempB = Node(a)
                if flag1 == 1:
                    temp.bottom = tempB
                    preB = tempB
                    flag1 = 0
                else:
                    preB.bottom = tempB
                    preB = tempB
        root = flatten(head)
        printList(root)
        t-=1