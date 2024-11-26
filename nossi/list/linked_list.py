class Node:
    def __init__(self, value, next):
        self.value = value
        self.next = next


class LinkedList:
    def __init__(self, head):
        self.head = head
        self.tail = head

    def append(self, node):
        if self.head == None:
            self.head = node
            self.tail = node
        else:
            current = self.head
            while current.next:
                current = current.next
            current.next = node
            self.tail = node


ll = LinkedList(Node(1, None))
print(ll.tail.value)
ll.append(Node(2, None))
print(ll.tail.value)