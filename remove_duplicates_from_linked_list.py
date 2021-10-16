from interview_linkedlist_class import LinkedList

duplicate_lst = LinkedList()
duplicate_lst.add(1)
duplicate_lst.add(1)
duplicate_lst.add(2)
duplicate_lst.add(2)
duplicate_lst.add(3)
duplicate_lst.add(4)
print(duplicate_lst)

def delete_node(tmp, node):
    tmp.next = node.next

def remove_duplicates(lst):
    if not lst.head:
        print("list is empty")
        return
    start = lst.head
    elements = set()
    while start:
        if start.value in elements:
            delete_node(temp,start)
        else:
            elements.add(start.value)
        temp = start
        start = start.next

remove_duplicates(duplicate_lst)
print(duplicate_lst)

dups2 = LinkedList()#empty list
remove_duplicates(dups2)

dups2.add(1)
dups2.add(1)
print(dups2)
remove_duplicates(dups2)
print(dups2)

dups3 = LinkedList()
dups3.add(0)
dups3.add(1)
dups3.add(2)
dups3.add(4)
dups3.add(5)
dups3.add(5)
print(dups3)
remove_duplicates(dups3)
print(dups3)