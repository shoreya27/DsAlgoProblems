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
        lst = [node.value for node in music]
        print(lst)

music = DoublyLinkedList()
music.create(1)
music.display()