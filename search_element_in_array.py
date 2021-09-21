'''
Searching an element in an array
can be done in multiple ways
>using Index if given
>using binary search for efficiency
>Traversing each element and comparing the given value
'''

from array import *

arr1 = array('i', [10,11,12,13,14])

def searchElement(arr, value):
    for i in arr:
        if i == value:
            return "element found"
    return "Element not found"
'''
Time complexity is O(N) as we need to iterate over n elements here
space complexity is O(1) as we dont require any extra space
'''


print(searchElement(arr1, 11))
print(searchElement(arr1, 15))
print(searchElement(arr1, 13))