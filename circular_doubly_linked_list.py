class Node:

    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class CircularDoublyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
    
    def __iter__(self):
        start = self.head
        while True:
            yield start.value
            if start == self.head:
                break
            start = start.next
    
    def display(self):
        lst = [element for element in self]
        print(lst)
    
    def creation(self, nodeval):
        node = Node(nodeval)
        self.head = self.tail = node
        node.next = node.prev = node
    
songs = CircularDoublyLinkedList()
songs.creation(1)
songs.display()