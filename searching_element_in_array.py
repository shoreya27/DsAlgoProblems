my_list = [4,5,6]

def findVal(lst, val):
    for i in lst:
        if i == val:
            return True
    return False

print(findVal(my_list, 15))
print(findVal(my_list, 4))