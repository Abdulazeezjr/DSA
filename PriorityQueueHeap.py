class PriorityQueueHeap:
    def __init__(self):
        self.array = []

    def upheapify(self, n):
        if n == 0:
            return
        root = (n - 1) // 2
        if self.array[n] < self.array[root]:
            self.array[n],self.array[root] = self.array[root], self.array[n]
            self.upheapify(root)

    def downheapify(self, n):
        left = (2 * n) + 1
        right = (2 * n) + 2
        smallest = n
        
        # make sure we have a left and a right and compare them with the smallest
        if left < len(self.array) and self.array[left] < self.array[smallest]:
            smallest = left
        if right < len(self.array) and self.array[right] < self.array[smallest]:
            smallest = right
        
        # make sure smallest is not our original, if not it will run forever
        if smallest != n:
            self.array[n], self.array[smallest] = self.array[smallest], self.array[n]
            self.downheapify(smallest)

    def remove_min(self):
        if len(self.array) == 0:
            raise IndexError("Heap is empty")
       
        self.array[0], self.array[-1] = self.array[-1], self.array[0]
        min = self.array.pop(-1)
        self.downheapify(0)
        return min

    def insert(self,n):
        self.array.append(n)
        self.upheapify(len(self.array) - 1)

    def show(self):
        print(self.array)

pq = PriorityQueueHeap()
pq.insert(3)
pq.insert(2)
pq.insert(4)
pq.insert(5)
pq.insert(0)
pq.insert(1)
pq.insert(20)
pq.insert(8)
pq.insert(12)
pq.insert(6)
pq.insert(7)
print(pq.remove_min())
pq.show()

