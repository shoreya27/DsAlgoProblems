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