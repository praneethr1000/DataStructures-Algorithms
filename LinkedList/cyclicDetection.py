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

    def cyclicDetection(self):
        fast = slow = self.head
        while fast != None and slow != None:
            fast = fast.next
            if slow == fast:
                cycleRemoval(fast,slow)
                return True
            if fast.next == None:
                return False
            fast = fast.next
            if slow == fast:
                cycleRemoval(fast, slow)
                return True
            slow = slow.next
        return False

    def cycleRemoval(self,fast,slow):
        slow = self.head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return fast

    def lengthOfLoop(self,fast,slow):
        count = 0
        while fast != slow:
            count += 1
            fast = fast.next
