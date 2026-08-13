class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        temp = self.head
        while temp.next:
            temp = temp.next

        temp.next = new_node

    def insert_at_position(self, data, position):
        new_node = Node(data)

        if position == 0:
            new_node.next = self.head
            self.head = new_node
            return

        temp = self.head
        for i in range(position - 1):
            if temp is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    def display(self):
        temp = self.head
        elements = []

        while temp:
            elements.append(str(temp.data))
            temp = temp.next

        if elements:
            print(" -> ".join(elements))
        else:
            print("List is empty")

    def delete_head(self):
        if self.head is None:
            return

        self.head = self.head.next

    def delete_tail(self):
        if self.head is None:
            return

        if self.head.next is None:
            self.head = None
            return

        current = self.head
        while current.next.next is not None:
            current = current.next

        current.next = None

    def delete_at_position(self, position):
        if self.head is None:
            print("List is empty")
            return

        # If deleting the head node (position 0)
        if position == 0:
            self.head = self.head.next
            return

        temp = self.head
        # Traverse to the node just before the target position
        for i in range(position - 1):
            if temp is None or temp.next is None:
                print("Position out of range")
                return
            temp = temp.next

        if temp.next is None:
            print("Position out of range")
            return

        # Bypass the node to be deleted
        temp.next = temp.next.next


# Driver Code
ll = LinkedList()

ll.insert_at_end(10)
ll.insert_at_end(20)
ll.insert_at_end(30)

print("Original List:")
ll.display()

ll.insert_at_beginning(5)
print("After inserting 5 at beginning:")
ll.display()

ll.insert_at_position(15, 2)
print("After inserting 15 at position 2:")
ll.display()

ll.delete_at_position(2)
print("After deleting element at position 2:")
ll.display()

ll.delete_head()
print("After deleting at beginning:")
ll.display()

ll.delete_tail()
print("After deleting at end:")
ll.display()