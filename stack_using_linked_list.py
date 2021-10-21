class Node:

    def __init__(self, value):
        self.value = value
        self.next = None

class Stack:

    def __init__(self) -> None:
        self.head = None
    
    def isEmpty(self):
        if not self.head:
            return True
        return False
    
    def push(self, val):
        node = Node(val)
        node.next = self.head
        self.head = node
    
    def __str__(self):
        start = self.head
        while start:
            print(start.value)
            start = start.next
        return ""
pages = Stack()
pages.push(4)
pages.push(10)
print(pages)