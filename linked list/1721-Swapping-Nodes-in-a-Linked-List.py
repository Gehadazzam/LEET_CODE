# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        right = left = head 
        for _ in range(k - 1):
            right = right.next
        temp = right
        while right.next:
            right = right.next
            left = left.next
        temp.val, left.val = left.val, temp.val
        return head