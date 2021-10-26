class AnimalShelter:

    def __init__(self):
        self.list = []
        self.cat_index = []
        self.dog_index = []
        self.index = 0

    def __str__(self):
        print(self.list)
        return ""

    def enqueue(self, val):
        self.list.append(val)
        if val == 'c':
            self.cat_index.append(self.index)
        else:
            self.dog_index.append(self.index)
        self.index += 1
    
    def dequeue_any(self):
        for i in range(len(self.list)):
            if self.list[i]:
                temp = self.list[i]
                if temp == 'c':
                    self.cat_index.pop(0)
                else:
                    self.dog_index.pop(0)
                self.list[i] = None
                return temp
        print("empty queue")
        self.index = 0
        self.list = []
        return ""

    def deque_dog(self):
        if self.dog_index:
            oldest_dog_index = self.dog_index.pop(0)
            last = self.list[oldest_dog_index]
            self.list[oldest_dog_index] = None
            return last
        print("Sorry! No Dog Available.")
        return ""
    def deque_cat(self):
        if self.cat_index:
            oldest_cat_index = self.cat_index.pop(0)
            last = self.list[oldest_cat_index]
            self.list[oldest_cat_index] = None
            return last
        print("Sorry! No Cat Available.")
        return ""

dogocatu = AnimalShelter()

dogocatu.enqueue('d')
dogocatu.enqueue('c')
dogocatu.enqueue('c')
dogocatu.enqueue('c')
dogocatu.enqueue('d')
dogocatu.enqueue('c')
dogocatu.enqueue('d')

print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)

print(dogocatu.dequeue_any())
print(dogocatu.dequeue_any())

print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)

print(dogocatu.deque_cat())
print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)

print(dogocatu.dequeue_any())
print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)

dogocatu.enqueue('c')
dogocatu.enqueue('d')
dogocatu.enqueue('c')
dogocatu.enqueue('d')

print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)


print(dogocatu.deque_dog())
print(dogocatu.deque_dog())

print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)

print(dogocatu.dequeue_any())
print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)


print(dogocatu.deque_dog())
print(dogocatu.deque_dog())

print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)
print(dogocatu.deque_dog())

print(dogocatu.dequeue_any())
print(dogocatu.dequeue_any())
print(dogocatu.dequeue_any())


dogocatu.enqueue('d')
dogocatu.enqueue('c')
dogocatu.enqueue('c')
dogocatu.enqueue('c')
dogocatu.enqueue('d')
dogocatu.enqueue('c')
dogocatu.enqueue('d')

print(dogocatu)
print(dogocatu.dog_index)
print(dogocatu.cat_index)