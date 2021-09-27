my_list = [1,4,10,5,8,25,41,41]
new_lst = []

def checkDuplicate(lst):
    for i in lst:
        if i in new_lst:
            return False
        else:
            new_lst.append(i)
    print(new_lst)
    return True

print(checkDuplicate(my_list))#True --- unique
