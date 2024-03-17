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
    
    def pop(self):
        if self.head == None:
            return None
        temp = self.head
        pre = self.head
        while temp.next:
            pre = temp
            temp = temp.next
        self.tail = pre
        self.tail.next = None
        self.length -= 1
        if self.length == 0:
            self.head = None
            self.tail = None
        return temp

    def prepend(self, value):
        new_node = Node(value)
        if self.head == None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        return True

    def pop_first(self):
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp

    def print_list(self):
        result = ''
        temp = self.head
        if self.head == None:
            return None
        while temp is not None:
            result += f'{str(temp.value)}  '
            temp = temp.next
        return result

l_list1 = LinkedList(4)
l_list1.append(5)
l_list1.append(7)
l_list1.append(1)
print(l_list1.print_list())
print(l_list1.pop().value)
print(l_list1.print_list())
print(l_list1.pop().value)
print(l_list1.print_list())
print(l_list1.pop().value)
print(l_list1.print_list())
l_list1.prepend(66)
print(l_list1.print_list())
l_list1.pop_first()
l_list1.pop_first()
l_list1.pop_first()
print(l_list1.print_list())