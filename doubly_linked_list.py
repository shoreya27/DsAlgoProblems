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