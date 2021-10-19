from interview_linkedlist_class import LinkedList

lst1 = LinkedList()
lst1.generate_random(3, 1,10)
lst2 = LinkedList()
lst2.generate_random(3, 1, 10)
print(lst1)
print(lst2)

def sum_of_lsts(lst1, lst2):
    new_ll = LinkedList()
    start1 = lst1.head
    start2 = lst2.head
    add_on = 0

    while start1 and start2:
        sum_nodes = start1.value + start2.value + add_on
        remainder = sum_nodes
        add_on = 0
        if sum_nodes>=10:
            remainder = sum_nodes%10
            add_on = sum_nodes//10
        new_ll.add(remainder)
        start1 = start1.next
        start2 = start2.next
    print(new_ll)

sum_of_lsts(lst1, lst2)