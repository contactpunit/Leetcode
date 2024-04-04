# first create a Node class which instantiate each new node
class Node:
    def __init__(self, value) -> None:
        self.data = value
        self.next = None

node1 = Node('elem1')
head = node1

node2 = Node('elem2')
node3 = Node('elem3')
node4 = Node('elem4')

node1.next = node2
node2.next = node3
node3.next = node4

pointer = head

# Traversing a linked list and print values of each node
while pointer != None:
    print(pointer.value)
    pointer = pointer.next

#  Insert an element at beginning of LL

def insertBeginning():
    newNode = Node('beginning')
    newNode.next = head
    head = newNode

def insertEnd():
    endNode = Node('end')
    pointer = head
    while pointer.next == None:
        pointer = pointer.next
    pointer.next = endNode
    pointer = head

def insertMiddle(after = 'beginning'):
    pointer = head
    while pointer:
        if pointer.value == after:
            midNode = Node('mid')
            midNode.next = pointer.next
            pointer.next = midNode
            break
        else:
            pointer = pointer.next
    pointer = head