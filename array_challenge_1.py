'''
Find Missing number challenge
Given an array of series 
'''

my_list = [1,2,3,5,6,7,8,9,10] #list of series 1 to 10

def find_missing(lst, series_of):
    sum_n = series_of*(series_of+1)
    sum_n = sum_n//2

    sum_of_given_lst = sum(lst)
    missing = sum_n - sum_of_given_lst
    print(missing)

find_missing(my_list, 10)