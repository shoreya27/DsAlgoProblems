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
    

roll_no = Queue()
# print(roll_no)
roll_no.enqueue(1)
roll_no.enqueue(2)
roll_no.enqueue(3)
roll_no.enqueue(4)
print(roll_no)