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

    def sumOfLists(self,head1,head2):
        if head1 == None:
            return head2
        if head2 == None:
            return head1
        length1 = self.length(head1)
        length2 = self.length(head2)
        if length1 >= length2:
            longer = length1
            shorter = length2
        else:
            longer = length2
            shorter = length1
        sum = None
        carry = 0
    '''Yet to complete'''



    def length(self,head):
        count = 1
        while head != None:
            count += 1
            head = head.next
        return count




