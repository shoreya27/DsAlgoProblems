class Stack:

    def __init__(self, maxSize) :
        self.maxsize = maxSize
        self.list = []
    
    def isEmpty(self):
        if not self.list:
            return True
        return False
    
    def isFull(self):
        if len(self.list) == self.maxsize:
            return True
        return False

    def __str__(self):
        return '\n'.join(map(str,self.list[::-1]))
    
    def push(self, value):
        if self.isFull():
            print("stack is already full")
            return
        self.list.append(value)
    
    def pop(self):
        if self.isEmpty():
            print("stack is already empty")
            return
        return self.list.pop()

    def peek(self):
        if self.isEmpty():
            print("stack is already empty")
            return
        return self.list[-1]


plates = Stack(2)
print(plates.isEmpty())
print(plates.isFull())
# print(plates)

plates.push(1)
plates.push(2)
print(plates)
# plates.push(3)

print(plates.pop())
print(plates.pop())
plates.pop()

print(plates.peek())