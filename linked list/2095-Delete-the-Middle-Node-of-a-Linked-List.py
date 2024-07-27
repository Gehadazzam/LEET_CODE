# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        
        def getLength(ptr):
            length = 0
            while ptr:
                length += 1
                ptr = ptr.next
            return length
        
        current = head
        length = getLength(current)
        middleIdx = length // 2
        
        middleNode = head
        for _ in range(middleIdx - 1):
            middleNode = middleNode.next
        
        middleNode.next = middleNode.next.next
        return head