# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def reverse(node):
            prev = None
            while node:
                next_node = node.next
                node.next = prev
                prev = node
                node = next_node
            return prev
        head = reverse(head)
        current = head
        max_val = 0
        while current and current.next:
            if current.val > max_val:
                max_val = current.val
            if current.next.val < max_val:
                current.next = current.next.next
            else:
                current = current.next
        return reverse(head)