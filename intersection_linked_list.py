from interview_linkedlist_class import LinkedList, Node

node1 = Node(10)
node2 = Node(11)
node3 = Node(12)

lst1 = LinkedList()
lst2 = LinkedList()

lst1.add(5)
lst1.add(6)
lst1.add(7)
lst1.add_node(node1)
lst1.add_node(node2)
lst1.add_node(node3)
lst2.add(15)
lst2.add(16)
lst2.add(17)
lst2.add_node(node1)
lst2.add_node(node2)
lst2.add_node(node3)
print(lst2)
print(lst1)


def find_intersection(lst1, lst2):
    if not lst1.tail == lst2.tail:
        print("Not intersecting")
        return
    lst_elements = len(lst1)
    lst2_elements = len(lst2)
    start_1 = lst1.head
    start_2 = lst2.head
    steps_2 = steps_1 = None
    total_elements = lst_elements - lst2_elements
    if total_elements < 0:#lst2 is bigger
        steps_2 = -(total_elements)
    elif total_elements > 0: #lst1 is bigger
        steps_1 = total_elements

    if steps_2:
        start_2 = lst2_elements.head
        for i in range(steps_2):
            start_2 = start_2.next
    if steps_1:
        start_1 = lst1.head
        for i in range(steps_1):
            start_1 = start_1.next

    while start_1 or start_2:
        if start_1 == start_2:
            print(start_1.value)
            return
        start_1 = start_1.next
        start_2 = start_2.next

find_intersection(lst1, lst2)


lst3 = LinkedList()
lst4 = LinkedList()

lst3.generate_random(5, 10, 99)
lst4.generate_random(4, 10, 25)
lst3.add_node(node1)
lst4.add_node(node1)
print(lst3)
print(lst4)
find_intersection(lst3, lst4)