class Node:
    
    def __init__(self, data) -> None:
        self.data = data
        self.next = None

class LinkedList:

    def __init__(self) -> None:
        self.head = None

    def append_node(self, value):
        new_node = Node(value)

        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def find_node(self, node) -> bool:
        current_node = self.head

        while current_node.next: # while next is not none(empty)/essentially a while True statement
            if current_node.data == node:
                return True
            else:
                current_node = current_node.next
        return False 


my_linked = LinkedList()
my_linked.append_node(11)
my_linked.append_node(29)
my_linked.append_node(101)

value_exists = my_linked.find_node(11)
value_exists_two = my_linked.find_node(10)

print(value_exists)
print(value_exists_two)

