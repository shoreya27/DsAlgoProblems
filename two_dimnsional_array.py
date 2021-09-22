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
