class Node:

    def __init__(self, val):
        self.value = val
        self.next = None

class Queue:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def isEmpty(self):
        if not self.head:
            return True
        return False
    
    def __str__(self):
        start = self.head
        while start:
            print(start.value, end= " ")
            start = start.next
        return ""
    def enqueue(self, val):
        node = Node(val)
        if self.isEmpty():
            self.head = self.tail = node
        else:
            self.tail.next = node
            self.tail = node
    
    def dequeue(self):
        if self.isEmpty():
            print("queue is empty")
            return
        val = self.head.value
        self.head = self.head.next
        return val
    
    def peek(self):
        if self.isEmpty():
            print("queue is empty")
            return
        return self.head.value
    
    def delete(self):
        self.head = self.tail = None

roll_no = Queue()
# print(roll_no)
roll_no.enqueue(1)
roll_no.enqueue(2)
roll_no.enqueue(3)
roll_no.enqueue(4)
print(roll_no)

print(f"1st roll no:{roll_no.dequeue()}")
print(f"2nd roll no:{roll_no.dequeue()}")
print(".............")
print(roll_no)

roll_no.enqueue(5)
roll_no.enqueue(6)
roll_no.enqueue(7)

print(roll_no)

print(roll_no.peek())

roll_no.delete()
print(roll_no)