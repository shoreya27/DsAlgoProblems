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
            if start == self.tail:
                break
            start = start.next
    
    def display(self):
        lst = [element for element in self]
        print(lst)
    
    def creation(self, nodeval):
        node = Node(nodeval)
        self.head = self.tail = node
        node.next = node.prev = node
    
    def insertion(self, nodeval, loc):
        if not self.head:
            print("list is empty")
            return
        node = Node(nodeval)
        if loc == 0:#in begining
            node.next = self.head
            node.prev = self.tail
            self.head.prev = node
            self.head = node
            self.tail.next = node
        elif loc == -1:#at the end
            node.next = self.head
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
            self.head.prev = node
        else:
            start = self.head
            count = 1
            while count < loc-1:
                start = start.next
                count += 1
            node.next = start.next
            node.prev = start
            start.next.prev = node
            start.next = node
        self.display()
    
    def traversal(self):
        if not self.head:
            print("list is empty")
            return
        start = self.head
        while start:
            print(start.value)
            if start == self.tail:
                break
            start = start.next

    def reverse_traversal(self):
        if not self.head:
            print("list is empty")
            return
        start = self.tail
        while start:
            print(start.value)
            if start == self.head:
                break
            start = start.prev


songs = CircularDoublyLinkedList()
songs.creation(1)
songs.display()
songs.insertion(0,0)
songs.insertion(100,-1)
songs.insertion(2,3)
for i in range(3,100):
    songs.insertion(i,i+1)

songs.traversal()
songs.reverse_traversal()