'''
List is a Python Built in ds
Stores an ordered collection of items sequentially
'''

shoppingList = ["milk", "cheese", "butter", "pencil"]

#Accessing Element same like an array
print(shoppingList[0])
print(shoppingList[2])

#list traversal can be done using loop
for i in shoppingList:
    print(i, end=" ")

'''
Updating a list
Time complexity is O(1)
'''
myList = [1,2,3,4,5]
print(f"Before {myList}")
myList[0] = 0
myList[1] = 1
print(f"After {myList}")

'''
Inserting an element in the list
>insert() ---- O(n) as n items needs to be shiftd if inserted in begining or middle
>append() ---- O(1) as enters at the end of list
>extend() ---- O(n) as new list n elements will b inserted at the end
'''
pages = [11,44,55,66,75,48]
print(pages)
pages.insert(1, 22)
pages.insert(3, 77)
pages.insert(10,99)#does not give error , just append the elemen at last if index is greater
print(pages)

cars = ["a", "b", "c"]
trucks = ["A", "B"]
cars.extend(trucks)
print(cars)

'''
Deletion of elements from list
>pop() ----> removes element from last index by default ------> O(n)|O(1)
>remove() ----> remove the element by itself without knowing itself -------> O(n)
>del() ----> removes the element from its index  ----n> O(n)
'''
books = [1,2,3,4,5]
print(books.pop(0))
print(books)# [2,3,4,5]
print(books.remove(4))
print(books)