class Node:

    def __init__(self, val) -> None:
        self.value = val
        self.next = None

    def __str__(self):
        return str(self.value)


class LinkedList:

    def __init__(self) -> None:
        self.head = None
        self.tail = None
    
    def __iter__(self):
        start = self.head
        while start:
            yield start
            start = start.next
    
    def __str__(self):
        lst = [str(element.value) for element in self]
        return '->'.join(lst)
    
    def __len__(self):
        lst = [element.value for element in self]
        return len(lst)
    
    def add(self,nodeval):
        node = Node(nodeval)
        if not self.head:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

