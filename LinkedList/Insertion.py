class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeg(self,data):
        node = Node(data)
        node.next = self.head
        self.head = node

    def insertAfter(self,data,pos):
        node = Node(data)
        if pos == 0:
            self.head = node
        else:
            count = 0
            current = self.head
            while count < pos-1:
                count += 1
                current = current.next
            node.next = current.next
            current.next = node

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

    def deleteNode(self,pos):
        if pos == 1:
            current = self.head
            self.head = current.next
            current = None
        else:
            count = 0
            current = self.head
            previous = self.head
            while count < pos:
                count += 1
                if pos == count:
                    previous.next = current.next
                    current = None
                    return
                else:
                    previous = current
                    current = current.next


l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(4)
l.insertAtBeg(0)
l.insertAfter(3,3)
l.insertAfter(5,5)
l.display()
l.deleteNode(1)
l.display()




