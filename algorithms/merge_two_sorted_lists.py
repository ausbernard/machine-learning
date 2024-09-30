#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class BruteForceSolution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        # list to temp store values
        temp_vec = []
        # push values of l1 to temp
        while list1:
            temp_vec.append(list1.val)
            list1 = list1.next
        # push values of l2 to temp
        while list2:
            temp_vec.append(list2.val)
            list2 = list2.next
        # sort list
        temp_vec.sort()
        # create a new linked list
        temp_new = ListNode(-1)
        head = temp_new     # establish new head
        for vec in temp_vec:
            temp_new.next = ListNode(vec)
            temp_new = temp_new.next
        head = head.next

        return head
    # Time: O(N Log N)

class IterateSolution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode], d:
        # L1 [1] -> -> [3] -> [4] -> [5] -> [6]
        # Create a Dummy Node (fake head of list, stored at dummy.next -> L1(head))
        d = ListNode()
        # L2 [2] -> -> [3] -> [3] -> [4]
        cur = d
        
        while list1 and list2:
            if list1.val < list2.val:
                cur.next = list1
                cur = list1
                list1 = list1.next
            else:
                cur.next = list2
                cur = list2
                list2 = list2.next
        
        cur.next = list1 if list1 else list2
        
        return d.next
    # time(O(n))