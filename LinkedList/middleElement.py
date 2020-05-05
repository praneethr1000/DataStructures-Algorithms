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
            print(current.data,end= "->")
            current = current.next
        print(current.data)

    def middle(self):
        fast = slow = self.head
        while fast != None:
            fast = fast.next
            if fast == None:
                return slow
            fast = fast.next
            slow = slow.next
        return slow

l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
l.display()
print(l.middle().data)
