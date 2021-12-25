arr = [9,-10,4,2,3,6,-5,8,7,-1]

#bubble sort 
#compare adjacent pairs in diff rounds
#continue comparing until arr gets sorted

def bubble_sort(arr):
    print(arr)
    ln = len(arr)
    print(ln)
    for round in range(0, ln):
        for j in range(0,ln-1-round):
            # print(j)
            if arr[j] > arr[j+1]:
                temp = arr[j+1]
                arr[j+1] = arr[j]
                arr[j] = temp
    
    print(arr)

bubble_sort(arr)