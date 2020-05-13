class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stacks:
    def __init__(self):
        self.head = None
        self.minHead = None

    def insertMin(self,data):
        if self.minHead == None:
            self.minHead = Node(data)
        else:
            if data <= self.minHead.data:
                temp = Node(data)
                temp.next = self.minHead
                self.minHead = temp

    def insertion(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            temp = Node(data)
            temp.next = self.head
            self.head = temp
        self.insertMin(data)

    def minElement(self):
        return self.minHead.data

    def removeElement(self):
        temp = self.head
        data = temp.data
        self.head = self.head.next
        temp = None

        if self.minHead.data == data:
            temp = self.minHead
            self.minHead = self.minHead.next
            temp = None

    def display(self):
        temp = self.head
        while temp.next != None:
            print(temp.data,end = "->")
            temp = temp.next
        print(temp.data)

        temp = self.minHead
        while temp.next != None:
            print(temp.data,end = "->")
            temp = temp.next
        print(temp.data)

s = Stacks()
s.insertion(5)
s.insertion(2)
s.insertion(4)
s.insertion(6)
s.insertion(1)
s.display()
print(s.minElement())
s.removeElement()
s.removeElement()
s.display()
print(s.minElement())


