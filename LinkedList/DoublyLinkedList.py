class Node:
    def __init__(self,data):
        self.data = data
        self.previous = None
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeg(self,data):
        node = Node(data)
        node.next = self.head
        self.head.previous = node
        self.head = node

    def insertAtEnd(self,data):
        node = Node(data)
        current = self.head
        while current.next != None:
            current = current.next
        current.next = node
        node.previous = current

    def insertAtPos(self,data,pos):
        node = Node(data)
        current = self.head
        count = 0
        while count < pos-1:
            count += 1
            current = current.next
        node.next = current.next
        current.next.previous = node
        node.previous = current
        current.next = node

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
            self.head.previous = None
            current = None
        else:
            current = self.head
            count = 0
            while count < pos:
                count += 1
                if pos == count:
                    current.previous.next = current.next
                    current.next.previous = current.previous
                    current = None
                else:
                    current = current.next

    def insertion(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            node = Node(data)
            current = self.head
            while current.next != None:
                current = current.next
            current.next = node
            node.previous = current


l = DoublyLinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
l.insertAtEnd(6)
l.insertAtBeg(0)
l.insertAtPos(5,4)
l.display()
l.deleteNode(2)
l.display()





