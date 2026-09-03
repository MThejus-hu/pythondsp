class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.tail = None

    def insert_at_head(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
        print(f"Inserted {data} at head.")

    def insert_at_tail(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail
        else:
            new_node.next = self.tail.next
            self.tail.next = new_node
            self.tail = new_node  
        print(f"Inserted {data} at tail.")


    def delete_value(self, key):
        if not self.tail:
            print("List is empty.")
            return

        curr = self.tail.next  
        prev = self.tail

        
        if curr == self.tail and curr.data == key:
            self.tail = None
            print(f"Deleted {key} from list.")
            return

        
        while True:
            if curr.data == key:
                prev.next = curr.next
                if curr == self.tail:  
                    self.tail = prev
                print(f"Deleted {key} from list.")
                return

            prev = curr
            curr = curr.next
            if curr == self.tail.next:  
                break

        print(f"Value {key} not found in the list.")

    
    def search(self, key):
        if not self.tail:
            return False

        curr = self.tail.next
        while True:
            if curr.data == key:
                return True
            curr = curr.next
            if curr == self.tail.next:
                break

        return False

    
    def display(self):
        if not self.tail:
            print("List is empty.")
            return

        nodes = []
        curr = self.tail.next  
        while True:
            nodes.append(str(curr.data))
            curr = curr.next
            if curr == self.tail.next:
                break

        print(" -> ".join(nodes) + f" -> (head: {self.tail.next.data})")



if __name__ == "__main__":
    csll = CircularSinglyLinkedList()


    csll.insert_at_head(20)
    csll.insert_at_head(10)
    csll.insert_at_tail(30)
    csll.insert_at_tail(40)
    csll.display()  

    
    print("Search 30:", csll.search(30))  # Output: True
    print("Search 99:", csll.search(99))  # Output: False

    
    csll.delete_value(10)  
    csll.display()  

    csll.delete_value(40)  
    csll.display()  