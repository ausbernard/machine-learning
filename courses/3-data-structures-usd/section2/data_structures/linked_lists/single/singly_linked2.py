class SinglyNode:
    
    def __init__(self, val, next=None):
        self.val = val
        self.next = next
        
    def __str__(self):
        return str(self.val)
    
def display(head):
    current = head
    while current:
        print(current, end="->")
        current = current.next
    print("None")

def search(head, val):
    current = head
    while current:
        if val == current.val:
            return True
        current = current.next
    return False
    
Head = SinglyNode(1)
A = SinglyNode(3)
B = SinglyNode(4)
C = SinglyNode(7)

Head.next = A
A.next = B
B.next = C

display(Head)
print(search(Head, 7))
    