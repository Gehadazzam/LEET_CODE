# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next:
            return head
        last = head
        length = 1
        while last.next:
            last = last.next
            length += 1
        last.next = head
        k = k % length
        counter = length - k - 1
        temp = head
        for _ in range(counter):
            temp = temp.next
        new_head = temp.next
        temp.next = None
        return new_head