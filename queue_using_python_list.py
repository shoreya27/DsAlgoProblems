class Queue:

    def __init__(self):
        self.list = []
    
    def isEmpty(self):
        if not self.list:
            return True
        return False
    
    def enqueue(self, value):
        self.list.append(value)
    
    def __str__(self):
        return " ".join(map(str,self.list))
    
    def dequeue(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        return self.list.pop(0)

    def peek(self):
        if self.isEmpty():
            print("Empty Queue")
            return
        return self.list[0]

    def delete(self):
        self.list = []

orders = Queue()
print(orders.isEmpty())#true
orders.enqueue(4)
orders.enqueue(8)
orders.enqueue(12)
print(orders)
print(f"pop first element:{orders.dequeue()}")
print("Now Remaining queue is:", orders)
print(f"pop second element:{orders.dequeue()}")
# orders.dequeue()
# orders.dequeue()
# print(orderss)
print(orders.peek())
orders.delete()
print(orders)