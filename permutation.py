L1 = [2,3,4,1]
L2 = [1,2,3,4]

def isPermutation(L1,L2):
    if len(L1) != len(L2):
        print("Non permutated")
        return
    else:
        for i in L1:
            if i not in L2:
                print("Non Permutated")
                return
            else:
                if L1.count(i) != L2.count(i):
                    print("Non Permutated")
                    return
    print("Permutated List")
    return

isPermutation(L1,L2)
isPermutation([10,25,14],[10,25,66])
isPermutation([10,25,14],[10,25])
isPermutation([10,25,14],[10,14,25])