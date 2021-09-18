array = [1,2,3,4,5,18,14,1,26,55,900,48,20,100000,2500,-1584]
# array = [0,1,-1]
big = array[0]
def find_biggest_num(sample_array,num):
    if len(sample_array) == 1:
        if num < sample_array[0]:
            return sample_array[0]
        else:
            return num
    if num < sample_array[0]:
        num = sample_array[0]
    return find_biggest_num(sample_array[1:],num)

print(find_biggest_num(array, big))
