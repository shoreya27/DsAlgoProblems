from array import *

#declaration
my_arr = array('i')
print(my_arr)

element_arr = array('i', [1,2,3,4,5,6])
print(element_arr)

#O(1)
#insert at begining takes O(N)-----> all elements shiftd to right
element_arr.insert(0, 0)
print(element_arr)

#inserting at end of array takes O(1) as we kow the location and its empty
element_arr.insert(7,7)
print(element_arr)