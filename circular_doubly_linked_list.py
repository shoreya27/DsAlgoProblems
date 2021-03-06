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
            if start:
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

    def searching(self, nodeVal):
        if not self.head:
            print("list is empty")
            return
        start = self.head
        while start:
            if start.value == nodeVal:
                print("element found")
                return
            if start == self.tail:
                print("element does not exist")
                return
            start = start.next

    def deletion(self,loc):
        if not self.head:
            print("list is already empty")
            return
        if loc == 0:#from the begining
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = self.tail
                self.tail.next = self.head
        elif loc == -1:#from the end
            if self.head == self.tail:
                self.head.next = None
                self.head.prev = None
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = self.head
                self.head.prev = self.tail
        else:
            start = self.head
            count = 1
            while count < loc-1:
                start = start.next
                count += 1
            start.next = start.next.next
            start.next.prev = start
        self.display()
        return

    def delete_cdll(self):
        if not self.head:
            print("list is already empty!")
            return
        self.tail.next = None
        start = self.head
        while start:
            start.prev = None
            start = start.next
        self.head = None
        self.tail = None
        self.display()

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
songs.searching(55)
songs.searching(105)
songs.searching(12)

songs.deletion(1)
songs.deletion(-1)
songs.deletion(5)
songs.deletion(10)

songs.delete_cdll()