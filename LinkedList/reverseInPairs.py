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

    def reverseInpairs(self,pairs_count,head):
        count = 0
        current = head
        previous = None
        nextNode = None
        while current is not None and count < pairs_count:
            count += 1
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode

        if nextNode is not None:
            head.next = self.reverseInpairs(pairs_count,nextNode)

        return previous


l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
l.insertion(5)
l.insertion(6)
l.head = l.reverseInpairs(3,l.head)
l.display()

