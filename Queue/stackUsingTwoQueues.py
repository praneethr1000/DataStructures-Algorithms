class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self,item):
        self.queue.append(item)

    def dequeue(self):
        return self.queue.pop(0)

    def size(self):
        return len(self.queue)

    def empty(self):
        return self.queue == []

class Stack:
    def __init__(self):
        self.q1 = Queue()
        self.q2 = Queue()

    def isEmpty(self):
        return self.q1.empty() and self.q2.empty()

    def push(self,item):
        if self.q2.empty():
            self.q1.enqueue(item)
        else:
            self.q2.enqueue(item)

    def pop(self):
        if self.q2.empty():
            for i in range(self.q1.size()-1):
                self.q2.enqueue(self.q1.dequeue())
            return self.q1.dequeue()
        else:
            for i in range(self.q2.size()-1):
                self.q1.enqueue(self.q2.dequeue())
            return self.q2.dequeue()

stk = Stack()
for i in range(5):
    stk.push(i)
for i in range(5):
    print(stk.pop())
