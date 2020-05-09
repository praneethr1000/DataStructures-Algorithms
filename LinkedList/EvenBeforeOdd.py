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

    def evenBeforeOdd(self):
        oddList = evenList = None
        oddListEnd = evenListEnd = None
        temp = self.head
        while temp != None:
            if temp.data % 2 == 0:
                if evenList == None:
                    evenList = evenListEnd = temp
                else:
                    evenListEnd.next = temp
                    evenListEnd = temp
            else:
                if oddList == None:
                    oddList = oddListEnd = temp
                else:
                    oddListEnd.next = temp
                    oddListEnd = temp
            temp = temp.next
        oddListEnd.next = None
        evenListEnd.next = oddList
        self.head = evenList

l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
l.display()
l.evenBeforeOdd()
l.display()
