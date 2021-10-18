from interview_linkedlist_class import LinkedList

'''
Return Nth position
node from the last
'''

lst1 = LinkedList()
lst1.generate_random(10, 10, 99)
print(lst1)
def return_kth_node_from_last(k, lst):

    #find length
    total_nodes = len(lst1)
    steps_travrse = total_nodes - k + 1
    if steps_travrse < 1:
        return f"sorry list only have {total_nodes} nodes"
    start = lst1.head
    i = 1
    while i < steps_travrse:
        start = start.next
        i += 1
    return start.value

print(return_kth_node_from_last(1,lst1))
print(return_kth_node_from_last(10,lst1))
print(return_kth_node_from_last(15,lst1))
print(return_kth_node_from_last(4,lst1))
print(return_kth_node_from_last(5,lst1))
print(return_kth_node_from_last(9,lst1))
