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

    def sumOfElements(self,temp):
        if temp == None:
            return 0
        else:
            return temp.data + self.sumOfElements(temp.next)



l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
l.display()
print(l.sumOfElements(l.head))