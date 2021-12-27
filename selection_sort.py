#time complexity is same :O(n)^2
#selection sort : useful only whn u got a small list of elements

arr = [100,7,1,-5,2,8,9,3,4,6,-7,4,25,14,36,85,45,22]

def selection_sort(arr):
    # print(arr, len(arr))
    for round in range(len(arr)-1):
        #find minimum element in each round
        smallest = arr[round]
        for ind,element in enumerate(arr[round:]):
            if element <= smallest:
                smallest,index = element, ind
        arr[index+round] = arr[round]
        arr[round] = smallest
    # print(arr)

selection_sort(arr)