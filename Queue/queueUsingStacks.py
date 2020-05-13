class Queue:
    def __init__(self):
        self.stk1 = []
        self.stk2 = []

    def enqueue(self,item):
        self.stk1.append(item)

    def dequeue(self):
        if not self.stk2:
            while self.stk1:
                self.stk2.append(self.stk1.pop())
        return self.stk2.pop()

q = Queue()
for i in range(1,5):
    q.enqueue(i)
for i in range(1,5):
    print(q.dequeue())


