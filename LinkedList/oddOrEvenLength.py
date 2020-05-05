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

    def odd(self):
        temp = self.head
        while temp != None and temp.next != None:
            temp = temp.next.next
            if temp == None:
                return 0
        return 1

l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
if l.odd() == 1:
    print("odd")
else:
    print("even")