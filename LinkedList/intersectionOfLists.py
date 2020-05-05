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

    def length(self):
        count = 0
        current = self.head
        while current:
            count += 1
            current = current.next
        return count

    def intersection(self,length1,length2,head1,head2):
        diff = abs(length1-length2)
        if length1 > length2:
            for i in range(diff):
                head1 = head1.next
        elif length2 > length1:
            for i in range(diff):
                head2 = head2.next
        while head1 != head2:
            head1 = head1.next
            head2 = head2.next
        return head1

