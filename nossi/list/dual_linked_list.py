class DualNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.previous = None


class DualLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        new_node = DualNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.previous = self.tail
            self.tail = new_node
    def pop(self):
        self.tail = self.tail.previous
        self.tail.next = None

    def print(self):
        current = self.head
        while current.next:
            print(current.value, end=' ')
            current = current.next
        print(current.value)




dual_linked_list = DualLinkedList()
dual_linked_list.append(1)
dual_linked_list.append(2)
dual_linked_list.append(3)
dual_linked_list.append(4)
print(dual_linked_list.tail.value)
dual_linked_list.print()
dual_linked_list.pop()
print(dual_linked_list.tail.value)
dual_linked_list.print()


