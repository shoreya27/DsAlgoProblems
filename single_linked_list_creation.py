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
    
    def traversal(self):
        '''
        Traversing a SL
        takes O(n) time complexity
        and space complexity is O(1)
        '''
        start = self.head
        while start:
            print(start.value)
            start = start.next
    
    '''
    Searching value in
    Linked List
    '''
    def search(self, value):
        #check head
        if not self.head:
            print("Empty List")
            return
        start = self.head
        index = 1
        while start:
            if start.value == value:
                print(f"{value} is located at {index}")
                return
            start = start.next
            index += 1
        print(f"{value} is not present in list")
        return
    
    def deletion(self, loc):
        if not self.head:
            print("list is already empty!")
            return
        if loc == 0:#remove from begining
            if not self.head.next:
                self.head = None
                self.tail = None
            else:
                self.head = self.head.next
            return
        elif loc == -1:#remove from end
            if not self.head.next:
                self.head = None
                self.tail = None
            else:
                start = self.head
                while start.next.next:
                    start = start.next
                start.next = None
                self.tail = start
            return
        else:
            start = self.head
            pos = 1
            while pos<loc-1:
                start = start.next
                pos+=1
            start.next = start.next.next
            return
    
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
print()
# print("***************")
# newSingly.traversal()
# print("***************")
# print("........SEARCHING...........")
# newSingly.search(15)
# newSingly.search(41)
# newSingly.search(110)

newSingly.deletion(0)
newSingly.display()
print()
newSingly.deletion(4)
print("deleting the 4th index")
newSingly.display()
print()
print("deleting last element")
newSingly.deletion(-1)
newSingly.display()
print()
newSingly.deletion(-1)
newSingly.display()
newSingly.deletion(2)
print()
newSingly.display()