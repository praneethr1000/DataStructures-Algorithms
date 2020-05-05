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

    def sortedInsertion(self,data):
        node = Node(data)
        current = self.head
        previous = None
        inserted = False
        while current != None and not inserted:
            if current.data > data:
                inserted = True
            else:
                previous = current
                current = current.next
        if previous == None:
            node.next = self.head
            self.head = node
        else:
            node.next = previous.next
            previous.next = node

l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(4)
l.display()
l.sortedInsertion(3)
l.sortedInsertion(5)
l.display()
