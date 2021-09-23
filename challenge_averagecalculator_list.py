'''
Input numbers from users
and print the average of thos
input values
'''
my_list = []
while True:
    i = input("enter a num: ")
    if i is "done":
        print("!!!") 
        break
    my_list.append(int(i))

avg = sum(my_list)//len(my_list)
print(avg)