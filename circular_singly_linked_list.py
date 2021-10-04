'''
Circular singly linked list
Creation takes O(1)
and space complexity is O(1)
'''
from single_linked_list_creation import Node

class CircularLinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def create_ll(self, nodeval):
        node = Node(nodeval)
        node.next = node
        self.head = node
        self.tail = node
    
    def display(self):
        start = self.head
        print("[", end=" ")
        while start:
            print(start.value, end=" ")
            start = start.next
            if start == self.head:
                break
        print("]")

circular_ll = CircularLinkedList()
circular_ll.create_ll(4)
circular_ll.display()