'''
Singly Linked List DS
All elements are linked
to each other.
'''

class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class SLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None


singlyList = SLinkedList()
#create 2 nodes
node1 = Node(1)
node2 = Node(2)

singlyList.head = node1
singlyList.head.next = node2
singlyList.tail = singlyList.head.next