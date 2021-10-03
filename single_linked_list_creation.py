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

    def insertion(self, nodeval, loc=None):
        node = Node(nodeval)
        if not self.head:#empty list
            self.head = node
            self.tail = node
        else:#not empty , check which location we need to enter
            if loc == 'first':
                #at begining
                node.next = self.head
                self.head = node
            elif loc == 'end':
                self.tail.next = node
                self.tail = node
            else:
                start = self.head
                pos = 1
                while pos<loc:
                    start = start.next
                    pos+=1
                node.next = start.next
                start.next = node

    def display(self):
        start = self.head
        while start:
            print(start.value, end=" ")
            start = start.next

singlyList = SLinkedList()
#create 2 nodes
node1 = Node(1)
node2 = Node(2)

singlyList.head = node1
singlyList.head.next = node2
singlyList.tail = singlyList.head.next

newSingly = SLinkedList()
newSingly.insertion(0)
newSingly.insertion(5,'first')
newSingly.insertion(9,'end')
newSingly.insertion(11,1)
newSingly.insertion(41,'end')
newSingly.insertion(21,'first')
newSingly.insertion(15,4)
newSingly.display()