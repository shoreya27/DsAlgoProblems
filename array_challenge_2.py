'''
Given an array and target value
find distinct value pair indices.
'''
my_lst = [2,0,4,1,6,3]
target = 4

def findIndices(lst, val ):
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            if lst[i] + lst[j] == val and lst[i] != lst[j]:
                print(i,j)

findIndices(my_lst, target)