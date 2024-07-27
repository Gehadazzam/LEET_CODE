# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def getLength(ptr):
            length = 0
            while ptr:
                length += 1
                ptr = ptr.next
            return length
        
        current = head
        length = getLength(current)
        middle_index = length // 2
        
        middle_node = head
        for _ in range(middle_index):
            middle_node = middle_node.next
        
        return middle_node