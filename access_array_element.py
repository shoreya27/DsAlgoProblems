from array import *

'''
Access an element from array 
takes O(1) because we are not
itrating over N elements, we are directly
providing the index position and this 
is the best part of using an array
'''

arr11 = array('i', [0,1,2,3,4])

def accessElement(arr, index):

    if index >= len(arr):
        print(f"There is no such index in this array:{arr}")
    else:
        print(f"Element at index {index} is :{arr11.__getitem__(index)}")

accessElement(arr11, 0)
accessElement(arr11, 1)
accessElement(arr11, 5)