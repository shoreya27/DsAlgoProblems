class Stack:

    def __init__(self):
        self.list = []
    
    def __str__(self):
        return "\n".join(self.list[::-1])

    #isempty
    def isEmpty(self):
        if not self.list:
            return True
        return False

    #push
    def push(self, value):
        self.list.append(value)

    #pop
    def pop(self):
        if self.isEmpty():
            print("Stack is empty")
            return
        return self.list.pop()
    
    #delete
    def delete(self):
        self.list = []
    
    #peek
    def peek(self):
        if self.isEmpty():
            print("stack is empty")
            return
        return self.list[-1]

books = Stack()
# print(books.isEmpty())
books.push("The compound effect")
books.push("Swami Vivekanand On Himself")
books.push("The Psychology of money")
# print(books)

#------------Pop-----------------------#
print(books.pop())
print(books.pop())
# print(books.pop())
# print(books.pop())
print("............")
print(books.peek())
print("...........")
print(books)