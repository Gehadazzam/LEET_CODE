# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        current = head
        stack = []
        flag = True
        while current:
            stack.append(current.val)
            current = current.next        
        while head:
            idx = stack.pop()
            if idx != head.val:
                flag = False
            head = head.next
        return flag