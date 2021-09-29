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