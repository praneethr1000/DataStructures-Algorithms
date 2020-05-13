class Queue:
    def __init__(self, limit):
        self.que = []
        self.limit = limit
        self.front = None
        self.rear = None
        self.size = 0

    def isEmpty(self):
        return self.size <= 0

    def enqueue(self, item):
        if self.size >= self.limit:
            self.resize()
        self.que.append(item)
        if self.front == None:
            self.front = self.rear = 0
        else:
            self.rear = self.size
        self.size += 1
        print("Queue after enqueue",self.que)

    def dequeue(self):
        if self.size <= 0:
            print("Queue underflow")
            return 0
        else:
            self.que.pop(0)
            self.size -= 1
            if self.size == 0:
                self.front = self.rear = None
            else:
                self.rear = self.size - 1
            print("Queue after dequeue",self.que)

    def queueRear(self):
        if self.rear == None:
            print("Queue is empty")
            raise IndexError
        return self.que[self.rear]

    def queueFront(self):
        if self.front == None:
            print("Queue is empty")
            raise IndexError
        return self.que[self.front]

    def size(self):
        return self.size

    def resize(self):
        newQue = list(self.que)
        self.limit = 2*self.limit
        self.que = newQue

que = Queue(5)
que.enqueue(1)
print("Front",que.front)
print("Rear",que.rear)
que.enqueue(2)
print("Front",que.front)
print("Rear",que.rear)
que.enqueue(3)
print("Front",que.front)
print("Rear",que.rear)
que.enqueue(4)
print("Front",que.front)
print("Rear",que.rear)
que.enqueue(5)
print("Front",que.front)
print("Rear",que.rear)
que.enqueue(6)
print("Front",que.front)
print("Rear",que.rear)
que.dequeue()
print("Front",que.front)
print("Rear",que.rear)
que.dequeue()
print("Front",que.front)
print("Rear",que.rear)








