from single_linked_list_creation import SLinkedList

class Stack:

    def __init__(self):
        self.list = []
        self.min = 10000
        self.mins = SLinkedList()

    def isEmpty(self):
        if not self.list:
            return True
        return False

    def push(self, val):
        self.list.append(val)
        self.check_min(val)
    
    def check_min(self, val):
        if val < self.min:
            self.mins.insertion(val, 'first')
            self.min = val

    def pop_min(self, val):

        if val == self.mins.head.value:
            self.mins.head = self.mins.head.next
            self.min = self.mins.head.value

    def pop(self):
        if self.isEmpty():
            return "stack is empty"
        min_val = self.list.pop()
        self.pop_min(min_val)
        return min_val
    
    def get_min(self):
        return self.min

pages = Stack()
pages.push(10)
pages.push(20)
pages.push(30)
pages.push(5)
pages.push(2)
pages.push(220)
pages.push(-5)

print(pages.list)

print(".................")
print(pages.get_min())
print(pages.pop())
print(pages.pop())
print(pages.pop())
print(pages.pop())
print(".........")
print(pages.list)
print("..........")
print(pages.get_min())
print(pages.mins.display())

pages.push(2)
print(pages.get_min())

print(pages.mins.display())
pages.push(-2)

print(pages.get_min())
pages.pop()

print(pages.get_min())