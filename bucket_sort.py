arr = [3,9,5,1,7,2,4,6,16,8,29,150,47,86]
import math
from selection_sort import selection_sort
def bucket_sort(arr):

    #create n number of buckets
    print(arr)
    total = len(arr)
    buckts = round(math.sqrt(total))
    buckts_array = [ [] for i in range(buckts)]
    # print(buckts_array)
    #now insert each elements
    for element in arr:
        bucket_no = math.ceil((element*buckts)/max(arr))
        buckts_array[bucket_no-1].append(element)
    
    # print(buckts_array)

    #sort individual bucket using any algo
    for ar in buckts_array:
        selection_sort(ar)
    
    # print(buckts_array)
    #merge individual buckets
    result = []
    for ar in buckts_array:
        result += ar
    print(result)
bucket_sort(arr)
