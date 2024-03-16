class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value) -> None:
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

l_list1 = LinkedList(4)
l_list2 = LinkedList(6)
print(l_list1)
print(l_list1.head.value)
print(l_list1.tail.value)
print(l_list2)