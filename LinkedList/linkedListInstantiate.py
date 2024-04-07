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

def updateNode(target, newValue):
    curr = head
    while curr:
        if curr.value == target:
            curr.value = newValue
            break
        curr = curr.next

def deleteNode(head, val):
    prev = head
    curr = head.next
    while curr:
        if curr.value == val:
            prev.next = curr.next
            curr.next = None
            return curr
        prev = curr
        curr = curr.next

def removeFirst(head):
    if not head:
        return None
    curr = head
    head = head.next
    curr.next = None
    return curr

def removeLastNode(head):
    if not head:
        return None
    prev = head
    curr = prev.next
    if not curr.next:
        prev.next = None
        return curr
    while curr.next:
        prev = curr
        curr = curr.next
    prev.next = None
    return curr