class Queue:

    def __init__(self):
        self.list = []
    
    def isEmpty(self):
        if not self.list:
            return True
        return False
    
orders = Queue()
print(orders.isEmpty())#true