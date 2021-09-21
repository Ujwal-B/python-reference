import sys
class Queue:
    def __init__(self, size):
        self.queue = []
        self.size = size

    def isEmpty(self):
        return len(self.queue) == 0

    def isFull(self):
        return len(self.queue) == self.size

    def enqueue (self, item):
        if self.isFull():
            print("Queue is full")
        else:
            print(item, "is added to the queue")
            self.queue.append(item)

    def dequeue (self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queue[0], "is dequeued")
            self.queue.pop(0)

    def display(self):
        if self.isEmpty():
            print("Queue is empty")
        else:
            print(self.queue)

q = Queue(10)

q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
q.enqueue(90)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.display()
q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
q.enqueue(90)
q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
q.enqueue(90)
q.display()
q.enqueue(10)
q.enqueue(20)
q.enqueue(40)
q.enqueue(90)
q.display()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
q.dequeue()
    