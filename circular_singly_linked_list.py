'''
Circular singly linked list
Creation takes O(1)
and space complexity is O(1)
'''
# from single_linked_list_creation import Node


class Node:
    
    def __init__(self, value) -> None:
        self.value = value
        self.next = None
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

    def insertion(self, nodeval, loc):
        #check linkedlist exist
        if not self.head:
            print("Linked List does not exist")
            return
        node = Node(nodeval)
        if loc == 0:#at very begining
            node.next = self.head
            self.head = node
            self.tail.next = node
        elif loc == -1:#at very end
            node.next = self.tail.next
            self.tail.next = node
            self.tail = node
        else:#find the location and loop 1 node before location where to insert
            start = self.head
            count = 1
            while count < loc:
                start = start.next
                count += 1
            node.next = start.next
            start.next = node
        self.display()

circular_ll = CircularLinkedList()
circular_ll.create_ll(1)
circular_ll.display()
#insert 0 at begining
circular_ll.insertion(0, 0)
#insert 10 at last
circular_ll.insertion(10,-1)
#insert 2-9 in circular_ll
for i in range(2,10):
    circular_ll.insertion(i,i)