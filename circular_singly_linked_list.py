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

    def traversal(self):
        if not self.head:
            print("linked list is empty")
            return
        start = self.head
        print("[ ")
        while True:
            print(start.value, end=" ")
            start = start.next
            if start == self.head:
                break
        print(" ]")
    
    def searching(self, val):
        if not self.head:
            print("Linked List is empty")
        start = self.head
        while True:
            if start.value == val:
                print(f"{val} exist in CLL")
                return
            start = start.next
            if start == self.head:
                break
        print(f"{val} does not exist")
        return 

    def deletion(self, loc):
        if not self.head:
            print("List is empty!")
            return
        if loc == 0:#beginning
            if self.head.next == self.head:#only 1 element present
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.tail.next = self.head
        elif loc == -1:#remove from the end
            if self.head.next == self.head:#only 1 element present
                self.head = self.tail = None
            else:
                start = self.head
                while True:
                    start = start.next
                    if start.next == self.tail:
                        break
                start.next = self.head
                self.tail = start
        else:
            start = self.head
            count = 1
            while count < loc-1:
                start = start.next
                count += 1
            start.next = start.next.next
        self.display()
        return
        
    def remove_entire_linkd_lst(self):
        self.tail.next = None
        self.head = None
        self.tail = None
        self.display()
        return
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

new_circularr = CircularLinkedList()
# new_circularr.traversal()
# new_circularr.insertion(0,0)
new_circularr.create_ll(100)
# new_circularr.traversal()
for i in range(99,0,-1):
    new_circularr.insertion(i,-1)
new_circularr.traversal()
new_circularr.searching(77)
new_circularr.searching(150)
new_circularr.searching(1)
print("-----------------------------")
new_circularr.display()
print("-----------------------------")
new_circularr.deletion(0)
new_circularr.deletion(-1)
new_circularr.deletion(10)
new_circularr.remove_entire_linkd_lst()