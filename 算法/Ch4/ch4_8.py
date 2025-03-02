class Queue:
    def __init__(self,capacity):
        self.queue = []
        self.capacity = capacity
    def isEmpty(self):
        return self.size() == 0
    def size(self):
        return len(self.queue)
    def isFull(self):
        return self.size() == self.capacity
    def enqueue(self,data):
        if self.isFull():
            print("滿")
            return
        self.queue.append(data)
    def dequeue(self):
        if self.isEmpty():
            print("空")
            return None
        return self.queue.pop(0)
queue = Queue(3)
queue.enqueue("A")
queue.enqueue("B")
queue.enqueue("C")
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())

