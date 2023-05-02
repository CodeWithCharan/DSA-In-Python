from collections import deque
import time
import threading

class Queue:
    def __init__(self):
        self.buffer = deque()

    def enqueue(self,val):
        self.buffer.appendleft(val)

    def dequeue(self):
        if len(self.buffer) == 0:
            print("Queue is empty")
            return
        
        return self.buffer.pop()
    
    def isempty(self):
        return len(self.buffer) == 0
    
    def size(self):
        return len(self.buffer)
    
food_order = Queue()

def PlaceOrder(orders):
    for n in orders:
        print("Placing order for ",n)
        food_order.enqueue(n)
        time.sleep(0.5)

def ServeOrder(orders):
    time.sleep(1)
    while True:
        if food_order.isempty():
            print("All items Served")
            break
        
        order = food_order.dequeue()
        print("Serving order: ",order)
        time.sleep(2)

if __name__ == '__main__':
    orders = ['pizza','samosa','pasta','biryani','burger']

    t1 = threading.Thread(target=PlaceOrder, args=(orders,))
    t2 = threading.Thread(target=ServeOrder, args=(orders,))

    t1.start()
    t2.start()