from interview_linkedlist_class import LinkedList

ll = LinkedList()
ll.generate_random(10, 10, 99)
print(ll)

def partition(lst, x):
    curr_node = lst.head
    lst.tail = lst.head 

    while curr_node:
        nxt = curr_node.next
        if curr_node.value < x:
            curr_node.next = lst.head
            lst.head = curr_node
        else:
            lst.tail.next = curr_node
            lst.tail = curr_node
            curr_node.next = None
        curr_node = nxt

partition(ll, 40)
print(ll)