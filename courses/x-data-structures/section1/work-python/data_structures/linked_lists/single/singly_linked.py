class Node:
    def __init__(self, data):
        self.data = data    # Initialize the node with data
        self.next = None   # Initialize the next pointer to None
        self.prev = None

class SinglyLinkedList:
    def __init__(self):
        self.head = None    # Initialize the head of the list to None
        self.size = 0
    
    def length(self):
        return self.size
        
    def append(self, data):
        new_node = Node(data)
        # handle the special case at the beginning
        if not self.head:
            self.head = new_node
            self.size += 1
            return
        # start at the head
        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node
        self.size += 1
    
    def print_list(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end="->")
            current_node = current_node.next
        print("None")
        
    def find_element(self, target):
        current_node = self.head
        while current_node:
            if current_node.data == target:
                return True
            else:
                current_node = current_node.next
        return False
    
    def find_index(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node.data if current_node else None
    
    def insert(self, data, index):
        if index < 0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        new_node = Node(data)
        # if beginning
        if index == 0:
            new_node.next = self.head
            self.head = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next
            current_node.next = new_node
        
        self.size += 1
    
    def remove(self, index):
        if index < 0 or index > self.size:
            raise IndexError("Index Out of Bounds")
        # if beginning
        if index == 0:
            self.head = self.head.next
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next  # This line removes the node

        self.size -= 1
        
# Example usage
sll = SinglyLinkedList()
sll.append(1)
sll.append(2)
sll.append(3)
sll.print_list()  # Output: 1 -> 2 -> 3 -> None
# print(sll.find_element(4))
# # Find elements by index
# print(sll.find_index(0))  # Output: 1
# sll.insert(5, 0)
# sll.print_list()  # Output: 1 -> 2 -> 3 -> None
sll.remove(0)
sll.print_list()
