class Node:

    def __init__(self, value) -> None:
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
    

    def __iter__(self):
        start = self.head
        while start:
            yield start
            start = start.next
    
    #creation operation
    '''
    Creation of DLL
    takes O(1) time and space
    '''
    def create(self, nodeVal):
        node = Node(nodeVal)
        self.head = node
        self.tail = node

    def display(self):
        lst = [node.value for node in self]
        print(lst)

    '''
    Insertion of a node
    can be done at 3 diff locations
    In begining , In End, Or at given location
    '''
    def insertion(self, nodeVal, loc):
        if not self.head:
            print("List does not exist")
            return
        node = Node(nodeVal)
        if loc == 0:#in begining
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif loc == -1:#at end
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            start = self.head
            count = 1
            while count < loc:
                start = start.next
                count += 1
            node.next = start.next
            node.prev = start.next.prev
            start.next.prev = node
            start.next = node
        self.display()
        return

    def traversal(self):
        if not self.head:
            print("List is empty!")
            return
        start = self.head
        while start:
            print(start.value)
            start = start.next

    def reverse_traversal(self):
        if not self.head:
            print("Linked List is empty")
            return
        start = self.tail
        while start:
            print(start.value)
            start = start.prev
    
    def searching(self, nodeVal):
        if not self.head:
            print("list is empty")
            return
        start = self.head
        while start:
            if start.value == nodeVal:
                print(f"{nodeVal} is present in list")
                return
            start = start.next
        print(f"{nodeVal} is not there in the list")
        return

    def deletion(self, loc):
        if not self.head:
            print("Linked List is empty")
            return
        if loc == 0:#delete from begining
            if not self.head.next:#single node
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
        elif loc == -1:
            if not self.head.next:#single node
                self.head = self.tail = None
            else:
                self.tail = self.tail.prev
                self.tail.next = None
        else:
            start = self.head
            count = 1
            while count < loc-1:
                start = start.next
                count += 1
            start.next = start.next.next
            start.next.prev = start
        self.display()

    def delete_complete_list(self):
        if not self.head:
            print("list is empty")
            return
        start = self.head
        while start:
            start.prev = None
            start = start.next
        self.head = None
        self.tail = None

music = DoublyLinkedList()
music.create(1)
music.display()
music.insertion(0,0)
music.insertion(2,-1)
music.insertion(5,-1)
music.insertion(3,3)
music.insertion(50,-1)
for i in range(6,50):
    music.insertion(i,i-1)

music.traversal()
print("-------------------Reversing----------------")
music.reverse_traversal()

music.searching(15)
music.searching(150)

books = DoublyLinkedList()
books.deletion(1)
books.create(10)
for i in range(11,21):
    books.insertion(i,-1)

books.deletion(0)
books.deletion(3)
books.deletion(-1)

books.delete_complete_list()
books.display()