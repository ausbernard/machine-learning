# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        dummy = ListNode(0)
        dummy.next = head
        slow = fast = dummy

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

            if slow == fast:
                return True
        return False
        # Time: O(1)


        # hash_set = set()
        # current = head
        # while head:      
        #     if current in hash_set:
        #         return True
        #     hash_set.add(current)
        #     if current.next is None:
        #         return False
        #     else:  
        #         current = current.next   
        # return False 
        # time: O(N)