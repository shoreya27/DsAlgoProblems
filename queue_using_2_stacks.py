class Stack:

    def __init__(self) -> None:
        self.list = []
    
    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if self.list:
            return self.list.pop()
    
    def __len__(self):
        return len(self.list)

    def __str__(self):
        return ">".join(map(str, self.list[::-1]))

    def isEmpty(self):
        if self.list == []:
            return True
        return False

class QueueUsingStack:

    def __init__(self) -> None:
        self.push_stack = Stack()
        self.pop_stack = Stack()
    
    def __str__(self):
        print(self.push_stack.list)
        return ""

    def enqueue(self, val):
        if self.pop_stack:#move elements from this stack to push stack first
            while self.pop_stack:
                self.push_stack.push(self.pop_stack.pop())
        self.push_stack.push(val)

    def dequeue(self):
        if self.push_stack:
            while self.push_stack:
                self.pop_stack.push(self.push_stack.pop())
            
        print(self.pop_stack.pop())
queue = QueueUsingStack()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
queue.enqueue(4)
queue.enqueue(5)
queue.enqueue(6)


queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(7)
queue.enqueue(8)
queue.enqueue(9)

queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()
queue.dequeue()

queue.enqueue(10)
queue.enqueue(11)

print(queue)