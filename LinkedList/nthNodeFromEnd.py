class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertion(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            current = self.head
            while current.next != None:
                current = current.next
            current.next = Node(data)

    def display(self):
        current = self.head
        while current.next != None:
            print(current.data,end="->")
            current = current.next
        print(current.data)

    def nthNodeFromEnd(self,n):
        if n > 0:
            return None
        temp = self.head
        count = 0
        while count != n and temp != None:
            temp = temp.next
            count += 1
        if temp == None or count < n:
            return None
        pthNode = self.head
        while temp.next != None:
            pthNode = pthNode.next
            temp = temp.next
        return pthNode.data

l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
l.insertion(5)
l.insertion(6)
l.display()
print(l.nthNodeFromEnd(2))
