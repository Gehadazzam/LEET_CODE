# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        while head and head.val == val:
            head = head.next      
        if not head:
            return None
        ptr = head
        while ptr.next:
            if ptr.next.val == val:
                ptr.next = ptr.next.next
            else:
                ptr = ptr.next
        return head