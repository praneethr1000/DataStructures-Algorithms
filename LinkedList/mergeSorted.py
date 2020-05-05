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

    def sorting(self,head1,head2):
        if head1.data < head2.data:
            temp = Node(head1.data)
        else:
            temp = Node(head2.data)
        while head1 != None and head2 != None:
            if head1.data < head2.data:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next
        if head1 == None:
            temp.next = head2
        else:
            temp.next = head1
        self.head1 = temp
        self.display()

    def display(self):
        current = self.head
        while current.next != None:
            print(current.data,end="->")
            current = current.next
        print(current.data)

l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(4)
l.display()

l1 = LinkedList()
l1.insertion(3)
l1.insertion(5)
l1.display()

l.sorting(l.head,l1.head)




