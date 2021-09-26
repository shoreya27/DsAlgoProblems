'''
Given a array of n integers
find Max product of 2 int values
1>can same int value be considered?
'''

my_list = [2,5,7,4,3,9,10,5,20]

def maxProduct(lst):
    max = 0
    for i in range(len(lst)):
        for j in range(i+1, len(lst)):
            prod = lst[i]*lst[j]
            if prod > max:
                max = prod
    print(max)

maxProduct(my_list)
'''
Time Complexity here is O(n*n)
'''
