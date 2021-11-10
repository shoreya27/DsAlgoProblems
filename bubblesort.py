def bubblesort(lst):

    for i in range(len(lst)):
        for j in range(len(lst)-1-i):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    
    print(lst)


clst = [9,4,2,1,6,15,17]

print(clst)

bubblesort(clst)