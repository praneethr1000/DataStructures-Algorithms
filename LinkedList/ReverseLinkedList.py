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

    def reverse(self):
        current = self.head
        previous = None
        while current != None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        self.head = previous


    def reverseRecursively(self,temp):
        if temp != None:
            right = temp.next
            if temp != self.head:
                temp.next = self.head
                self.head = temp
            else:
                temp.next = None
            self.reverseRecursively(right)

l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(4)
l.display()
l.reverseRecursively(l.head)
l.display()
