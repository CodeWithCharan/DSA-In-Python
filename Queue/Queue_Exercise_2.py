from collections import deque

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self, val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        return self.buffer.pop()
    
    def front(self):
        return self.buffer[-1]
    
def produce_binary_numb(n):
    add = Queue()
    add.enqueue("1")

    for i in range(n):
        front_numb = add.front()
        print(front_numb)
        add.enqueue(front_numb+"0")
        add.enqueue(front_numb+"1")
        add.dequeue()

if __name__ == '__main__':
    produce_binary_numb(10)