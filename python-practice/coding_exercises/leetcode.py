from typing import List, Optional

class SumSolution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashtable = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in hashtable:
                return [hashtable[complement], i]
            hashtable[num] = i

        print("No two numbers add up to target")
        return []
    
sol1 = SumSolution()
# Define a list of numbers and a target number
nums = [34, 38, 20, 50, 26, 41, 14, 31, 47, 2, 37, 10, 23, 50, 38, 45, 39, 20, 1, 6, 25, 46, 36, 12, 43, 40, 2, 21, 31, 17, 23, 43, 42, 34, 19, 20, 28, 25, 2, 29, 34, 50, 14, 4, 40, 8, 42, 7, 13, 39]
target = 9

# Call the twoSum method with the numbers and target
result = sol1.twoSum(nums, target)


#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class TwoNumSolution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        def linked_list_to_int(node):
            num = []
            while node:
                num.append(str(node.val))
                node = node.next
            return int(''.join(num[::-1]))

        def int_to_linked_list(num):
            dummy = ListNode(0)
            ptr = dummy
            for i in str(num):
                ptr.next = ListNode(int(i))
                ptr = ptr.next
            return dummy.next

        l1 = linked_list_to_int(l1)
        l2 = linked_list_to_int(l2)
        two_sum = str(l1 + l2)[::-1]
        return int_to_linked_list(two_sum)
        
        
        
sol2 = TwoNumSolution()
l1 = [2,4,3]
l2 = [5,6,4]
result = sol2.addTwoNumbers(l1, l2)
print(result)



class Solution:
    # 31ms
    def kthDistinct(self, arr: List[str], k: int) -> str:
        hashtable = {}
        for iteration, letter in enumerate(arr):
            if letter in hashtable:
                hashtable[letter] += 1
            else:
                hashtable[letter] = 1
        keys = []
        position = k - 1
        for key, value in hashtable.items():
            if value == 1:
                keys.append(key)
        if position < len(keys):
            return keys[position]
        else:
            return ""
        
