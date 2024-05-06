# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        stack = []
        current = head
        
        while current:
            while stack and stack[-1].val < current.val:
                #remove it if not greater than the right
                stack.pop()
            
            stack.append(current)
            current = current.next
        
        dummy = ListNode(0)
        prev = dummy
        #make list to return
        for node in stack:
            prev.next = node
            prev = prev.next
        
        prev.next = None
        
        return dummy.next