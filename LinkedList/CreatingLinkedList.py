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

    def append(self, value):
        temp = Node(value)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

l_list1 = LinkedList(4)
l_list1.append(5)
l_list1.append(7)
l_list1.append(1)
l_list1.print_list()