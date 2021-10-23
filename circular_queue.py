class CircularQueue:

    def __init__(self, size):
        self.list = [None]*size
        self.start = -1
        self.top = -1

    def __str__(self) -> str:
        return " ".join(map(str, self.list))

    def isEmpty(self):
        if self.list[self.start] is None:
            return True
        return False
    
    def isFull(self):
        if None in self.list:
            return False
        return True
    
    def enqueue(self, value):
        if self.isEmpty():
            self.list[0] = value
            self.start += 1
            self.top += 1
        elif self.isFull():
            print("list is full")
        else:
            if self.top == len(self.list) - 1:
                self.top = 0
                self.list[self.top] = value
            else:
                self.top += 1
                self.list[self.top] = value

    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        val = self.list[self.start]
        self.list[self.start] = None
        if self.start == len(self.list) - 1:
            self.start = 0
        else:
            self.start +=1
        return val
    
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.list[self.start]
    
    def delete(self):
        self.list = []
        self.start = -1
        self.top = -1

order = CircularQueue(3)
print(order)
order.enqueue(5)
print(order)
order.enqueue(7)
print(order)
order.enqueue(9)
print(order)
order.enqueue(11)
print(order)
print(order.start, order.top)
print("-----------------------")
print("First Order:",order.dequeue())
print("second Order:",order.dequeue())
print("||||||||QUEUE||||||||||||")
print(order)
print(order.start, order.top)
order.enqueue(2)
order.enqueue(4)
order.enqueue(6)
print(order)
print(order.start, order.top)
print("3rd order:",order.dequeue())
print(order)
print(order.start, order.top)
print("4th order:",order.dequeue())
print("5th order:",order.dequeue())
print(order)
print(order.start, order.top)
