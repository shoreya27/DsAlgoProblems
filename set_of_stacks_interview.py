class Stack:

    def __init__(self) -> None:
        self.list = []
    
    def push(self, item):
        self.list.append(item)
    
    def pop(self):
        if self.list:
            return self.list.pop()
    
    def __len__(self):
        return len(self.list)

    def __str__(self):
        return ">".join(map(str, self.list[::-1]))

    def isEmpty(self):
        if self.list == []:
            return True
        return False

class SetOfStacks:

    def __init__(self) -> None:
        self.threshold = 5
        self.total_stacks = []
        self.current_stack = None
    
    def __str__(self):
        for i in self.total_stacks[::-1]:
            print(i, end=" ")
        return ""


    def check_threshold(self, st):
        if len(st) == self.threshold:
            return True
        return False
    
    def add_value(self, val):
        if not self.current_stack:
            # print(val)
            st = Stack()
            self.current_stack = st
            st.push(val)
            self.total_stacks.append(st)
        else:
            #check threshold
            if self.check_threshold(self.current_stack):
                # print(val)
                #create a new stack and push
                st = Stack()
                st.push(val)
                self.current_stack = st
                self.total_stacks.append(st)
            else:
                # print(val)
                self.current_stack.push(val)
        return ""
    def pop_value(self):
        if self.current_stack:
            if not self.current_stack.isEmpty():
                return f"Returned Value from stack is:{self.current_stack.pop()}"
        else:
                try:
                    self.total_stacks.pop()
                    self.current_stack = self.total_stacks[-1]
                    return f"Returned Value from stack is:{self.current_stack.pop()}"
                except:
                    self.current_stack = None
                    print("all stacks are empty")
        return ""

plates = SetOfStacks()
plates.add_value(1)
plates.add_value(2)
plates.add_value(3)
plates.add_value(4)
plates.add_value(5)
plates.add_value(6)
plates.add_value(7)
plates.add_value(8)
plates.add_value(9)
plates.add_value(10)
plates.add_value(16)
plates.add_value(17)
plates.add_value(18)
plates.add_value(19)
plates.add_value(20)
plates.add_value(21)

print(plates.pop_value())#21
print(plates.pop_value())#20
print(plates.pop_value())#19
print(plates.pop_value())#18
print(plates.pop_value())#17
print(plates.pop_value())#16
print(plates.pop_value())#10
print(plates.pop_value())#9
print(plates.pop_value())#8
print(plates.pop_value())#7
print(plates.pop_value())#6
print(plates.pop_value())#5
print(plates.pop_value())#4

# plates.add_value(10)
# plates.add_value(10)
# plates.add_value(10)
# plates.add_value(10)
# plates.add_value(20)
# plates.add_value(20)
# plates.add_value(20)
# plates.add_value(20)

print(plates.pop_value())
print(plates.pop_value())
print(plates.pop_value())


plates.add_value(9)
plates.add_value(10)
plates.add_value(16)
plates.add_value(17)
plates.add_value(18)
plates.add_value(19)
plates.add_value(20)
plates.add_value(21)

print(plates)