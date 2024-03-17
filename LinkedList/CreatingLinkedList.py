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
        # appends a node to the end of LL
        temp = Node(value)
        if self.head == None:
            self.head = temp
            self.tail = temp
        else:
            self.tail.next = temp
            self.tail = temp
        self.length += 1
    
    def pop(self):
        # removes last element of a LL
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
        # adds a node to the beginning of LL
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
        # removes a node from beginning of LL
        if self.head == None:
            return None
        temp = self.head
        self.head = self.head.next
        temp.next = None
        self.length -= 1
        if self.length == 0:
            self.tail = None
        return temp
    
    def get(self, index):
        # get a node present at a specified index
        if index < 0 or index >= self.length:
            return None
        temp = self.head
        for _ in range(index):
            temp = temp.next
        return temp
    
    def set_value(self, index, value):
        # set a value of node at specified index
        temp = self.get(index)
        if temp:
            temp.value = value
            return True
        return False
    
    def insert(self, index, value):
        # insert a node at a specified index
        if index < 0 or index >= self.length:
            return False
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        temp = self.get(index - 1)
        new_node.next = temp.next
        temp.next = new_node
        self.length += 1
        return True
    
    def remove(self, index):
        # remove a node from specified index
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        elif index == self.length - 1:
            return self.pop()
        pre = self.get(index - 1)
        temp = pre.next
        pre.next = temp.next
        temp.next = None
        self.length -= 1
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
print(l_list1.print_list())
print(l_list1.length)
l_list1.prepend(67)
l_list1.prepend(78)
print(l_list1.print_list())
print(l_list1.get(0).value)
print(l_list1.get(10))
l_list1.set_value(1, 11)
print(l_list1.print_list())
l_list1.set_value(5, 11)
print(l_list1.print_list())
l_list1.insert(2, 33)
print(l_list1.print_list())
l_list1.remove(2)
l_list1.remove(0)
print(l_list1.print_list())