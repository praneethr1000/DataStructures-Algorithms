class BinaryHeap:
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)

    def parent(self,i):
        return (i - 1) // 2

    def left(self,i):
        return (2 * i) + 1

    def right(self,i):
        return (2 * i) + 2

    def get(self,i):
        return self.items[i]

    def getMax(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def getMin(self):
        if self.size() == 0:
            return None
        return self.items[0]

    def extract_max(self):
        if self.size() == 0:
            return None
        largest = self.getMax()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.max_heapify(0)
        return largest

    def extract_min(self):
        if self.size() == 0:
            return None
        smallest = self.getMin()
        self.items[0] = self.items[-1]
        del self.items[-1]
        self.min_heapify(0)
        return smallest

    def max_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        if l <= self.size() - 1 and self.get(l) > self.get(i):
            largest = l
        else:
            largest = i
        if r <= self.size() - 1 and self.get(r) > self.get(largest):
            largest = r
        if largest != i:
            self.swap(i,largest)
            self.max_heapify(largest)

    def min_heapify(self,i):
        l = self.left(i)
        r = self.right(i)
        smallest = i
        if l < self.size() and self.get(l) < self.get(smallest):
            smallest = l
        if r < self.size() and self.get(r) < self.get(smallest):
            smallest = r
        if smallest != i:
            self.swap(i,smallest)
            self.min_heapify(smallest)

    def swap(self,i,j):
        self.items[i], self.items[j] = self.items[j], self.items[i]

    def insertMax(self,key):
        index = self.size()
        self.items.append(key)

        while index != 0:
            p = self.parent(index)
            if self.get(p) < self.get(index):
                self.swap(p, index)
            index = p

    def insertMin(self,key):
        index = self.size()
        self.items.append(key)

        while index != 0:
            p = self.parent(index)
            if self.get(p) > self.get(index):
                self.swap(p, index)
            index = p

maxheap = BinaryHeap()
for i in range(1,8):
    maxheap.insertMax(i)
minheap = BinaryHeap()
for i in range(7,0,-1):
    minheap.insertMin(i)
for i in range(7):
    print(maxheap.extract_max())
    print(maxheap.items)
for i in range(7):
    print(minheap.extract_min())
    print(minheap.items)










