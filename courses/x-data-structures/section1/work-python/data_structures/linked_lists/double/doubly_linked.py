class Node:
    def __init__(self, data, next=None, prev=None):
        self.data = data
        self.next = next
        self.prev = prev
    
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
        
    def display(self):
        current_node = self.head
        while current_node:
            print(current_node.data, end=" <-> ")
            current_node = current_node.next
        print("None")
    
    def append(self, data):
        new_node = Node(data)
        # empty list
        if not self.head:
            self.head = new_node
            self.tail = new_node
            self.size += 1
            return
        # not empty list
        else:
            self.tail.next = new_node   # Link the current tail's next to the new node
            new_node.prev = self.tail   # Link the new node's previous to the current tail
            self.tail = new_node        # Update the tail to be the new node
            self.size += 1
    
    def insert(self, data, index):
        new_node = Node(data)
        # beginning
        if index ==  0:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        # end
        elif index == self.size:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            new_node.next = current_node.next    # Set the new node's next to the current node's next
            new_node.prev = current_node.prev    # Set the new node's prev to the current node's prev
            current_node.next = new_node         # Link the current node's next to the new node
            new_node.next.prev = new_node        # Link the next node's previous to the new node
    
        self.size += 1
    
    def remove(self, index):
        if index < 0 or index >= self.size:
            raise IndexError("Index Out of Bounds")
        # beginning
        if index == 0:
            self.head = self.head.next
            self.head.prev = None
        # end (0 based iterations)
        elif index == (self.size - 1):
            self.tail = self.tail.prev
            self.tail.next = None
        else:
            current_node = self.head
            for _ in range(index - 1):
                current_node = current_node.next
            current_node.next = current_node.next.next
            current_node.next.prev = current_node
        
        self.size -= 1
            
            
            
    
dll = DoublyLinkedList()
dll.append(1)
dll.append(2)
dll.append(3)
dll.append(4)
dll.display()
dll.insert(5,1)
dll.display()
dll.remove(4)
dll.display()
    