# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode(0)
        sumVal = 0
        while l1 or l2 or sumVal:
            if l1:
                sumVal += l1.val
                l1 = l1.next
            if l2:
                sumVal += l2.val
                l2 = l2.next
            curr.next = (ListNode(sumVal%10))
            curr = curr.next
            sumVal //= 10
        return head.next