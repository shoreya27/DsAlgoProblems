'''
Accessing|Updating In dictionary
Time complexity : O(1)
space complexity: O(1)
'''

my_dict = {"one":"1", "two":2}

#print --- 2
print(my_dict["one"])
print(my_dict["two"])

'''
Traversal in dictionary
Time complexity: O(n)
space complexity: O(1)
'''
name = {"name":"shoreya", 
        "age":25,
        "degree":"software engineer"
        }
for key in name:
    print(f"key:{key}, value:{name[key]}")
'''
Search a given value in 
dictionary --- linear search
Time complexity : O(n)
space complexity: O(1)
'''
for key in name:
    if name[key] == "shoreya":
        print(key, name[key])

'''
Deletion in dictionary
>pop()
>popitem()
>del keyword
>clear method
T = O(n)|O(1)
'''
items = {1:"mango", 2:"cream", 3:"herbs"}
val = items.pop(3)
print(val)
print(items)
del items[2]
print(items)