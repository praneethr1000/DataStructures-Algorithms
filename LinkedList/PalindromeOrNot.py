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

    def palindrome(self):
        slow_ptr = self.head
        fast_ptr = self.head
        while fast_ptr != None and fast_ptr.next != None:
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        middle = slow_ptr
        second_half = self.reverse(slow_ptr.next)
        temp = self.head
        while second_half != None:
            if temp.data != second_half.data:
                return False
            temp = temp.next
            second_half = second_half.next
        return True


    def reverse(self,temp):
        current = temp
        previous = None
        while current != None:
            nextNode = current.next
            current.next = previous
            previous = current
            current = nextNode
        return previous


l = LinkedList()
l.insertion(1)
l.insertion(2)
l.insertion(3)
l.insertion(4)
l.insertion(3)
l.insertion(2)
l.insertion(0)
print(l.palindrome())