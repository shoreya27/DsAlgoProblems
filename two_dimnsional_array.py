from array import *
'''
we have to create 2D array using
numpy module and 
'''
import numpy as np
'''
Time complexity to create and initialise
an array requires O(1)
but if we create an empty array and then
individually add the element will take
O(n)
'''
arr = np.array([[1,2,3],[4,5,6],[7,8,9]])
print(arr)

'''
Insertion is done either
at begining, middle or at the end.
insert() isused to add [] as a row or column and takes O(mn)
'''
newArrr = np.insert(arr,0,[[100,200,300]],0)
print("Array after inserting a new row is:")
print(newArrr)

#insrting new array as a column
okarr = np.insert(arr,0,[[4,5,7]],1)
print("Array after inserting a new row is:")
print(okarr)

#Accessing element in 2D Array
'''
Time complexity for accessing an element takes O(1) as array are efficient for this only
Space Complexity is O(1) as this operation does not require any other operation space.
'''
def accessElement(arr, row, col):
    if row >= len(arr) or col >= len(arr[0]):
        print("wrong index provided")
    else:
        print(arr[row][col])

accessElement(okarr,2,2)#8
accessElement(okarr,3,1)#wrong index provided
accessElement(okarr,1,4)#wrong index provided

'''
Array Traversal: visiting each object in array
Time complexity is O(MN)
space complexity is O(1)
'''

def traverArr(arr):
    for row in range(len(arr)):
        for col in range(len(arr[0])):
            print(arr[row][col], end=" ")

traverArr(arr)