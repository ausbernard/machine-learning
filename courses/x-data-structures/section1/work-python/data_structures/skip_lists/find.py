import random
class Node:
    def __init__(self, data=None, level = 0):
        self.data = data
        self.next = [None] * (level + 1)
        
class FindSkipList:
    def __init__(self, max_height=16):
        self.head = Node(level=max_height)
        self.height = 0
        self.max_height = max_height
    
    def random_level(self):
        level = 0
        while random.random() < 0.5 and level < self.max_height:
            level += 1
        return level
        
    def find_element(self, element):
        current_node = self.head
        for layer in range(self.height, -1, -1):
            while current_node.next[layer] and current_node.next[layer].data < element:
                current_node = current_node.next[layer]
        current_node =  current_node.next[0]
        if current_node and current_node.data == element:
            return True
        return False
    
    def find_element(self, element):
        current_node = self.head
        for layer in range(self.height, -1, -1):
            while current_node.next[layer] and current_node.next[layer].data < element:
                current_node = current_node.next[layer]
        current_node = current_node.next[0]
        if current_node and current_node.data == element:
            return True
        return False
    
    def insert_element(self, element):
        update = [None] * (self.max_height + 1)
        current_node = self.head
        for layer in range(self.height, -1, -1):
            while current_node.next[layer] and current_node.next[layer].data < element:
                current_node = current_node.next[layer]
            update[layer] = current_node
        level = self.random_level()
        if level > self.height:
            for i in range(self.height + 1, level + 1):
                update[i] = self.head
            self.height = level
        new_node = Node(data=element, level=level)
        for i in range(level + 1):
            new_node.next[i] = update[i].next[i]
            update[i].next[i] = new_node
            
    def print_list(self):
        for layer in range(self.height, -1, -1):
            current_node = self.head
            print(f"Level {layer}: ", end="")
            while current_node.next[layer]:
                print(current_node.next[layer].data, end=" -> ")
                current_node = current_node.next[layer]
            print("None")
    
    def math_probability(self):
        for i in range(0,6):
            print(f"{i}: {(1/2**i)}" )

skip_list = FindSkipList()
# Print the skip list
skip_list.print_list()
print(" ")
skip_list.insert_element(3)
skip_list.insert_element(6)
skip_list.insert_element(7)
skip_list.insert_element(9)
skip_list.insert_element(12)
skip_list.insert_element(17)
skip_list.insert_element(19)
skip_list.insert_element(21)
skip_list.insert_element(25)
skip_list.insert_element(26)

# Print the skip list
skip_list.print_list()
print(" ")
print(skip_list.find_element(19))  # Output: True
print(skip_list.find_element(15))  # Output: False

skip_list.math_probability()