class MultipleStack:

    def __init__(self, number_of_stacks) -> None:
        
        self.stack_size = 3
        self.list = [0] * (self.stack_size * number_of_stacks)
        self.each_stack_len = [0]*number_of_stacks
        self.top_index = [0]*number_of_stacks
    
    def isEmpty(self, stack_num):

        stack_count = self.each_stack_len[stack_num]
        if stack_count == 0:
            return True
        return False
    
    def isFull(self, stack_num):
        
        stack_count = self.each_stack_len[stack_num]
        if stack_count == self.stack_size:
            return True
        return False
    
    def topIndexVal(self, stack_num):
        offset = stack_num * self.stack_size
        return offset + self.each_stack_len[stack_num]
    
    def push(self, stack_num, val):
        if self.isFull(stack_num):
            return "stack is full"
        get_top_index = self.topIndexVal(stack_num)
        # print(f"...{get_top_index}"s)
        self.list[get_top_index] = val
        self.each_stack_len[stack_num] += 1

    def pop(self, stack_num):
        if self.isEmpty(stack_num):
            return "stack is empty"
        top_index = self.topIndexVal(stack_num) -1
        val = self.list[top_index]
        self.list[top_index] = None
        self.each_stack_len[stack_num] -= 1
        return val


books = MultipleStack(2)
print(books.isEmpty(0))#zero stack will be  ---- >true
print(books.isFull(0))#zero stack will not be full ---> false
print(books.push(0,"a"))
print(books.push(1,"d"))
# print(books.list)
print(books.push(0,"b"))
print(books.push(1,"e"))
print(books.push(0,"c"))
print(books.push(1,"f"))
print(books.list)
print(books.push(0,"h"))

print(books.each_stack_len)

print(books.pop(0))
print(books.pop(1))
print(books.pop(0))
print(books.pop(1))
print(books.pop(0))
print(books.pop(1))
print(books.pop(0))
print(books.pop(1))

print(books.each_stack_len)

print(".................ROUND2......................")
print(books.push(0,"a"))
print(books.push(1,"d"))
# print(books.list)
print(books.push(0,"b"))
print(books.push(1,"e"))
print(books.push(0,"c"))
print(books.push(1,"f"))
print(books.list)
print(books.push(0,"h"))