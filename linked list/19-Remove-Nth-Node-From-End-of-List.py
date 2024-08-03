# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        def getLength(node):
            count = 0
            while node:
                count += 1
                node = node.next
            return count
        length = getLength(head)
        if n > length:
            return head 
        ptr = dummy
        for _ in range(length - n):
            ptr = ptr.next
        if ptr.next:
            ptr.next = ptr.next.next
        return dummy.next