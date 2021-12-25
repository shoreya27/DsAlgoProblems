#divide array into 2
#pick element from unsorted array and put them into
#there correct position in sorted array.


arr = [100,7,1,-5,2,8,9,3,4,6,-7,4,25,14,36,85,45,22]


def insertion_sort(arr):
    print(arr, len(arr))
    for round in range(len(arr)):
        element = arr[round]
        for index, val in enumerate(arr[:round]):
            if element<=val:
                # print("-----",index,"---",val)
                del arr[round]
                arr.insert(index,element)
                break
            
    print(arr)

insertion_sort(arr)